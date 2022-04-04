import asyncio
from typing import ClassVar, Dict, Iterable, List, Union, cast

import asyncpg
from aiohttp import ClientResponse

from genesis.blockchain.adapter import NodeAdapter
from genesis.blockchain.exceptions import (
    DoesNotExist,
    NodeNotReady,
    TooManyRequests,
    UnknownNodeException,
)
from genesis.blockchains import Blockchain
from genesis.encoders import fast_deserialize_response


class CardanoNodeAdapter(NodeAdapter):
    BLOCKCHAIN: ClassVar[Blockchain] = Blockchain.CARDANO
    connection: asyncpg.connection.Connection

    async def init_async(self):
        self.connection = await asyncpg.connect(dsn=self.url)

    async def get_transaction(self, transaction_hash: str, *, verbose: bool = True) -> dict:
        # TODO statement could be prepared and stored in db upon start up
        query = """
            SELECT 
                tx_out.address AS address,
                tx_out.value AS amount,
                NULL AS transaction_pointer_hash,
                NULL AS transaction_pointer_index
            FROM tx_out
            LEFT JOIN tx ON tx_out.tx_id = tx.id
            WHERE tx.hash = decode($1, 'hex')
            UNION
            SELECT 
                tx_out.address AS address,
                tx_out.value AS amount,
                encode(tx.hash, 'hex') AS transaction_pointer_hash,
                tx_in.tx_out_index AS transaction_pointer_index
            FROM tx_out
            LEFT JOIN tx_in ON tx_out.id = tx_in.tx_out_id
            LEFT JOIN tx ON tx_out.tx_id = tx.id
            WHERE tx_in.tx_in_id = (SELECT tx.id FROM tx WHERE tx.hash = decode($1, 'hex'))
        """
        result = await self.query(query, transaction_hash)
        if not result:
            raise DoesNotExist(f"Transaction with hash {transaction_hash} does not exist")

        return dict(hash=transaction_hash, inputs_outputs=result)

    async def get_block_by_hash(self, block_hash: str) -> dict:
        query = """
            SELECT 
                block.id AS id,
                encode(block.hash, 'hex') AS hash,  
                block.block_no AS height, 
                extract(epoch from block.time) * 1000 AS timestamp_ms
            FROM block 
            WHERE block.hash = decode($1, 'hex')
        """
        block_data = await self.query(query, block_hash)

        if not block_data:
            raise DoesNotExist(f"Block with hash {block_hash} does not exist")

        return block_data[0]

    async def get_block_by_height(self, height: int) -> dict:
        query = """
            SELECT 
                block.id AS id,
                encode(block.hash, 'hex') AS hash, 
                block.block_no AS height, 
                extract(epoch from block.time) * 1000 AS timestamp_ms
            FROM block 
            WHERE block.block_no = $1
        """
        block_data = await self.query(query, height)
        if not block_data:
            raise DoesNotExist(f"Block with height {height} does not exist")

        return block_data[0]

    async def get_block_latest(self) -> dict:
        block_height = await self.get_block_count()
        return await self.get_block_by_height(block_height)

    async def get_block_count(self) -> int:
        QUERY = """
            SELECT 
                block.block_no AS block_count
            FROM block 
            WHERE block.block_no IS NOT NULL
            ORDER BY block.block_no DESC
            LIMIT 1
        """
        return await self.query(QUERY)

    async def get_list_of_transactions_in_block(self, block_id: int) -> List[dict]:
        sql = """
            SELECT 
                encode(tx.hash, 'hex') AS hash 
            FROM tx 
            WHERE tx.block_id = $1
        """
        return await self.query(sql, block_id)

    @property
    def headers(self) -> dict:
        raise NotImplementedError

    async def query(self, sql, *args):
        prepared_statement = await self.connection.prepare(sql)
        records = await prepared_statement.fetch(*args)
        return [dict(record) for record in records]

    def __del__(self):
        if self.connection:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self.connection.close())
