from typing import ClassVar

from genesis.blockchain.bitcoin.adapter import BitcoinNodeAdapter
from genesis.constants import BlockchainName


class LitecoinNodeAdapter(BitcoinNodeAdapter):
    BLOCKCHAIN: ClassVar[BlockchainName] = BlockchainName.LITECOIN
