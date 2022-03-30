from typing import ClassVar

import logging518 as logging

from genesis.blockchain.dogecoin.adapter import DogecoinNodeAdapter
from genesis.blockchain.litecoin.parser import LitecoinParser
from genesis.blockchains import Blockchain
from genesis.currencies import Currency

logger = logging.get_logger(__name__)


class DogecoinParser(LitecoinParser):
    BLOCKCHAIN: ClassVar[Blockchain] = Blockchain.DOGECOIN
    CURRENCY: ClassVar[Currency] = Currency.DOGECOIN
    node_adapter: DogecoinNodeAdapter
