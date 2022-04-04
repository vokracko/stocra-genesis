from enum import unique

from genesis.choices_enum import ChoicesEnum


@unique
class TokenType(ChoicesEnum):
    ERC20 = "ERC20"
