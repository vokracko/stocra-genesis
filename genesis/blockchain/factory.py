from typing import Dict, Type

from genesis.blockchain.adapter import NodeAdapter
from genesis.blockchain.bitcoin.adapter import BitcoinNodeAdapter
from genesis.blockchain.bitcoin.parser import BitcoinParser
from genesis.blockchain.ethereum.adapter import EthereumNodeAdapter
from genesis.blockchain.ethereum.parser import EthereumParser
from genesis.blockchain.parser import Parser
from genesis.constants import BlockchainName

ADAPTERS = {adapter.BLOCKCHAIN: adapter for adapter in NodeAdapter.__subclasses__()}
PARSERS = {parser.BLOCKCHAIN: parser for parser in Parser.__subclasses__()}


class NodeAdapterFactory:
    @classmethod
    def get_client(cls, blockchain_name: str, *args: str, **kwargs: str) -> NodeAdapter:
        return ADAPTERS[BlockchainName(blockchain_name)](*args, **kwargs)


class ParserFactory:
    @classmethod
    def get_parser(cls, blockchain_name: str, adapter: NodeAdapter) -> Parser:
        return PARSERS[BlockchainName(blockchain_name)](adapter)
