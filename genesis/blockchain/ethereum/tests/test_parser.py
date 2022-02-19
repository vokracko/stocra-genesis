import pytest

from genesis.blockchain.ethereum.adapter import EthereumNodeAdapter
from genesis.blockchain.ethereum.parser import EthereumParser


@pytest.fixture
def adapter() -> EthereumNodeAdapter:
    return EthereumNodeAdapter(url="")


@pytest.fixture
def parser(adapter: EthereumNodeAdapter) -> EthereumParser:
    return EthereumParser(adapter)


@pytest.mark.asyncio
async def test_decode_block(parser: EthereumParser) -> None:
    from genesis.blockchain.ethereum.tests.fixtures.block import (
        BLOCK_DECODED,
        BLOCK_JSON,
    )

    decoded_transaction = await parser.decode_block(BLOCK_JSON)
    assert decoded_transaction == BLOCK_DECODED


@pytest.mark.asyncio
async def test_decode_coinbase_transaction(parser: EthereumParser) -> None:
    raise NotImplementedError


#     from nodes.bitcoin.tests.fixtures.coinbase_transaction import (
#         TRANSACTION_DECODED,
#         TRANSACTION_JSON,
#     )
#
#     decoded_transaction = await parser.decode_transaction(TRANSACTION_JSON)
#     assert decoded_transaction == TRANSACTION_DECODED


@pytest.mark.asyncio
async def test_decode_transaction(parser: EthereumParser) -> None:
    from genesis.blockchain.ethereum.tests.fixtures.transaction import (
        TRANSACTION_DECODED,
        TRANSACTION_JSON,
    )

    decoded_transaction = await parser.decode_transaction(TRANSACTION_JSON, decode_inputs=False)
    assert decoded_transaction == TRANSACTION_DECODED
