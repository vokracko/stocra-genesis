import asyncio
from typing import ClassVar, Dict, Optional

from aiohttp import ClientError, ClientResponse, ClientSession
from async_lru import alru_cache
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection

from genesis.blockchain.adapter import NodeAdapter
from genesis.blockchain.exceptions import DoesNotExist, Unavailable
from genesis.blockchains import Blockchain
from genesis.encoders import fast_deserialize_response, fast_serializer_to_str


class EosNodeAdapter(NodeAdapter):
    BLOCKCHAIN: ClassVar[Blockchain] = Blockchain.EOS
    session: ClientSession
    mongo_client: AsyncIOMotorClient
    mongo_collection: AsyncIOMotorCollection

    async def init_async(self) -> None:
        self.session = ClientSession(json_serialize=fast_serializer_to_str)
        self.mongo_client = AsyncIOMotorClient(f"{self.BLOCKCHAIN.blockchain_name}-mongo-1")
        mongo_database = self.mongo_client["stocra"]
        self.mongo_collection = mongo_database["txid_to_block_map"]

    async def get_transaction(self, transaction_hash: str) -> dict:
        mapping = await self.mongo_collection.find_one(transaction_hash)
        if mapping is None:
            raise DoesNotExist("Mapping not found")

        raw_block = await self.get_block_by_height(height=mapping["block_number"])

        for raw_transaction in raw_block["transactions"]:
            if raw_transaction["trx"]["id"] == transaction_hash:
                return raw_transaction

        raise DoesNotExist(
            f"Transaction {transaction_hash} not found in mapping to block number {mapping['block_number']}"
        )

    @alru_cache(maxsize=100)
    async def get_block_by_height(self, height: int) -> dict:
        data = dict(block_num_or_id=height)
        return await self.post("v1/chain/get_block", data)

    async def get_block_latest(self) -> dict:
        block_count = await self.get_block_count()
        return await self.get_block_by_height(height=block_count)

    async def get_block_count(self) -> int:
        data = await self.post("v1/chain/get_info")
        return data["head_block_num"]

    async def get_block_by_hash(self, block_hash: str) -> dict:
        data = dict(block_num_or_id=block_hash)
        return await self.post("v1/chain/get_block", data)

    async def post(self, endpoint: str, data: Optional[dict] = None) -> Dict:
        try:
            async with self.session.post(f"{self.url}/{endpoint}", json=data) as response:
                return await self._get_json_or_raise_response_error_aiohttp(response)
        except ClientError as exc:
            raise Unavailable("Node not available") from exc

    @staticmethod
    async def _get_json_or_raise_response_error_aiohttp(response: ClientResponse) -> Dict:
        try:
            response_json = await fast_deserialize_response(response)
            if not response.ok:
                error = response_json["error"]

                if error["code"] in [3100002, 3010008]:
                    raise DoesNotExist()

                response.raise_for_status()

            return response_json
        except asyncio.TimeoutError as exc:
            raise Unavailable("Timeout error") from exc
