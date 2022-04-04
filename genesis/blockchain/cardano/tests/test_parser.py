import pytest
from flexmock import flexmock

from genesis.blockchain.cardano.parser import CardanoParser
from genesis.blockchain.cardano.tests.fixtures.block import BLOCK_DECODED, BLOCK_JSON
from genesis.blockchain.cardano.tests.fixtures.transaction import (
    TRANSACTION_DECODED,
    TRANSACTION_JSON,
)
from genesis.blockchain.tests.utils import AwaitableValue


@pytest.mark.asyncio
async def test_decode_block(parser: CardanoParser) -> None:
    flexmock(parser.node_adapter).should_receive("get_list_of_transactions_in_block").with_args(
        BLOCK_JSON["id"]
    ).and_return(AwaitableValue([dict(hash="dbd87b3876da9847c01b7f229a4126ea113cdd17494ba6b86e714b4ca1864fcd")])).once()
    decoded_transaction = await parser.decode_block(BLOCK_JSON)
    assert decoded_transaction == BLOCK_DECODED


@pytest.mark.asyncio
async def test_decode_transaction(parser: CardanoParser) -> None:
    decoded_transaction = await parser.decode_transaction(TRANSACTION_JSON)
    assert decoded_transaction == TRANSACTION_DECODED
