from typing import cast

import pytest
from aioresponses import aioresponses
from flexmock import flexmock

from genesis.blockchain.ethereum.adapter import EthereumNodeAdapter
from genesis.blockchain.exceptions import BlockDoesNotExist
from genesis.blockchain.factory import NodeAdapterFactory
from genesis.blockchain.tests.utils import AwaitableValue, CalledRequests
from genesis.constants import BlockchainName

NODE_URL = "http://127.0.0.1:666/"


@pytest.fixture
def adapter() -> EthereumNodeAdapter:
    client = NodeAdapterFactory.get_client(BlockchainName.ETHEREUM.value, url=NODE_URL)
    return cast(EthereumNodeAdapter, client)


@pytest.mark.asyncio
async def test_get_transaction(adapter: EthereumNodeAdapter) -> None:
    with aioresponses() as mocker:
        mocker.post(NODE_URL, payload=dict(result=42))
        transaction = await adapter.get_transaction("hash")
        request_kwargs = CalledRequests(mocker.requests).get_request_kwargs()
        assert request_kwargs["json"] == dict(
            jsonrpc="2.0",
            method="eth_getTransactionByHash",
            params=["hash"],
            id=1,
        )

    assert transaction == 42


@pytest.mark.parametrize("include_transactions", [True, False])
@pytest.mark.asyncio
async def test_get_block_by_hash(adapter: EthereumNodeAdapter, include_transactions: bool) -> None:
    with aioresponses() as mocker:
        mocker.post(NODE_URL, payload=dict(result=42))
        block = await adapter.get_block_by_hash("hash", include_transactions=include_transactions)
        request_kwargs = CalledRequests(mocker.requests).get_request_kwargs(0)
        assert request_kwargs["json"] == dict(
            jsonrpc="2.0",
            method="eth_getBlockByHash",
            params=["hash", include_transactions],
            id=1,
        )

    assert block == 42


@pytest.mark.asyncio
async def test_get_block_hash(adapter: EthereumNodeAdapter) -> None:
    with pytest.raises(NotImplementedError):
        await adapter.get_block_hash(420)


@pytest.mark.parametrize("include_transactions", [True, False])
@pytest.mark.asyncio
async def test_get_block_by_height(adapter: EthereumNodeAdapter, include_transactions: bool) -> None:
    with aioresponses() as mocker:
        mocker.post(NODE_URL, payload=dict(result=42))
        block = await adapter.get_block_by_height(420, include_transactions=include_transactions)
        request_kwargs = CalledRequests(mocker.requests).get_request_kwargs(0)
        assert request_kwargs["json"] == dict(
            jsonrpc="2.0",
            method="eth_getBlockByNumber",
            params=["0x1a4", include_transactions],
            id=1,
        )

    assert block == 42


@pytest.mark.asyncio
async def test_get_next_block_with_transactions(adapter: EthereumNodeAdapter) -> None:
    flexmock(adapter).should_receive("get_block_by_height").with_args(height=420, include_transactions=True).and_return(
        AwaitableValue(42)
    ).once()
    block = await adapter.get_next_block_with_transactions(420)
    assert block == 42


@pytest.mark.asyncio
async def test_block_by_hash_does_not_exist(adapter: EthereumNodeAdapter) -> None:
    with aioresponses() as mocker:
        with pytest.raises(BlockDoesNotExist):
            mocker.post(NODE_URL, payload=dict(result=None))
            await adapter.get_block_by_hash("abcd")


@pytest.mark.asyncio
async def test_block_by_number_does_not_exist(adapter: EthereumNodeAdapter) -> None:
    with aioresponses() as mocker:
        with pytest.raises(BlockDoesNotExist):
            mocker.post(NODE_URL, payload=dict(result=None))
            await adapter.get_block_by_height(420)
