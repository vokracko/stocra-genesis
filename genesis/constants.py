from enum import Enum
from typing import List, Type


class ChoicesEnum(Enum):
    @classmethod
    def choices(cls: Type) -> List:
        return [(choice.name, choice.value) for choice in cls]


class BlockchainName(ChoicesEnum):
    BITCOIN = "bitcoin"
    ETHEREUM = "ethereum"
