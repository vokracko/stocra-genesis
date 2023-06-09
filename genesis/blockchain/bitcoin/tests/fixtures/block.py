from genesis.blockchain.bitcoin.tests.fixtures.coinbase_transaction import (
    TRANSACTION_HASH,
)
from genesis.models import PlainBlock

BLOCK_JSON = {
    "hash": "000000002c05cc2e78923c34df87fd108b22221ac6076c18f3ade378a4d915e9",
    "confirmations": 710697,
    "strippedsize": 215,
    "size": 215,
    "weight": 860,
    "height": 10,
    "version": 1,
    "versionHex": "00000001",
    "merkleroot": "d3ad39fa52a89997ac7381c95eeffeaf40b66af7a57e9eba144be0a175a12b11",
    "tx": [TRANSACTION_HASH],
    "time": 1231473952,
    "mediantime": 1231471428,
    "nonce": 1709518110,
    "bits": "1d00ffff",
    "difficulty": 1,
    "chainwork": "0000000000000000000000000000000000000000000000000000000b000b000b",
    "nTx": 1,
    "previousblockhash": "000000008d9dc510f23c2657fc4f67bea30078cc05a90eb89e84cc475c080805",
    "nextblockhash": "0000000097be56d606cdd9c54b04d4747e957d3608abe69198c661f2add73073",
}

BLOCK_DECODED = PlainBlock(
    height=10,
    hash="000000002c05cc2e78923c34df87fd108b22221ac6076c18f3ade378a4d915e9",
    timestamp_ms=1231473952000,
    transactions=[TRANSACTION_HASH],
)
