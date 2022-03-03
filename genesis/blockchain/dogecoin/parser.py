from typing import ClassVar

import logging518 as logging

from genesis.blockchain.dogecoin.adapter import DogecoinNodeAdapter
from genesis.blockchain.litecoin.parser import LitecoinParser
from genesis.constants import BlockchainName, CurrencySymbol

logger = logging.get_logger(__name__)


class DogecoinParser(LitecoinParser):
    BLOCKCHAIN: ClassVar[BlockchainName] = BlockchainName.DOGECOIN
    CURRENCY_SYMBOL: ClassVar[CurrencySymbol] = CurrencySymbol.DOGE
    node_adapter: DogecoinNodeAdapter
