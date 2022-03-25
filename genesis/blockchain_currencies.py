from decimal import Decimal
from types import MappingProxyType

from genesis.constants import BlockchainName, CurrencySymbol

BLOCKCHAIN_CURRENCIES = MappingProxyType(
    {
        BlockchainName.BITCOIN: {
            CurrencySymbol.BTC: None,
        },
        BlockchainName.ETHEREUM: {
            CurrencySymbol.ETH: None,
            CurrencySymbol.USDT: dict(
                address="0xdac17f958d2ee523a2206206994597c13d831ec7",
                scaling=Decimal("1e-6"),
            ),
        },
        BlockchainName.LITECOIN: {
            CurrencySymbol.LTC: None,
        },
        BlockchainName.DOGECOIN: {
            CurrencySymbol.DOGE: None,
        },
    }
)
