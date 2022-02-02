from typing import cast

import pytest
from aioresponses import aioresponses
from flexmock import flexmock

from genesis.blockchain.bitcoin.adapter import BitcoinNodeAdapter
from genesis.blockchain.exceptions import (
    AdapterException,
    BlockDoesNotExist,
    NodeNotReady,
)
from genesis.blockchain.factory import NodeAdapterFactory
from genesis.blockchain.tests.utils import AwaitableValue, CalledRequests
from genesis.constants import BlockchainName

EXPECTED_HEADERS = dict(Authorization="Basic cnBjdXNlcjpycGNwYXNzd29yZA==")

NODE_URL = "http://127.0.0.1:666/"


@pytest.fixture
def adapter() -> BitcoinNodeAdapter:
    client = NodeAdapterFactory.get_client(BlockchainName.BITCOIN.value, url=NODE_URL)
    return cast(BitcoinNodeAdapter, client)


@pytest.mark.parametrize("verbose", [True, False])
@pytest.mark.asyncio
async def test_get_transaction(adapter: BitcoinNodeAdapter, verbose: bool) -> None:
    with aioresponses() as mocker:
        mocker.post(NODE_URL, payload=dict(result=42))
        transaction = await adapter.get_transaction("hash", verbose=verbose)
        request_kwargs = CalledRequests(mocker.requests).get_request_kwargs()
        assert request_kwargs["headers"] == EXPECTED_HEADERS
        assert request_kwargs["json"] == dict(method="getrawtransaction", params=["hash", verbose])

    assert transaction == 42


@pytest.mark.parametrize("verbosity", [0, 1, 2])
@pytest.mark.asyncio
async def test_get_block_by_hash(adapter: BitcoinNodeAdapter, verbosity: int) -> None:
    with aioresponses() as mocker:
        mocker.post(NODE_URL, payload=dict(result=42))
        block = await adapter.get_block_by_hash("hash", verbosity=verbosity)
        request_kwargs = CalledRequests(mocker.requests).get_request_kwargs(0)
        assert request_kwargs["headers"] == EXPECTED_HEADERS
        assert request_kwargs["json"] == dict(method="getblock", params=["hash", verbosity])

    assert block == 42


@pytest.mark.asyncio
async def test_get_block_hash(adapter: BitcoinNodeAdapter) -> None:
    with aioresponses() as mocker:
        mocker.post(NODE_URL, payload=dict(result="hash"))
        block_hash = await adapter.get_block_hash(420)
        called_requests = CalledRequests(mocker.requests)
        request_kwargs = called_requests.get_request_kwargs(0)
        assert request_kwargs["headers"] == EXPECTED_HEADERS
        assert request_kwargs["json"] == dict(method="getblockhash", params=[420])

    assert block_hash == "hash"


@pytest.mark.parametrize("verbosity", [0, 1, 2])
@pytest.mark.asyncio
async def test_get_block_by_height(adapter: BitcoinNodeAdapter, verbosity: int) -> None:
    flexmock(adapter).should_receive("get_block_hash").with_args(420).and_return(AwaitableValue("hash")).once()
    flexmock(adapter).should_receive("get_block_by_hash").with_args("hash", verbosity).and_return(
        AwaitableValue(42)
    ).once()
    block = await adapter.get_block_by_height(420, verbosity=verbosity)
    assert block == 42


@pytest.mark.asyncio
async def test_get_block_including_transactions(adapter: BitcoinNodeAdapter) -> None:
    flexmock(adapter).should_receive("get_block_hash").with_args(420).and_return(AwaitableValue("hash")).once()
    flexmock(adapter).should_receive("get_block_by_hash").with_args("hash").and_return(AwaitableValue(42)).once()
    block = await adapter.get_block_including_transactions(420)
    assert block == 42


@pytest.mark.asyncio
async def test_decode_script(adapter: BitcoinNodeAdapter) -> None:
    with aioresponses() as mocker:
        mocker.post(NODE_URL, payload=dict(result="decoded script"))
        script = await adapter.decode_script(script="script")
        called_requests = CalledRequests(mocker.requests)
        request_kwargs = called_requests.get_request_kwargs(0)
        assert request_kwargs["headers"] == EXPECTED_HEADERS
        assert request_kwargs["json"] == dict(method="decodescript", params=["script"])

    assert script == "decoded script"


@pytest.mark.asyncio
async def test_block_by_hash_does_not_exist(adapter: BitcoinNodeAdapter) -> None:
    with aioresponses() as mocker:
        with pytest.raises(BlockDoesNotExist):
            mocker.post(NODE_URL, payload=dict(error=dict(code=-8, message="block does not exist")), status=500)
            await adapter.get_block_hash(420)


@pytest.mark.asyncio
async def test_block_by_hash_other_exception(adapter: BitcoinNodeAdapter) -> None:
    with aioresponses() as mocker:
        with pytest.raises(AdapterException):
            mocker.post(NODE_URL, payload=dict(error=dict(code=-9, message="Other exception")), status=500)
            await adapter.post(data=dict())


@pytest.mark.asyncio
async def test_node_not_ready(adapter: BitcoinNodeAdapter) -> None:
    with aioresponses() as mocker:
        with pytest.raises(NodeNotReady):
            mocker.post(NODE_URL, payload=dict(error=dict(code=-28, message="Not ready")), status=400)
            await adapter.post(data=dict())


@pytest.mark.asyncio
async def test_other_error(adapter: BitcoinNodeAdapter) -> None:
    with aioresponses() as mocker:
        with pytest.raises(AdapterException):
            mocker.post(NODE_URL, payload=dict(error=dict(code=0, message="Other exception")), status=400)
            await adapter.post(data=dict())
