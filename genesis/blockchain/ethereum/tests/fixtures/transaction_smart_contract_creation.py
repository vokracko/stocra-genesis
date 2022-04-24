from decimal import Decimal

from genesis.currencies import Currency
from genesis.models import Amount, PlainInput, PlainTransaction

TRANSACTION_SMART_CONTRACT_CREATION_JSON = {
    "blockHash": "0xce97e51b368054e4cb404cc766af274e59a4639e621a2ed9f8b0f8d6ba7f47bc",
    "blockNumber": "0xded81c",
    "from": "0x806f5d470ee7dd7b7a8ceb092d3fa7ef00a70576",
    "gas": "0x25020a",
    "gasPrice": "0x817e7ac31",
    "maxFeePerGas": "0x837a4d14d",
    "maxPriorityFeePerGas": "0x59682f00",
    "hash": "0x77e7d3a927ee4127f7653e8d19edaec998d32a7ec49a14e06cf249e5d03c976e",
    "input": "0x608060405260405162002e5738038062002e578....",
    "nonce": "0x8",
    "to": None,
    "transactionIndex": "0x39",
    "value": "0x0",
    "type": "0x2",
    "accessList": [],
    "chainId": "0x1",
    "v": "0x0",
    "r": "0x7ba0ae7e8e2fc02aff075a5cdfe878d46506127e1d368aa9825f7281caa8e2ed",
    "s": "0x7aa3896cf8f06dace7bcbd1d10e5d6ebdf6485c814b390d69114abb4af758c5c",
}

TRANSACTION_SMART_CONTRACT_CREATION_RECEIPT_JSON = {
    "blockHash": "0xce97e51b368054e4cb404cc766af274e59a4639e621a2ed9f8b0f8d6ba7f47bc",
    "blockNumber": "0xded81c",
    "contractAddress": "0x6f10c2b4d87e553ef29910110549db48a1806f27",
    "cumulativeGasUsed": "0x6e973a",
    "effectiveGasPrice": "0x817e7ac31",
    "from": "0x806f5d470ee7dd7b7a8ceb092d3fa7ef00a70576",
    "gasUsed": "0x25020a",
    "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000040000000000000000000000000008000000000000000000040000000000000000000000000080020000000000000000000800000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000002000000000000010000000000000000000000000000000000000060000000000000000000000000000000000002000000000000000000000000000010",
    "status": "0x1",
    "to": None,
    "transactionHash": "0x77e7d3a927ee4127f7653e8d19edaec998d32a7ec49a14e06cf249e5d03c976e",
    "transactionIndex": "0x39",
    "type": "0x2",
}


TRANSACTION_SMART_CONTRACT_CREATION_DECODED = PlainTransaction(
    hash="0x77e7d3a927ee4127f7653e8d19edaec998d32a7ec49a14e06cf249e5d03c976e",
    inputs=[
        PlainInput(
            address="0x806f5d470ee7dd7b7a8ceb092d3fa7ef00a70576",
            amount=Amount(
                value=Decimal("0.084307238612245482"),
                currency_symbol=Currency.ETHER.symbol,
            ),
        ),
    ],
    outputs=[],
    fee=Amount(
        value=Decimal("0.084307238612245482"),
        currency_symbol=Currency.ETHER.symbol,
    ),
)
