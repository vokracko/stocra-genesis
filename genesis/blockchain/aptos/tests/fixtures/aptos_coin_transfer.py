from decimal import Decimal

from genesis.currencies import Currency
from genesis.models import Amount, PlainInput, PlainOutput, PlainTransaction

TRANSACTION_JSON = {
    "hash": "0xd25466ad067f160e921461ca2f6f192e76076bd0a02b1bd703835b033c1690f9",
    "gas_used": "541",
    "success": True,
    "sender": "0xf6ce24e11d838d5ab9a91bc8d4e741975eba317b83eec99d06b0e68c72ad3c65",
    "max_gas_amount": "2000",
    "gas_unit_price": "101",
    "payload": {
        "function": "0x1::coin::transfer",
        "type_arguments": ["0x1::aptos_coin::AptosCoin"],
        "arguments": ["0x957cbc861a67de378c6658312d2dc0e61ac08d642bc476db6a02a0e2f9c56d5a", "1010000"],
        "type": "entry_function_payload",
    },
    "timestamp": "1667060580545488",
    "type": "user_transaction",
}


TRANSACTION_DECODED = PlainTransaction(
    hash="0xd25466ad067f160e921461ca2f6f192e76076bd0a02b1bd703835b033c1690f9",
    inputs=[
        PlainInput(
            address="0xf6ce24e11d838d5ab9a91bc8d4e741975eba317b83eec99d06b0e68c72ad3c65",
            amount=Amount(value=Decimal("0.00054641"), currency_symbol=Currency.APTOS.symbol),
        ),
        PlainInput(
            address="0xf6ce24e11d838d5ab9a91bc8d4e741975eba317b83eec99d06b0e68c72ad3c65",
            amount=Amount(value=Decimal("0.0101"), currency_symbol="0x1::aptos_coin::AptosCoin"),
        ),
    ],
    outputs=[
        PlainOutput(
            address="0x957cbc861a67de378c6658312d2dc0e61ac08d642bc476db6a02a0e2f9c56d5a",
            amount=Amount(value=Decimal("0.0101"), currency_symbol="0x1::aptos_coin::AptosCoin"),
        )
    ],
    fee=Amount(value=Decimal("0.00054641"), currency_symbol=Currency.APTOS.symbol),
)
