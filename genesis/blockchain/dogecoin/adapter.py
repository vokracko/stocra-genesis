from typing import ClassVar

from genesis.blockchain.litecoin.adapter import LitecoinNodeAdapter
from genesis.blockchains import Blockchain


class DogecoinNodeAdapter(LitecoinNodeAdapter):
    BLOCKCHAIN: ClassVar[Blockchain] = Blockchain.DOGECOIN

    async def get_block_by_hash(self, block_hash: str, *, include_transactions: bool) -> dict:
        data = dict(
            method="getblock",
            params=[block_hash, True],
        )
        return await self.post(data)
