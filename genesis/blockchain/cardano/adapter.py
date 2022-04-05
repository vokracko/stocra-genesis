import asyncio
from typing import ClassVar, Dict, List

from asyncpg import connect
from asyncpg.connection import Connection
from asyncpg.prepared_stmt import PreparedStatement

from genesis.blockchain.adapter import NodeAdapter
from genesis.blockchain.cardano.queries import (
    GET_BLOCK_BY_HASH_QUERY,
    GET_BLOCK_BY_HEIGHT_QUERY,
    GET_BLOCK_COUNT_QUERY,
    GET_LIST_OF_TRANSACTION_QUERY,
    GET_TRANSACTION_QUERY,
)
from genesis.blockchain.exceptions import DoesNotExist
from genesis.blockchains import Blockchain


class CardanoNodeAdapter(NodeAdapter):
    BLOCKCHAIN: ClassVar[Blockchain] = Blockchain.CARDANO

    connection: Connection = None
    prepared_statements: Dict[str, PreparedStatement]

    async def init_async(self) -> None:
        self.connection = await connect(dsn=self.url)
        await self._prepare_statements()

    async def _prepare_statements(self) -> None:
        self.prepared_statements = {
            self.get_transaction.__name__: await self.connection.prepare(GET_TRANSACTION_QUERY),
            self.get_block_by_height.__name__: await self.connection.prepare(GET_BLOCK_BY_HEIGHT_QUERY),
            self.get_block_by_hash.__name__: await self.connection.prepare(GET_BLOCK_BY_HASH_QUERY),
            self.get_block_count.__name__: await self.connection.prepare(GET_BLOCK_COUNT_QUERY),
            self.get_list_of_transactions_in_block.__name__: await self.connection.prepare(
                GET_LIST_OF_TRANSACTION_QUERY
            ),
        }

    async def get_transaction(self, transaction_hash: str) -> dict:
        result = await self.query(self.get_transaction.__name__, transaction_hash)
        if not result:
            raise DoesNotExist(f"Transaction with hash {transaction_hash} does not exist")

        return dict(hash=transaction_hash, inputs_outputs=result)

    async def get_block_by_hash(self, block_hash: str) -> dict:
        block_data = await self.query(self.get_block_by_hash.__name__, block_hash)

        if not block_data:
            raise DoesNotExist(f"Block with hash {block_hash} does not exist")

        return block_data[0]

    async def get_block_by_height(self, height: int) -> dict:
        block_data = await self.query(self.get_block_by_height.__name__, height)
        if not block_data:
            raise DoesNotExist(f"Block with height {height} does not exist")

        return block_data[0]

    async def get_block_latest(self) -> dict:
        block_height = await self.get_block_count()
        return await self.get_block_by_height(block_height)

    async def get_block_count(self) -> int:
        return await self.query(self.get_block_by_height.__name__)

    async def get_list_of_transactions_in_block(self, block_id: int) -> List[dict]:
        return await self.query(self.get_list_of_transactions_in_block.__name__, block_id)

    async def query(self, prepared_statement_index: str, *args):
        records = await self.prepared_statements[prepared_statement_index].fetch(*args)
        return [dict(record) for record in records]

    def __del__(self) -> None:
        if self.connection:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self.connection.close())
