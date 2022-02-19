from genesis.models import PlainBlock

BLOCK_JSON = {
    "difficulty": "0x42be722b6",
    "extraData": "0x476574682f4c5649562f76312e302e302f6c696e75782f676f312e342e32",
    "gasLimit": "0x1388",
    "gasUsed": "0x0",
    "hash": "0xdfe2e70d6c116a541101cecbb256d7402d62125f6ddc9b607d49edc989825c64",
    "logsBloom": "",
    "miner": "0xbb7b8287f3f0a933474a79eae42cbca977791171",
    "mixHash": "0x5bb43c0772e58084b221c8e0c859a45950c103c712c5b8f11d9566ee078a4501",
    "nonce": "0x37129c7f29a9364b",
    "number": "0x64",
    "parentHash": "0xdb10afd3efa45327eb284c83cc925bd9bd7966aea53067c1eebe0724d124ec1e",
    "receiptsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
    "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
    "size": "0x21e",
    "stateRoot": "0x90c25f6d7fddeb31a6cc5668a6bba77adbadec705eb7aa5a51265c2d1e3bb7ac",
    "timestamp": "0x55ba43eb",
    "totalDifficulty": "0x19b5afdc486",
    "transactions": [],
    "transactionsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
    "uncles": [],
}

BLOCK_DECODED = PlainBlock(
    height=100,
    hash="0xdfe2e70d6c116a541101cecbb256d7402d62125f6ddc9b607d49edc989825c64",
    timestamp=1438270443,
)
