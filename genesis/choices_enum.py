from enum import Enum
from typing import Any, List, Tuple, Type


class ChoicesEnum(Enum):
    @classmethod
    def choices(cls: Type) -> List[Tuple[str, Any, Any]]:
        return [(choice.name, choice.value, choice) for choice in cls]

    @classmethod
    def exists(cls: Type, value: str) -> bool:
        return value in cls.__members__

    @classmethod
    def values(cls: Type) -> List[Any]:
        return [choice.value for choice in cls]

    @classmethod
    def value_exists(cls: Type, value: str) -> bool:
        return value in cls.values()
