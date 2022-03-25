from decimal import Decimal

TRANSACTION_RECEIPT_JSON = {
    "blockHash": "0x6bd7e3f6176b483b55e7d71ba96da60f9a93435b564315ff1dbd1c0a14f2d97d",
    "blockNumber": "0xbe0ac8",
    "contractAddress": None,
    "cumulativeGasUsed": "0xe2333c",
    "effectiveGasPrice": "0x1176592e00",
    "from": "0x18916e1a2933cb349145a280473a5de8eb6630cb",
    "gasUsed": "0x5208",
    "logs": [],
    "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "status": "0x1",
    "to": "0xd67f401f48d9bd30e8860ace01bff1bcd4675f1e",
    "transactionHash": "0xffac6416d8e24f9d8e308a7acf2ff58a576d14967795926ddd37376031d8f5ee",
    "transactionIndex": "0xe4",
    "type": "0x0",
}

TRANSACTION_RECEIPT_GAS_USED = Decimal("21_000")
TRANSACTION_RECEIPT_GAS_PRICE = Decimal("75000000000")  # TODO FIXME this might need scaling