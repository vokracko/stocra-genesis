from decimal import Decimal

from genesis.currencies import Currency
from genesis.models import Amount, PlainInput, PlainOutput, PlainTransaction

TRANSACTION_ERC20_FAILED_JSON = {
    "blockHash": "0xe09640159123039346e644a410669b5d20eee569b8c7833281959b7c42d67c70",
    "blockNumber": "0xc3e2fb",
    "from": "0x980370651dcb658d1b05f93b179f63fc8dbf2896",
    "gas": "0xa954",
    "gasPrice": "0x55ae82600",
    "hash": "0x86985799e234a9b7e7dd2198404c498e82d78e5df5adb124887eebba56246890",
    "input": "0xa9059cbb000000000000000000000000dc05c435f07f2439732cae234639819530810cdc000000000000000000000000000000000000000000000000000000001b98d1c0",
    "nonce": "0xe",
    "to": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
    "transactionIndex": "0x11e",
    "value": "0x0",
    "type": "0x0",
    "v": "0x26",
    "r": "0xf2e3c90273d9e5c605e1896508ed7fa70d2009495c7762f1f014632a8a9acefd",
    "s": "0x247cc7611ce918f4a7f14c383962d3792cf6324ebcdaba2108df0802db70c109",
}
TRANSACTION_ERC20_FAILED_RECEIPT_JSON = {
    "blockHash": "0xe09640159123039346e644a410669b5d20eee569b8c7833281959b7c42d67c70",
    "blockNumber": "0xc3e2fb",
    "contractAddress": None,
    "cumulativeGasUsed": "0xdb1514",
    "effectiveGasPrice": "0x55ae82600",
    "from": "0x980370651dcb658d1b05f93b179f63fc8dbf2896",
    "gasUsed": "0xa89c",
    "logs": [],
    "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "status": "0x0",
    "to": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
    "transactionHash": "0x86985799e234a9b7e7dd2198404c498e82d78e5df5adb124887eebba56246890",
    "transactionIndex": "0x11e",
    "type": "0x0",
}

TRANSACTION_ERC20_FAILED_DECODED = PlainTransaction(
    hash="0x86985799e234a9b7e7dd2198404c498e82d78e5df5adb124887eebba56246890",
    inputs=[
        PlainInput(
            address="0x980370651dcb658d1b05f93b179f63fc8dbf2896",
            amount=Amount(
                value=Decimal("0.000992772"),
                currency_symbol=Currency.ETHER.symbol,
            ),
        ),
    ],
    outputs=[],
    fee=Amount(
        value=Decimal("0.000992772"),
        currency_symbol=Currency.ETHER.symbol,
    ),
)
