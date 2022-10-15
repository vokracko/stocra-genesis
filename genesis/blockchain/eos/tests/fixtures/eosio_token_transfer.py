from decimal import Decimal

from genesis.models import Amount, PlainInput, PlainOutput, PlainTransaction

TRANSACTION_JSON = {
    "trx": {
        "id": "c2d885f22b1598acd83ff26f136a7684a0c96dcf90488071955ddf90da79247a",
        "transaction": {
            "actions": [
                {
                    "account": "eosio.token",
                    "name": "transfer",
                    "data": {
                        "from": "mrnumberzero",
                        "to": "betdiceadmin",
                        "quantity": "2.5000 EOS",
                    },
                }
            ],
        },
    },
}

TRANSACTION_DECODED = PlainTransaction(
    hash="c2d885f22b1598acd83ff26f136a7684a0c96dcf90488071955ddf90da79247a",
    inputs=[
        PlainInput(
            address="mrnumberzero",
            amount=Amount(
                value=Decimal("2.5"),
                currency_symbol="EOS",
            ),
        )
    ],
    outputs=[
        PlainOutput(
            address="betdiceadmin",
            amount=Amount(
                value=Decimal("2.5"),
                currency_symbol="EOS",
            ),
        )
    ],
    fee=Amount(
        value=Decimal(0),
        currency_symbol="EOS",
    ),
)
