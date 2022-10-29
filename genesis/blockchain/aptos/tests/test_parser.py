import pytest

from genesis.blockchain.aptos.parser import AptosParser


@pytest.mark.asyncio
async def test_decode_native_transfer(parser: AptosParser) -> None:
    from genesis.blockchain.aptos.tests.fixtures.native_transfer import (
        TRANSACTION_DECODED,
        TRANSACTION_JSON,
    )

    decoded_transaction = await parser.decode_transaction(TRANSACTION_JSON)
    assert decoded_transaction == TRANSACTION_DECODED


@pytest.mark.asyncio
async def test_decode_native_transfer_failed(parser: AptosParser) -> None:
    from genesis.blockchain.aptos.tests.fixtures.native_transfer_failed import (
        TRANSACTION_DECODED,
        TRANSACTION_JSON,
    )

    decoded_transaction = await parser.decode_transaction(TRANSACTION_JSON)
    assert decoded_transaction == TRANSACTION_DECODED


@pytest.mark.asyncio
async def test_decode_non_user_transaction(parser: AptosParser) -> None:
    from genesis.blockchain.aptos.tests.fixtures.block_meta_tx import (
        TRANSACTION_DECODED,
        TRANSACTION_JSON,
    )

    decoded_transaction = await parser.decode_transaction(TRANSACTION_JSON)
    assert decoded_transaction == TRANSACTION_DECODED


@pytest.mark.asyncio
async def test_decode_coin_transfer(parser: AptosParser) -> None:
    from genesis.blockchain.aptos.tests.fixtures.aptos_coin_transfer import (
        TRANSACTION_DECODED,
        TRANSACTION_JSON,
    )

    decoded_transaction = await parser.decode_transaction(TRANSACTION_JSON)
    assert decoded_transaction == TRANSACTION_DECODED
