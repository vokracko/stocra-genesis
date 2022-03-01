from enum import Enum
from typing import Any, List, Type


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


class BlockchainName(ChoicesEnum):
    BITCOIN = "bitcoin"
    ETHEREUM = "ethereum"


class CurrencySymbol(ChoicesEnum):
    BTC = "BTC"
    ETH = "ETH"
    LTC = "LTC"
