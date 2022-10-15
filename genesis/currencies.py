from enum import unique

from genesis.choices_enum import ChoicesEnum
from genesis.models import CurrencyInfo


@unique
class Currency(ChoicesEnum):
    BITCOIN = CurrencyInfo(symbol="BTC", name="Bitcoin")
    ETHER = CurrencyInfo(symbol="ETH", name="Ether")
    LITECOIN = CurrencyInfo(symbol="LTC", name="Litecoin")
    DOGECOIN = CurrencyInfo(symbol="DOGE", name="Dogecoin")
    ADA = CurrencyInfo(symbol="ADA", name="Ada")
    APTOS = CurrencyInfo(symbol="APT", name="Aptos")
    EOS = CurrencyInfo(symbol="EOS", name="Eos")

    @property
    def symbol(self) -> str:
        return self.value.symbol

    @property
    def currency_name(self) -> str:
        return self.value.name

    @classmethod
    def from_name(cls, currency_name: str) -> "Currency":
        for _, choice_value, choice in cls.choices():
            if currency_name == choice_value.name:
                return choice

        raise ValueError(f"`{currency_name}` not found")
