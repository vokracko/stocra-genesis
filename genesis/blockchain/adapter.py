from typing import ClassVar

from genesis.blockchains import Blockchain


class NodeAdapter:
    BLOCKCHAIN: ClassVar[Blockchain]

    url: str
    token: str

    def __init__(self, url: str, token: str) -> None:
        self.url = url
        self.token = token

    async def init_async(self):
        pass

    async def get_transaction(self, transaction_hash: str) -> dict:
        raise NotImplementedError

    async def get_block_by_hash(self, block_hash: str) -> dict:
        raise NotImplementedError

    async def get_block_by_height(self, height: int) -> dict:
        raise NotImplementedError

    async def get_block_latest(self) -> dict:
        raise NotImplementedError

    async def get_block_count(self) -> int:
        raise NotImplementedError
