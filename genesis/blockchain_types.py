from enum import unique

from genesis.choices_enum import ChoicesEnum


@unique
class BlockchainType(ChoicesEnum):
    ACCOUNT = "account"
    UTXO = "utxo"
