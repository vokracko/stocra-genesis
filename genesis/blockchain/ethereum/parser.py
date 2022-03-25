from decimal import Decimal
from typing import ClassVar

from genesis.blockchain.ethereum.constants import (
    INPUT_ERC20_ADDRESS_LENGTH,
    INPUT_ERC20_ADDRESS_OFFSET,
    INPUT_ERC20_AMOUNT_OFFSET,
    INPUT_ERC20_TRANSFER_PREFIX,
)
from genesis.blockchain_currencies import BLOCKCHAIN_CURRENCIES

ERC20_ADDRESS_OFFSET = len(INPUT_ERC20_TRANSFER_PREFIX) + INPUT_ERC20_ADDRESS_OFFSET

from genesis.blockchain.ethereum.adapter import EthereumNodeAdapter
from genesis.blockchain.parser import Parser
from genesis.constants import BlockchainName, CurrencySymbol
from genesis.models import PlainBlock, PlainInput, PlainOutput, PlainTransaction


class EthereumParser(Parser):
    BLOCKCHAIN = BlockchainName.ETHEREUM
    CURRENCY: ClassVar[CurrencySymbol] = CurrencySymbol.ETH
    node_adapter: EthereumNodeAdapter

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
        gas_used = Decimal(int(raw_transaction["gas"], 16))
        gas_price = Decimal(int(raw_transaction["gasPrice"], 16))
        fee = gas_used * gas_price / Decimal("1e18")
        amount = Decimal(int(raw_transaction["value"], 16)) / Decimal("1e18")

        return PlainTransaction(
            hash=raw_transaction["hash"],
            inputs=[PlainInput(address=raw_transaction["from"])],
            outputs=[PlainOutput(address=raw_transaction["to"], amount=amount)],
            fee=fee,
            amount=amount,
            currency_symbol=CurrencySymbol.ETH,
        )

    async def is_erc20_transfer(self, raw_transaction: dict) -> bool:
        return raw_transaction["input"].startswith(INPUT_ERC20_TRANSFER_PREFIX)

    async def parse_erc20_recipient(self, raw_transaction: dict) -> bool:
        address_without_prefix = raw_transaction["input"][INPUT_ERC20_ADDRESS_OFFSET:INPUT_ERC20_ADDRESS_LENGTH]
        return f"0x{address_without_prefix}"

    async def parse_erc20_amount(self, raw_transaction: dict) -> bool:
        amount_hex = raw_transaction["input"][INPUT_ERC20_AMOUNT_OFFSET:]
        return Decimal(int(amount_hex, 16))

    async def scale_erc20_amount(self, currency: CurrencySymbol, value: Decimal) -> Decimal:
        return value * BLOCKCHAIN_CURRENCIES[self.BLOCKCHAIN][currency]["scaling"]
