from typing import ClassVar

from genesis.blockchain.dogecoin.adapter import DogecoinNodeAdapter
from genesis.blockchain.litecoin.parser import LitecoinParser
from genesis.blockchains import Blockchain
from genesis.currencies import Currency
from genesis.logging import get_logger

logger = get_logger(__name__)


class DogecoinParser(LitecoinParser):
    BLOCKCHAIN: ClassVar[Blockchain] = Blockchain.DOGECOIN
    CURRENCY: ClassVar[Currency] = Currency.DOGECOIN
    node_adapter: DogecoinNodeAdapter
