from decimal import Decimal

from genesis.blockchain.ethereum.adapter import EthereumNodeAdapter
from genesis.blockchain.parser import Parser
from genesis.constants import BlockchainName
from genesis.models import PlainBlock, PlainInput, PlainOutput, PlainTransaction


class EthereumParser(Parser):
    BLOCKCHAIN = BlockchainName.ETHEREUM
    node_adapter: EthereumNodeAdapter

    def __init__(self, node_adapter: EthereumNodeAdapter) -> None:
        super().__init__(node_adapter)

    async def decode_block(self, raw_block: dict) -> PlainBlock:
        transactions = [await self.decode_transaction(tx) for tx in raw_block["transactions"]]
        return PlainBlock(
            height=int(raw_block["number"], 16),
            hash=raw_block["hash"],
            timestamp=int(raw_block["timestamp"], 16),
            transactions=transactions,
        )

    async def decode_transaction(self, raw_transaction: dict) -> PlainTransaction:
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
        )
