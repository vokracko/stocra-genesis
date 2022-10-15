from typing import Dict, Type

from genesis.blockchain.adapter import NodeAdapter
from genesis.blockchain.aptos.adapter import AptosNodeAdapter
from genesis.blockchain.aptos.parser import AptosParser
from genesis.blockchain.bitcoin.adapter import BitcoinNodeAdapter
from genesis.blockchain.bitcoin.parser import BitcoinParser
from genesis.blockchain.cardano.adapter import CardanoNodeAdapter
from genesis.blockchain.cardano.parser import CardanoParser
from genesis.blockchain.dogecoin.adapter import DogecoinNodeAdapter
from genesis.blockchain.dogecoin.parser import DogecoinParser
from genesis.blockchain.eos.adapter import EosNodeAdapter
from genesis.blockchain.eos.parser import EosParser
from genesis.blockchain.ethereum.adapter import EthereumNodeAdapter
from genesis.blockchain.ethereum.parser import EthereumParser
from genesis.blockchain.litecoin.adapter import LitecoinNodeAdapter
from genesis.blockchain.litecoin.parser import LitecoinParser
from genesis.blockchain.parser import Parser
from genesis.blockchains import Blockchain

ADAPTERS: Dict[Blockchain, Type[NodeAdapter]] = {
    BitcoinNodeAdapter.BLOCKCHAIN: BitcoinNodeAdapter,
    EthereumNodeAdapter.BLOCKCHAIN: EthereumNodeAdapter,
    LitecoinNodeAdapter.BLOCKCHAIN: LitecoinNodeAdapter,
    DogecoinNodeAdapter.BLOCKCHAIN: DogecoinNodeAdapter,
    CardanoNodeAdapter.BLOCKCHAIN: CardanoNodeAdapter,
    AptosNodeAdapter.BLOCKCHAIN: AptosNodeAdapter,
    EosNodeAdapter.BLOCKCHAIN: EosNodeAdapter,
}
PARSERS: Dict[Blockchain, Type[Parser]] = {
    BitcoinParser.BLOCKCHAIN: BitcoinParser,
    EthereumParser.BLOCKCHAIN: EthereumParser,
    LitecoinParser.BLOCKCHAIN: LitecoinParser,
    DogecoinParser.BLOCKCHAIN: DogecoinParser,
    CardanoParser.BLOCKCHAIN: CardanoParser,
    AptosParser.BLOCKCHAIN: AptosParser,
    EosParser.BLOCKCHAIN: EosParser,
}


class NodeAdapterFactory:
    @classmethod
    async def get_client(cls, blockchain: Blockchain, *args: str, **kwargs: str) -> NodeAdapter:
        client = ADAPTERS[blockchain](*args, **kwargs)
        await client.init_async()
        return client


class ParserFactory:
    @classmethod
    async def get_parser(cls, blockchain: Blockchain, adapter: NodeAdapter) -> Parser:
        return PARSERS[blockchain](adapter)
