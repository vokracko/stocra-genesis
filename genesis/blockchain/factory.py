from genesis.blockchain.adapter import NodeAdapter
from genesis.blockchain.bitcoin.adapter import BitcoinNodeAdapter
from genesis.blockchain.bitcoin.parser import BitcoinParser
from genesis.blockchain.ethereum.adapter import EthereumNodeAdapter
from genesis.blockchain.ethereum.parser import EthereumParser
from genesis.blockchain.parser import Parser
from genesis.constants import BlockchainName

ADAPTERS = {
    BitcoinNodeAdapter.BLOCKCHAIN: BitcoinNodeAdapter,
    EthereumNodeAdapter.BLOCKCHAIN: EthereumNodeAdapter,
}
PARSERS = {BitcoinParser.BLOCKCHAIN: BitcoinNodeAdapter, EthereumParser.BLOCKCHAIN: EthereumParser}


class NodeAdapterFactory:
    @classmethod
    def get_client(cls, blockchain: BlockchainName, *args: str, **kwargs: str) -> NodeAdapter:
        return ADAPTERS[blockchain](*args, **kwargs)


class ParserFactory:
    @classmethod
    def get_parser(cls, blockchain: BlockchainName, adapter: NodeAdapter) -> Parser:
        return PARSERS[blockchain](adapter)
