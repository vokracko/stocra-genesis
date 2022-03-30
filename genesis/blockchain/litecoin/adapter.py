from typing import ClassVar

from genesis.blockchain.bitcoin.adapter import BitcoinNodeAdapter
from genesis.blockchains import Blockchain


class LitecoinNodeAdapter(BitcoinNodeAdapter):
    BLOCKCHAIN: ClassVar[Blockchain] = Blockchain.LITECOIN
