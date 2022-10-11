from decimal import Decimal

from genesis.currencies import Currency
from genesis.models import Amount, PlainInput, PlainOutput, PlainTransaction

TRANSACTION_JSON = {
    "version": "259182501",
    "hash": "0xb8d31179087466d9025e60735124c8712725e2c2a4bf4be198ca503b2acb2a6e",
    "state_checkpoint_hash": None,
    "gas_used": "0",
    "success": True,
    "vm_status": "Executed successfully",
    "accumulator_root_hash": "0xebb9fe1e60999dcaef3aee1dbc05727661dced49aad1e36f68326aeaa2655dd4",
    "id": "0x05fb53f2386cdc19eb74978c444affa494f4c89f9d122ecd326643217b0c4a6d",
    "epoch": "705",
    "round": "5477",
    "type": "block_metadata_transaction",
}

TRANSACTION_DECODED = PlainTransaction(
    hash="0xb8d31179087466d9025e60735124c8712725e2c2a4bf4be198ca503b2acb2a6e",
    inputs=[],
    outputs=[],
    fee=Amount(value=Decimal("0"), currency_symbol=Currency.APTOS.symbol),
)
