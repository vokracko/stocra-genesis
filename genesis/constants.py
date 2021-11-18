from enum import Enum
from typing import List, Type


class BlockchainName(Enum):
    BITCOIN = "bitcoin"
    ETHEREUM = "ethereum"

    @classmethod
    def choices(self, cls: Type) -> List:
        return [(choice.name, choice.value) for choice in cls]
