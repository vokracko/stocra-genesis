from enum import Enum, unique
from typing import Any, List, Type

from genesis.models import CurrencyInfo


class ChoicesEnum(Enum):
    @classmethod
    def choices(cls: Type) -> List:
        return [(choice.name, choice.value) for choice in cls]

    @classmethod
    def exists(cls: Type, value: str) -> bool:
        return value in cls.__members__

    @classmethod
    def values(cls: Type) -> List[Any]:
        return [choice.value for choice in cls]

    @classmethod
    def value_exists(cls: Type, value: str) -> bool:
        return value in cls.values()


@unique
class BlockchainName(ChoicesEnum):
    BITCOIN = "bitcoin"
    ETHEREUM = "ethereum"
    LITECOIN = "litecoin"
    DOGECOIN = "dogecoin"
    CARDANO = "cardano"


class Currency(ChoicesEnum):
    BITCOIN = CurrencyInfo(symbol="BTC", name="Bitcoin")
    ETHER = CurrencyInfo(symbol="ETH", name="Ether")
    LITECOIN = CurrencyInfo(symbol="LTC", name="Litecoin")
    DOGECOIN = CurrencyInfo(symbol="DOGE", name="Dogecoin")
    ADA = CurrencyInfo(symbol="ADA", name="Ada")

    @property
    def symbol(self) -> str:
        return self.value.symbol

    @property
    def name(self) -> str:
        return self.value.name
