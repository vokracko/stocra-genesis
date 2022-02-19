import pytest

from genesis.blockchain.adapter import NodeAdapter


class AdapterStub(NodeAdapter):
    ...


@pytest.mark.asyncio
async def test_get_block_including_transactions() -> None:
    pass
