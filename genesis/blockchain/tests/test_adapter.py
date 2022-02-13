import pytest

from genesis.blockchain.adapter import NodeAdapter
from genesis.blockchain.exceptions import Unavailable


class AdapterStub(NodeAdapter):
    ...


@pytest.mark.asyncio
async def test_get_block_including_transactions() -> None:
    adapter = AdapterStub(url="none")
    with pytest.raises(Unavailable):
        await adapter.get_block_latest(0)
