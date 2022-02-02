import pytest

from genesis.blockchain.bitcoin.adapter import BitcoinNodeAdapter
from genesis.blockchain.bitcoin.parser import BitcoinParser


@pytest.fixture
def adapter() -> BitcoinNodeAdapter:
    return BitcoinNodeAdapter(url="")


@pytest.fixture
def parser(adapter: BitcoinNodeAdapter) -> BitcoinParser:
    return BitcoinParser(adapter)


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
        TRANSACTION_DECODED,
        TRANSACTION_JSON,
    )

    decoded_transaction = await parser.decode_transaction(TRANSACTION_JSON)
    assert decoded_transaction == TRANSACTION_DECODED


@pytest.mark.parametrize(
    "script_pub_key, address",
    [
        (
            dict(
                asm=(
                    "04c7b1f1d0537b9d800f4413e0222370f7fb8c3844fc98dafe9bdbfea27650ef78d3cb89ab5022493"
                    "4c6473e8e925cfdb42c4c6f32145bf4ea87ecda17a0e24e4f OP_CHECKSIG"
                ),
                hex=(
                    "4104c7b1f1d0537b9d800f4413e0222370f7fb8c3844fc98dafe9bdbfea27650ef78d3cb89"
                    "ab50224934c6473e8e925cfdb42c4c6f32145bf4ea87ecda17a0e24e4fac"
                ),
                type="pubkey",
            ),
            "1KnUs1jKkSbcNwBt7gA4PaRKhiabuVXsaT",
        )
    ],
)
@pytest.mark.asyncio
async def test_decode_address_from_script_pub_key(parser: BitcoinParser, script_pub_key: dict, address: str) -> None:
    parsed_address = await parser._decode_address_from_script_pub_key(script_pub_key)
    assert parsed_address == "1KnUs1jKkSbcNwBt7gA4PaRKhiabuVXsaT"
