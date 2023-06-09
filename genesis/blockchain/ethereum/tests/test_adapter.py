import pytest
from aioresponses import aioresponses

from genesis.blockchain.ethereum.adapter import EthereumNodeAdapter
from genesis.blockchain.exceptions import DoesNotExist
from genesis.blockchain.tests.utils import CalledRequests

NODE_URL = "http://127.0.0.1:666/"


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


@pytest.mark.asyncio
async def test_get_block_by_hash(adapter: EthereumNodeAdapter) -> None:
    with aioresponses() as mocker:
        mocker.post(NODE_URL, payload=dict(result=42))
        block = await adapter.get_block_by_hash("hash")
        request_kwargs = CalledRequests(mocker.requests).get_request_kwargs(0)
        assert request_kwargs["json"] == dict(
            jsonrpc="2.0",
            method="eth_getBlockByHash",
            params=["hash", False],
            id=1,
        )

    assert block == 42


@pytest.mark.asyncio
async def test_get_block_hash(adapter: EthereumNodeAdapter) -> None:
    with pytest.raises(NotImplementedError):
        await adapter.get_block_hash(420)


@pytest.mark.asyncio
async def test_get_block_by_height(adapter: EthereumNodeAdapter) -> None:
    with aioresponses() as mocker:
        mocker.post(NODE_URL, payload=dict(result=42))
        block = await adapter.get_block_by_height(420)
        request_kwargs = CalledRequests(mocker.requests).get_request_kwargs(0)
        assert request_kwargs["json"] == dict(
            jsonrpc="2.0",
            method="eth_getBlockByNumber",
            params=["0x1a4", False],
            id=1,
        )

    assert block == 42


@pytest.mark.asyncio
async def test_block_by_hash_does_not_exist(adapter: EthereumNodeAdapter) -> None:
    with aioresponses() as mocker:
        with pytest.raises(DoesNotExist):
            mocker.post(NODE_URL, payload=dict(result=None))
            await adapter.get_block_by_hash("abcd")


@pytest.mark.asyncio
async def test_block_by_number_does_not_exist(adapter: EthereumNodeAdapter) -> None:
    with aioresponses() as mocker:
        with pytest.raises(DoesNotExist):
            mocker.post(NODE_URL, payload=dict(result=None))
            await adapter.get_block_by_height(420)
