from decimal import Decimal
from typing import ClassVar, Dict

from logging518 import get_logger

from genesis.blockchain.ethereum.adapter import EthereumNodeAdapter
from genesis.blockchain.ethereum.constants import (
    INPUT_ERC20_ADDRESS_LENGTH,
    INPUT_ERC20_ADDRESS_OFFSET,
    INPUT_ERC20_AMOUNT_OFFSET,
    INPUT_ERC20_TRANSFER_PREFIX,
)
from genesis.blockchain.ethereum.tokens import TOKENS
from genesis.blockchain.parser import Parser
from genesis.blockchains import Blockchain
from genesis.currencies import Currency
from genesis.models import (
    CurrencyInfo,
    PlainBlock,
    PlainInput,
    PlainOutput,
    PlainTransaction,
    TokenInfo,
)

logger = get_logger(__name__)


class EthereumParser(Parser):
    BLOCKCHAIN = Blockchain.ETHEREUM
    CURRENCY: ClassVar[Currency] = Currency.ETHER
    node_adapter: EthereumNodeAdapter
    TOKENS: ClassVar[Dict] = TOKENS
    SCALING_FACTOR = Decimal("1e-18")

    def __init__(self, node_adapter: EthereumNodeAdapter) -> None:
        super().__init__(node_adapter)

    async def decode_block(self, raw_block: dict) -> PlainBlock:
        return PlainBlock(
            height=int(raw_block["number"], 16),
            hash=raw_block["hash"],
            timestamp_ms=int(raw_block["timestamp"], 16) * 1_000,
            transactions=raw_block["transactions"],
        )

    async def decode_transaction(self, raw_transaction: dict) -> PlainTransaction:
        receipt = await self.node_adapter.get_transaction_receipt(raw_transaction["hash"])
        gas_used = await self._parse_gas_used(receipt)
        gas_price = await self._parse_gas_price(receipt)
        fee = gas_used * gas_price * self.SCALING_FACTOR

        if await self._is_erc20_transfer(raw_transaction):
            currency_symbol = raw_transaction["to"]
            amount = await self._parse_amount_erc20(raw_transaction)
            output_address = await self._parse_recipient_erc20(raw_transaction)
        else:
            currency_symbol = self.CURRENCY.symbol
            amount = Decimal(int(raw_transaction["value"], 16)) * self.SCALING_FACTOR
            output_address = raw_transaction["to"]

        # TODO handle case of contract that is not supported

        inputs = [
            PlainInput(
                address=raw_transaction["from"],
                amount=amount,
            ),
        ]
        outputs = [
            PlainOutput(
                address=output_address,
                amount=amount,
            ),
        ]
        return PlainTransaction(
            hash=raw_transaction["hash"],
            inputs=inputs,
            outputs=outputs,
            fee=fee,
            amount=amount,
            currency_symbol=currency_symbol,
        )

    async def _is_erc20_transfer(self, raw_transaction: dict) -> bool:
        return raw_transaction["input"].startswith(INPUT_ERC20_TRANSFER_PREFIX)

    async def _get_token_info(self, raw_transaction: dict) -> TokenInfo:
        contract_address = raw_transaction["to"]
        token_info = self.TOKENS.get(contract_address.lower())

        if token_info:
            return token_info

        logger.warning("Unknown erc20 currency: %s", raw_transaction["to"])
        return TokenInfo(currency=CurrencyInfo(symbol=contract_address, name=contract_address), scaling=Decimal("1"))

    async def _parse_recipient_erc20(self, raw_transaction: dict) -> str:
        address_without_prefix = raw_transaction["input"][INPUT_ERC20_ADDRESS_OFFSET:INPUT_ERC20_ADDRESS_LENGTH]
        return f"0x{address_without_prefix}"

    async def _parse_amount_erc20(self, raw_transaction: dict) -> Decimal:
        amount_hex = raw_transaction["input"][INPUT_ERC20_AMOUNT_OFFSET:]
        return Decimal(int(amount_hex, 16))

    async def _parse_gas_used(self, raw_receipt: dict) -> Decimal:
        gas_used_hex = raw_receipt["gasUsed"]
        return Decimal(int(gas_used_hex, 16))

    async def _parse_gas_price(self, raw_receipt: dict) -> Decimal:
        return Decimal(int(raw_receipt["effectiveGasPrice"], 16))
