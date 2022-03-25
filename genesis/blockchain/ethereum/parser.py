from decimal import Decimal
from typing import ClassVar

from genesis.blockchain.ethereum.adapter import EthereumNodeAdapter
from genesis.blockchain.ethereum.constants import (
    INPUT_ERC20_ADDRESS_LENGTH,
    INPUT_ERC20_ADDRESS_OFFSET,
    INPUT_ERC20_AMOUNT_OFFSET,
    INPUT_ERC20_TRANSFER_PREFIX,
)
from genesis.blockchain.parser import Parser
from genesis.blockchain_currencies import BLOCKCHAIN_CURRENCIES
from genesis.constants import BlockchainName, CurrencySymbol
from genesis.models import PlainBlock, PlainInput, PlainOutput, PlainTransaction


class EthereumParser(Parser):
    BLOCKCHAIN = BlockchainName.ETHEREUM
    CURRENCY: ClassVar[CurrencySymbol] = CurrencySymbol.ETH
    node_adapter: EthereumNodeAdapter
    SCALING_FACTOR = Decimal("1e-18")

    def __init__(self, node_adapter: EthereumNodeAdapter) -> None:
        super().__init__(node_adapter)

    async def decode_block(self, raw_block: dict) -> PlainBlock:
        return PlainBlock(
            height=int(raw_block["number"], 16),
            hash=raw_block["hash"],
            timestamp_ms=int(raw_block["timestamp"], 16),
            transactions=raw_block["transactions"],
        )

    async def decode_transaction(self, raw_transaction: dict, *, decode_inputs: bool) -> PlainTransaction:
        receipt = await self.node_adapter.get_transaction_receipt(raw_transaction["hash"])
        gas_used = await self.parse_gas_used(receipt)
        gas_price = await self.parse_gas_price(receipt)
        fee = gas_used * gas_price * self.SCALING_FACTOR
        amount = Decimal(int(raw_transaction["value"], 16)) * self.SCALING_FACTOR

        # TODO add case to parse erc20 transaction
        # TODO make sure that  erc20 transaction is successful
        # TODO handle case of contract that is not supported

        inputs = [
            PlainInput(
                address=raw_transaction["from"],
                amount=amount + fee,
            ),
        ]
        outputs = [
            PlainOutput(
                address=raw_transaction["to"],
                amount=amount,
            ),
        ]
        return PlainTransaction(
            hash=raw_transaction["hash"],
            inputs=inputs,
            outputs=outputs,
            fee=fee,
            amount=amount,
            currency_symbol=CurrencySymbol.ETH,
        )

    async def is_erc20_transfer(self, raw_transaction: dict) -> bool:
        return raw_transaction["input"].startswith(INPUT_ERC20_TRANSFER_PREFIX)

    async def parse_erc20_recipient(self, raw_transaction: dict) -> str:
        address_without_prefix = raw_transaction["input"][INPUT_ERC20_ADDRESS_OFFSET:INPUT_ERC20_ADDRESS_LENGTH]
        return f"0x{address_without_prefix}"

    async def parse_erc20_amount(self, raw_transaction: dict) -> Decimal:
        amount_hex = raw_transaction["input"][INPUT_ERC20_AMOUNT_OFFSET:]
        return Decimal(int(amount_hex, 16))

    async def scale_erc20_amount(self, currency: CurrencySymbol, value: Decimal) -> Decimal:
        return value * BLOCKCHAIN_CURRENCIES[self.BLOCKCHAIN][currency]["scaling"]

    async def parse_gas_used(self, raw_receipt: dict) -> Decimal:
        gas_used_hex = raw_receipt["gasUsed"]
        return Decimal(int(gas_used_hex, 16))

    async def parse_gas_price(self, raw_receipt: dict) -> Decimal:
        return Decimal(int(raw_receipt["effectiveGasPrice"], 16))
