from decimal import Decimal

from genesis.constants import CurrencySymbol
from genesis.models import PlainInput, PlainOutput, PlainTransaction

TRANSACTION_JSON = {
    "blockHash": "0x8e38b4dbf6b11fcc3b9dee84fb7986e29ca0a02cecd8977c161ff7333329681e",
    "blockNumber": "0xf4240",
    "from": "0x39fa8c5f2793459d6622857e7d9fbb4bd91766d3",
    "gas": "0x1f8dc",
    "gasPrice": "0x12bfb19e60",
    "hash": "0xea1093d492a1dcb1bef708f771a99a96ff05dcab81ca76c31940300177fcf49f",
    "input": "0x",
    "nonce": "0x15",
    "to": "0xc083e9947cf02b8ffc7d3090ae9aea72df98fd47",
    "transactionIndex": "0x0",
    "value": "0x56bc75e2d63100000",
    "type": "0x0",
    "v": "0x1c",
    "r": "0xa254fe085f721c2abe00a2cd244110bfc0df5f4f25461c85d8ab75ebac11eb10",
    "s": "0x30b7835ba481955b20193a703ebc5fdffeab081d63117199040cdf5a91c68765",
}

TRANSACTION_DECODED = PlainTransaction(
    hash="0xea1093d492a1dcb1bef708f771a99a96ff05dcab81ca76c31940300177fcf49f",
    inputs=[
        PlainInput(
            address="0x39fa8c5f2793459d6622857e7d9fbb4bd91766d3",
            transaction_pointer=None,
            amount=None,  # TODO
        )
    ],
    outputs=[PlainOutput(address="0xc083e9947cf02b8ffc7d3090ae9aea72df98fd47", amount=Decimal("100"))],
    amount=Decimal("100"),
    fee=Decimal("0.002354887722"),
    currency_symbol=CurrencySymbol.ETH,
)
