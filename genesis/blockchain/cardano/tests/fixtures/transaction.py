from decimal import Decimal

from genesis.currencies import Currency
from genesis.models import (
    Amount,
    PlainInput,
    PlainOutput,
    PlainTransaction,
    PlainTransactionPointer,
)

TRANSACTION_JSON = {
    "hash": "2802037e8724128bd6f7361606e2698dc71c5e929bfb528e55a8829601d7cb69",
    "inputs_outputs": [
        {
            "address": "DdzFFzCqrhsqz23SkTxevzJ3Dn4ee14BpQVe5T9LX2yWJpcjHToP2qxnzaEiy5qiHwNVtX5ANXtLJyBwKz8PvjJZYq2n8fyy7Dp9RqXa",
            "amount": Decimal("2.0E+5"),
            "transaction_pointer_hash": None,
            "transaction_pointer_index": None,
        },
        {
            "address": "DdzFFzCqrht8wAQiwNCromuPxNjQoK2Cs2vMiVFwFYYAQCcA1nPs7BMXFYhZZVBYhAKexYhaiA8xCUW8EEnc4Wdn6X5zD7R9xcabHip8",
            "amount": Decimal("358212"),
            "transaction_pointer_hash": None,
            "transaction_pointer_index": None,
        },
        {
            "address": "DdzFFzCqrhsm6jrC1KFcWNENb2PE171SDpg4rpaLytzVNFSsC8yGQpLggMTTSpedAKHmBUu9LtudohiHZ2zVjRKah38DVJyGVjWZoZPd",
            "amount": Decimal("729106"),
            "transaction_pointer_hash": "dbd87b3876da9847c01b7f229a4126ea113cdd17494ba6b86e714b4ca1864fcd",
            "transaction_pointer_index": 0,
        },
    ],
}

TRANSACTION_DECODED = PlainTransaction(
    hash="2802037e8724128bd6f7361606e2698dc71c5e929bfb528e55a8829601d7cb69",
    inputs=[
        PlainInput(
            address="DdzFFzCqrhsm6jrC1KFcWNENb2PE171SDpg4rpaLytzVNFSsC8yGQpLggMTTSpedAKHmBUu9LtudohiHZ2zVjRKah38DVJyGVjWZoZPd",
            amount=Amount(
                value=Decimal("0.729106"),
                currency_symbol=Currency.ADA.symbol,
            ),
            transaction_pointer=PlainTransactionPointer(
                transaction_hash="dbd87b3876da9847c01b7f229a4126ea113cdd17494ba6b86e714b4ca1864fcd", output_index=0
            ),
        )
    ],
    outputs=[
        PlainOutput(
            address="DdzFFzCqrhsqz23SkTxevzJ3Dn4ee14BpQVe5T9LX2yWJpcjHToP2qxnzaEiy5qiHwNVtX5ANXtLJyBwKz8PvjJZYq2n8fyy7Dp9RqXa",
            amount=Amount(
                value=Decimal("0.20"),
                currency_symbol=Currency.ADA.symbol,
            ),
        ),
        PlainOutput(
            address="DdzFFzCqrht8wAQiwNCromuPxNjQoK2Cs2vMiVFwFYYAQCcA1nPs7BMXFYhZZVBYhAKexYhaiA8xCUW8EEnc4Wdn6X5zD7R9xcabHip8",
            amount=Amount(
                value=Decimal("0.358212"),
                currency_symbol=Currency.ADA.symbol,
            ),
        ),
    ],
    amount=Amount(
        value=Decimal("0.558212"),
        currency_symbol=Currency.ADA.symbol,
    ),
    fee=Amount(
        value=Decimal("0.170894"),
        currency_symbol=Currency.ADA.symbol,
    ),
)
