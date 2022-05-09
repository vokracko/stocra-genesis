import asyncio
from typing import ClassVar, List

from asyncpg import Pool, PostgresError, create_pool
from asyncpg.exceptions import PostgresConnectionError

from genesis.blockchain.adapter import NodeAdapter
from genesis.blockchain.cardano.queries import (
    GET_BLOCK_BY_HASH_QUERY,
    GET_BLOCK_BY_HEIGHT_QUERY,
    GET_BLOCK_COUNT_QUERY,
    GET_LIST_OF_TRANSACTION_QUERY,
    GET_TRANSACTION_QUERY,
)
from genesis.blockchain.exceptions import DoesNotExist, Unavailable
from genesis.blockchains import Blockchain


class CardanoNodeAdapter(NodeAdapter):
    BLOCKCHAIN: ClassVar[Blockchain] = Blockchain.CARDANO

    connection_pool: Pool = None

    async def init_async(self) -> None:
        try:
            self.connection_pool = await create_pool(dsn=self.url)
        except (OSError, PostgresError) as exc:
            raise Unavailable(f"Failed to connect to {self.url}") from exc

    async def get_transaction(self, transaction_hash: str) -> dict:
        result = await self.query(GET_TRANSACTION_QUERY, transaction_hash)
        if not result:
            raise DoesNotExist(f"Transaction with hash {transaction_hash} does not exist")

        return dict(hash=transaction_hash, inputs_outputs=result)

    async def get_block_by_hash(self, block_hash: str) -> dict:
        block_data = await self.query(GET_BLOCK_BY_HASH_QUERY, block_hash)

        if not block_data:
            raise DoesNotExist(f"Block with hash {block_hash} does not exist")

        return block_data[0]

    async def get_block_by_height(self, height: int) -> dict:
        block_data = await self.query(GET_BLOCK_BY_HEIGHT_QUERY, height)
        if not block_data:
            raise DoesNotExist(f"Block with height {height} does not exist")

        return block_data[0]

    async def get_block_latest(self) -> dict:
        block_height = await self.get_block_count()
        return await self.get_block_by_height(block_height)

    async def get_block_count(self) -> int:
        try:
            async with self.connection_pool.acquire() as connection:
                return await connection.fetchval(GET_BLOCK_COUNT_QUERY)
        except PostgresConnectionError as exc:
            raise Unavailable(str(exc)) from exc

    async def get_list_of_transactions_in_block(self, block_id: int) -> List[dict]:
        return await self.query(GET_LIST_OF_TRANSACTION_QUERY, block_id)

    async def query(self, query: str, *args):
        try:
            async with self.connection_pool.acquire() as connection:
                records = await connection.fetch(query, *args)
        except PostgresConnectionError as exc:
            raise Unavailable(str(exc)) from exc
        return [dict(record) for record in records]

    def __del__(self) -> None:
        if self.connection_pool:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self.connection_pool.close())
