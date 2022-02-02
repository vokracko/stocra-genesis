from typing import Optional

import pytest

from genesis.blockchain.adapter import NodeAdapter
from genesis.blockchain.exceptions import BlockDoesNotExist


class AdapterStub(NodeAdapter):
    async def _get_block_including_transactions(self, height: int) -> Optional[dict]:
        raise BlockDoesNotExist


@pytest.mark.asyncio
async def test_get_block_including_transactions() -> None:
    adapter = AdapterStub(url="none")
    result = await adapter.get_block_including_transactions(0)
    assert result is None
