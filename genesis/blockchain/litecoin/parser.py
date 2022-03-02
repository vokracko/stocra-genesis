from typing import ClassVar

import logging518 as logging

from genesis.blockchain.bitcoin.parser import BitcoinParser
from genesis.blockchain.litecoin.adapter import LitecoinNodeAdapter
from genesis.constants import BlockchainName, CurrencySymbol

logger = logging.get_logger(__name__)


class LitecoinParser(BitcoinParser):
    BLOCKCHAIN: ClassVar[BlockchainName] = BlockchainName.LITECOIN
    CURRENCY_SYMBOL: ClassVar[CurrencySymbol] = CurrencySymbol.LTC
    node_adapter: LitecoinNodeAdapter
