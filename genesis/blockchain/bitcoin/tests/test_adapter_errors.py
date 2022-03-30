import pytest
from aioresponses import aioresponses

from genesis.blockchain.bitcoin.adapter import BitcoinNodeAdapter
from genesis.blockchain.bitcoin.tests.conftest import NODE_URL
from genesis.blockchain.exceptions import (
    DoesNotExist,
    NodeNotReady,
    TooManyRequests,
    UnknownNodeException,
)


@pytest.mark.asyncio
async def test_get_block_by_hash_invalid_hash_number(adapter: BitcoinNodeAdapter) -> None:
    with aioresponses() as mocker:
        with pytest.raises(DoesNotExist):
            mocker.post(
                NODE_URL,
                payload=dict(error=dict(code=-1, message="JSON value is not a string as expected")),
                status=500,
            )
            await adapter.get_block_by_hash(1_000_000)


@pytest.mark.asyncio
async def test_get_block_by_hash_invalid_hash_string_nonsence(adapter: BitcoinNodeAdapter) -> None:
    with aioresponses() as mocker:
        with pytest.raises(DoesNotExist):
            mocker.post(
                NODE_URL,
                payload=dict(
                    error=dict(code=-8, message="blockhash must be of length 64 (not 17, for 'invalidhashstring')"),
                ),
                status=500,
            )
            await adapter.get_block_by_hash("invalidhashstring")


@pytest.mark.asyncio
async def test_get_block_by_hash_invalid_hash_string_not_bitcoin_block_hash(adapter: BitcoinNodeAdapter) -> None:
    with aioresponses() as mocker:
        with pytest.raises(DoesNotExist):
            mocker.post(NODE_URL, payload=dict(error=dict(code=-5, message="Block not found")), status=500)
            await adapter.get_block_by_hash("000000000000000003aba32e1cd5548f01aef6d4d5e27df7f6ced6d85fca52af")


@pytest.mark.asyncio
async def test_block_by_hash_other_exception(adapter: BitcoinNodeAdapter) -> None:
    with aioresponses() as mocker:
        with pytest.raises(UnknownNodeException):
            mocker.post(NODE_URL, payload=dict(error=dict(code=-9, message="Other exception")), status=500)
            await adapter.post(data=dict())


@pytest.mark.asyncio
async def test_node_not_ready(adapter: BitcoinNodeAdapter) -> None:
    with aioresponses() as mocker:
        with pytest.raises(NodeNotReady):
            mocker.post(NODE_URL, payload=dict(error=dict(code=-28, message="Not ready")), status=500)
            await adapter.post(data=dict())


@pytest.mark.asyncio
async def test_too_many_request(adapter: BitcoinNodeAdapter) -> None:
    with aioresponses() as mocker:
        with pytest.raises(TooManyRequests):
            mocker.post(NODE_URL, status=503)
            await adapter.post(data=dict())
