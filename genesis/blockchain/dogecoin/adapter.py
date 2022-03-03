from typing import ClassVar

from genesis.blockchain.litecoin.adapter import LitecoinNodeAdapter
from genesis.constants import BlockchainName


class DogecoinNodeAdapter(LitecoinNodeAdapter):
    BLOCKCHAIN: ClassVar[BlockchainName] = BlockchainName.DOGECOIN
