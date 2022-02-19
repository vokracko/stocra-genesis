import pytest
from aioresponses import aioresponses
from flexmock import flexmock

from genesis.blockchain.bitcoin.adapter import BitcoinNodeAdapter
from genesis.blockchain.bitcoin.tests.conftest import EXPECTED_HEADERS, NODE_URL
from genesis.blockchain.tests.utils import AwaitableValue, CalledRequests


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


@pytest.mark.parametrize("include_transactions, verbosity", [(False, 1), (True, 2)])
@pytest.mark.asyncio
async def test_get_block_by_hash(adapter: BitcoinNodeAdapter, include_transactions, verbosity: int) -> None:
    with aioresponses() as mocker:
        mocker.post(NODE_URL, payload=dict(result=42))
        block = await adapter.get_block_by_hash("hash", include_transactions=include_transactions)
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


@pytest.mark.parametrize("include_transactions", [True, False])
@pytest.mark.asyncio
async def test_get_block_by_height(adapter: BitcoinNodeAdapter, include_transactions: bool) -> None:
    flexmock(adapter).should_receive("get_block_hash").with_args(420).and_return(AwaitableValue("hash")).once()
    flexmock(adapter).should_receive("get_block_by_hash").with_args(
        "hash", include_transactions=include_transactions
    ).and_return(AwaitableValue(42)).once()
    block = await adapter.get_block_by_height(420, include_transactions=include_transactions)
    assert block == 42


@pytest.mark.asyncio
async def test_get_block_including_transactions(adapter: BitcoinNodeAdapter) -> None:
    flexmock(adapter).should_receive("get_block_hash").with_args(420).and_return(AwaitableValue("hash")).once()
    flexmock(adapter).should_receive("get_block_by_hash").with_args("hash", include_transactions=True).and_return(
        AwaitableValue(42)
    ).once()
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
