from genesis.blockchain.adapter import NodeAdapter
from genesis.blockchain.bitcoin.adapter import BitcoinNodeAdapter  # noqa
from genesis.blockchain.bitcoin.parser import BitcoinParser  # noqs
from genesis.blockchain.ethereum.adapter import EthereumNodeAdapter  # noqa
from genesis.blockchain.ethereum.parser import EthereumParser  # noqa
from genesis.blockchain.parser import Parser
from genesis.constants import BlockchainName

ADAPTERS = {adapter.BLOCKCHAIN: adapter for adapter in NodeAdapter.__subclasses__()}
PARSERS = {parser.BLOCKCHAIN: parser for parser in Parser.__subclasses__()}


class NodeAdapterFactory:
    @classmethod
    def get_client(cls, blockchain: BlockchainName, *args: str, **kwargs: str) -> NodeAdapter:
        return ADAPTERS[blockchain](*args, **kwargs)


class ParserFactory:
    @classmethod
    def get_parser(cls, blockchain: BlockchainName, adapter: NodeAdapter) -> Parser:
        return PARSERS[blockchain](adapter)
