import pytest
from flexmock import flexmock

from genesis.blockchain.bitcoin.parser import BitcoinParser
from genesis.blockchain.tests.utils import AwaitableValue


@pytest.mark.asyncio
async def test_decode_block(parser: BitcoinParser) -> None:
    from genesis.blockchain.bitcoin.tests.fixtures.block import (
        BLOCK_DECODED,
        BLOCK_JSON,
    )

    decoded_transaction = await parser.decode_block(BLOCK_JSON)
    assert decoded_transaction == BLOCK_DECODED


@pytest.mark.asyncio
async def test_decode_coinbase_transaction(parser: BitcoinParser) -> None:
    from genesis.blockchain.bitcoin.tests.fixtures.coinbase_transaction import (
        TRANSACTION_DECODED,
        TRANSACTION_JSON,
    )

    decoded_transaction = await parser.decode_transaction(TRANSACTION_JSON)
    assert decoded_transaction == TRANSACTION_DECODED


@pytest.mark.asyncio
async def test_decode_pubkey_transaction(parser: BitcoinParser) -> None:
    from genesis.blockchain.bitcoin.tests.fixtures.pubkey_transaction import (
        DECODED_SCRIPT_PUB_KEY,
        TRANSACTION_DECODED,
        TRANSACTION_JSON,
    )

    flexmock(parser.node_adapter).should_receive("decode_script").with_args(
        TRANSACTION_JSON["vout"][0]["scriptPubKey"]["hex"]
    ).and_return(AwaitableValue(DECODED_SCRIPT_PUB_KEY))
    decoded_transaction = await parser.decode_transaction(TRANSACTION_JSON)
    assert decoded_transaction == TRANSACTION_DECODED


@pytest.mark.parametrize(
    "script_pub_key, decoded, address",
    [
        (
            dict(
                addresses=[
                    "LesZyFw6HL666MYLUG4dexGaV356rD3a64",
                    "LgLMDEwNXXK5qSE7k5yYHQxHB6yFYpdH8z",
                    "LejZnZ77gSUQoABn78kAaCRqb6wrhkkA2P",
                ],
                asm="1 03681000e63398896c7579287b79a2f041cfee580ec0143fb2179f7d134fb0509c 026fa03bc998e7f8f61abb0a243529770191f0f15e5e249893fc9cc3745c2f5317 0277f7baabde15782807bf9a211530240dfd37b176f16c8de6af255bfac3534974 3 OP_CHECKMULTISIG",
                hex="512103681000e63398896c7579287b79a2f041cfee580ec0143fb2179f7d134fb0509c21026fa03bc998e7f8f61abb0a243529770191f0f15e5e249893fc9cc3745c2f5317210277f7baabde15782807bf9a211530240dfd37b176f16c8de6af255bfac353497453ae",
                reqSigs=1,
                type="multisig",
            ),
            {
                "addresses": [
                    "LesZyFw6HL666MYLUG4dexGaV356rD3a64",
                    "LgLMDEwNXXK5qSE7k5yYHQxHB6yFYpdH8z",
                    "LejZnZ77gSUQoABn78kAaCRqb6wrhkkA2P",
                ],
                "asm": "1 03681000e63398896c7579287b79a2f041cfee580ec0143fb2179f7d134fb0509c 026fa03bc998e7f8f61abb0a243529770191f0f15e5e249893fc9cc3745c2f5317 0277f7baabde15782807bf9a211530240dfd37b176f16c8de6af255bfac3534974 3 OP_CHECKMULTISIG",
                "p2sh": "MLETEZgQKQn5t2f6cAzDtYMYTm9tshQJ9W",
                "reqSigs": 1,
                "segwit": {
                    "addresses": ["ltc1q0f6a3yqs93fqnm3j2qwzc2u33gsmfchwaw8mhqg5u8wxlq8xuw2sf23r8m"],
                    "asm": "0 7a75d890102c5209ee32501c2c2b918a21b4e2eeeb8fbb8114e1dc6f80e6e395",
                    "hex": "00207a75d890102c5209ee32501c2c2b918a21b4e2eeeb8fbb8114e1dc6f80e6e395",
                    "p2sh-segwit": "MLixXdExDjaG34wUwX6KzyaYnb1PkCoyXE",
                    "reqSigs": 1,
                    "type": "witness_v0_scripthash",
                },
                "type": "multisig",
            },
            "ltc1q0f6a3yqs93fqnm3j2qwzc2u33gsmfchwaw8mhqg5u8wxlq8xuw2sf23r8m",
        ),
    ],
)
@pytest.mark.asyncio
async def test_decode_address_from_script_pub_key_segwit(
    parser: BitcoinParser, script_pub_key: dict, decoded: dict, address: str
) -> None:
    flexmock(parser.node_adapter).should_receive("decode_script").with_args(script_pub_key["hex"]).and_return(
        AwaitableValue(decoded)
    )
    parsed_address = await parser._decode_address_from_script_pub_key(script_pub_key)
    assert parsed_address == address
