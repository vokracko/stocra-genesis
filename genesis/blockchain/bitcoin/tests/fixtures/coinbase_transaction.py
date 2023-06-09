from decimal import Decimal

from genesis.currencies import Currency
from genesis.models import (
    Amount,
    PlainAddress,
    PlainOutput,
    PlainTransaction,
    PlainTransactionHash,
)

TRANSACTION_HASH = "682fd04fe5a80d2e238074e2c28d3ecb7c85786326fb96dd0527865f11aee8ed"

TRANSACTION_JSON = {
    "txid": TRANSACTION_HASH,
    "hash": TRANSACTION_HASH,
    "version": 1,
    "size": 134,
    "vsize": 134,
    "weight": 536,
    "locktime": 0,
    "vin": [{"coinbase": "0453ec131c0122", "sequence": 4294967295}],
    "vout": [
        {
            "value": 50.0,
            "n": 0,
            "scriptPubKey": {
                "address": "1KnUs1jKkSbcNwBt7gA4PaRKhiabuVXsaT",
            },
        }
    ],
    "hex": "01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff070453ec131c0122ffffffff0100f2052a01000000434104c7b1f1d0537b9d800f4413e0222370f7fb8c3844fc98dafe9bdbfea27650ef78d3cb89ab50224934c6473e8e925cfdb42c4c6f32145bf4ea87ecda17a0e24e4fac00000000",  # noqa
    "blockhash": "0000000005c2d08ba95b80f856959c892cfdb5b55e687399ee89726989d71a04",
    "confirmations": 650012,
    "time": 1273915632,
    "blocktime": 1273915632,
}
TRANSACTION_DECODED = PlainTransaction(
    hash=PlainTransactionHash(TRANSACTION_HASH),
    inputs=[],
    outputs=[
        PlainOutput(
            address=PlainAddress("1KnUs1jKkSbcNwBt7gA4PaRKhiabuVXsaT"),
            amount=Amount(value=Decimal("50"), currency_symbol=Currency.BITCOIN.symbol),
        ),
    ],
    fee=Amount(value=Decimal("0"), currency_symbol=Currency.BITCOIN.symbol),
)
