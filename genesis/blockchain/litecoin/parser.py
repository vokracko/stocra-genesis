from typing import ClassVar

from genesis.blockchain.bitcoin.parser import BitcoinParser
from genesis.blockchain.litecoin.adapter import LitecoinNodeAdapter
from genesis.blockchains import Blockchain
from genesis.currencies import Currency
from genesis.logging import get_logger

logger = get_logger(__name__)


class LitecoinParser(BitcoinParser):
    BLOCKCHAIN: ClassVar[Blockchain] = Blockchain.LITECOIN
    CURRENCY: ClassVar[Currency] = Currency.LITECOIN
    node_adapter: LitecoinNodeAdapter
