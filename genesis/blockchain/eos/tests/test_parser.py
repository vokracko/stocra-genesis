import pytest

from genesis.blockchain.eos.parser import EosParser


@pytest.mark.asyncio
async def test_decode_eosio_token_transfer(parser: EosParser) -> None:
    from genesis.blockchain.eos.tests.fixtures.eosio_token_transfer import (
        TRANSACTION_DECODED,
        TRANSACTION_JSON,
    )

    decoded_transaction = await parser.decode_transaction(TRANSACTION_JSON)
    assert decoded_transaction == TRANSACTION_DECODED
