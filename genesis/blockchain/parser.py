from typing import ClassVar, Dict

from genesis.blockchain.adapter import NodeAdapter
from genesis.constants import BlockchainName, Currency
from genesis.models import PlainBlock, PlainTransaction


class Parser:
    BLOCKCHAIN: ClassVar[BlockchainName]
    CURRENCY: ClassVar[Currency]
    TOKENS: ClassVar[Dict] = dict()
    node_adapter: NodeAdapter

    def __init__(self, node_adapter: NodeAdapter) -> None:
        self.node_adapter = node_adapter

    async def decode_block(self, raw_block: dict) -> PlainBlock:
        raise NotImplementedError

    async def decode_transaction(self, raw_transaction: dict, *, decode_inputs: bool) -> PlainTransaction:
        raise NotImplementedError
