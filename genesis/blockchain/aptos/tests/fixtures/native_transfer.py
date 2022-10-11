from decimal import Decimal

from genesis.currencies import Currency
from genesis.models import Amount, PlainInput, PlainOutput, PlainTransaction

TRANSACTION_JSON = {
    "hash": "0xbaa1c32627eb9a77843b849aa7b554583729b7fff6b8278919582cf162162b72",
    "gas_used": "529",
    "success": True,
    "sender": "0x1f44250a22f363940f581bb2d5695c5cdd5cbcb6c6c12e036871238d736fc278",
    "gas_unit_price": "100",
    "payload": {
        "function": "0x1::aptos_account::transfer",
        "type_arguments": [],
        "arguments": ["0xe0592a2bcd16539ed84b384e54ec22c5d860ef145d80522abbf2349b46f9a8a6", "210000000"],
        "type": "entry_function_payload",
    },
    "type": "user_transaction",
}

TRANSACTION_DECODED = PlainTransaction(
    hash="0xbaa1c32627eb9a77843b849aa7b554583729b7fff6b8278919582cf162162b72",
    inputs=[
        PlainInput(
            address="0x1f44250a22f363940f581bb2d5695c5cdd5cbcb6c6c12e036871238d736fc278",
            amount=Amount(value=Decimal("2.100529"), currency_symbol=Currency.APTOS.symbol),
        )
    ],
    outputs=[
        PlainOutput(
            address="0xe0592a2bcd16539ed84b384e54ec22c5d860ef145d80522abbf2349b46f9a8a6",
            amount=Amount(value=Decimal("2.1"), currency_symbol=Currency.APTOS.symbol),
        )
    ],
    fee=Amount(value=Decimal("0.000529"), currency_symbol=Currency.APTOS.symbol),
)
