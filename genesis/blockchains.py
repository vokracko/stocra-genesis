from enum import unique

from genesis.blockchain_types import BlockchainType
from genesis.choices_enum import ChoicesEnum
from genesis.models import BlockchainInfo


@unique
class Blockchain(ChoicesEnum):
    BITCOIN = BlockchainInfo(name="bitcoin", type=BlockchainType.UTXO)
    ETHEREUM = BlockchainInfo(name="ethereum", type=BlockchainType.ACCOUNT)
    LITECOIN = BlockchainInfo(name="litecoin", type=BlockchainType.UTXO)
    DOGECOIN = BlockchainInfo(name="dogecoin", type=BlockchainType.UTXO)
    CARDANO = BlockchainInfo(name="cardano", type=BlockchainType.UTXO)
    APTOS = BlockchainInfo(name="aptos", type=BlockchainType.ACCOUNT)

    @property
    def blockchain_name(self) -> str:
        return self.value.name

    @property
    def type(self) -> BlockchainType:
        return self.value.type

    @classmethod
    def from_name(cls, blockchain_name: str) -> "Blockchain":
        for _, choice_value, choice in cls.choices():
            if blockchain_name == choice_value.name:
                return choice

        raise ValueError(f"`{blockchain_name}` not found")
