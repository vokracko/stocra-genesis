from decimal import Decimal

from genesis.currencies import Currency
from genesis.models import Amount, PlainInput, PlainOutput, PlainTransaction

ERC20_TRANSACTION_UNKNOWN_JSON = {
    "blockHash": "0x6fdb4caf69ebd6abd484e558c04cd46a901a7da88e8e3bfa357e574fb9053680",
    "blockNumber": "0xdc8f86",
    "from": "0x5041ed759dd4afc3a72b8192c143f72f4724081a",
    "gas": "0x668a0",
    "gasPrice": "0xc1b710800",
    "hash": "0x6a85deb137f805512e34babb8780200f5307fb50e9b8f6614446126469a82a9c",
    "input": "0xa9059cbb00000000000000000000000086e1e40f557cafbd792330fa69fa5e32e95f8f4200000000000000000000000000000000000000000000000000000000003b3440",
    "nonce": "0xf8361",
    "to": "0xdac17f958d2ee523a2206206994597c13d831ec6",
    "transactionIndex": "0x1",
    "value": "0x0",
    "type": "0x0",
    "v": "0x25",
    "r": "0xfcf2e8ee9efb2d334055e18096a56314e7931300b1b5b2a3c7f248cfdbc18628",
    "s": "0x4a6cb28a2558251849e6bb30b7135567ec37be922826c53902d474a3c31b3b66",
}

ERC20_ADDRESS = "0x86e1e40f557cafbd792330fa69fa5e32e95f8f42"
ERC20_AMOUNT = Decimal("3880000")

ERC20_FEE_SCALED = Decimal("0.003286244")
ERC20_TRANSACTION_UNKNOWN_DECODED = PlainTransaction(
    hash="0x6a85deb137f805512e34babb8780200f5307fb50e9b8f6614446126469a82a9c",
    inputs=[
        PlainInput(
            address="0x5041ed759dd4afc3a72b8192c143f72f4724081a",
            amount=Amount(
                value=ERC20_FEE_SCALED,
                currency_symbol=Currency.ETHER.symbol,
            ),
        ),
        PlainInput(
            address="0x5041ed759dd4afc3a72b8192c143f72f4724081a",
            amount=Amount(
                value=ERC20_AMOUNT,
                currency_symbol="0xdac17f958d2ee523a2206206994597c13d831ec6",
            ),
        ),
    ],
    outputs=[
        PlainOutput(
            address="0x86e1e40f557cafbd792330fa69fa5e32e95f8f42",
            amount=Amount(
                value=ERC20_AMOUNT,
                currency_symbol="0xdac17f958d2ee523a2206206994597c13d831ec6",
            ),
        ),
    ],
    fee=Amount(value=ERC20_FEE_SCALED, currency_symbol=Currency.ETHER.symbol),
)
