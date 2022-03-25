from decimal import Decimal

from genesis.constants import CurrencySymbol
from genesis.models import PlainInput, PlainOutput, PlainTransaction

TRANSACTION_JSON = {
    "blockHash": "0x6bd7e3f6176b483b55e7d71ba96da60f9a93435b564315ff1dbd1c0a14f2d97d",
    "blockNumber": "0xbe0ac8",
    "from": "0x18916e1a2933cb349145a280473a5de8eb6630cb",
    "gas": "0x5208",
    "gasPrice": "0x1176592e00",
    "hash": "0xffac6416d8e24f9d8e308a7acf2ff58a576d14967795926ddd37376031d8f5ee",
    "input": "0x",
    "nonce": "0x1579fa",
    "to": "0xd67f401f48d9bd30e8860ace01bff1bcd4675f1e",
    "transactionIndex": "0xe4",
    "value": "0x1a7c4872ccf000",
    "type": "0x0",
    "v": "0x25",
    "r": "0xd456f69b86467b032a6fa00bc0fa5b30092307acb7fc7818b8751a9278d6a523",
    "s": "0x6984e68fff73a6da23d91b986cc9d624470fdb84c852f3208a2f0ca0cac08c1c",
}

# TRANSACTION_DECODED = PlainTransaction(
#     hash="0xea1093d492a1dcb1bef708f771a99a96ff05dcab81ca76c31940300177fcf49f",
#     inputs=[
#         PlainInput(
#             address="0x39fa8c5f2793459d6622857e7d9fbb4bd91766d3",
#             transaction_pointer=None,
#             amount=None,  # TODO
#         )
#     ],
#     outputs=[PlainOutput(address="0xc083e9947cf02b8ffc7d3090ae9aea72df98fd47", amount=Decimal("100"))],
#     amount=Decimal("100"),
#     fee=Decimal("0.002354887722"),
#     currency_symbol=CurrencySymbol.ETH,
# )
