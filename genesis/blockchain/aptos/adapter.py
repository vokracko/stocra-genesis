from typing import ClassVar, Dict

from aiohttp import ClientError, ClientResponse, ClientSession

from genesis.blockchain.adapter import NodeAdapter
from genesis.blockchain.exceptions import Unavailable
from genesis.blockchains import Blockchain
from genesis.encoders import fast_deserialize_response, fast_serializer_to_str


class AptosNodeAdapter(NodeAdapter):
    BLOCKCHAIN: ClassVar[Blockchain] = Blockchain.APTOS
    session: ClientSession

    async def init_async(self) -> None:
        self.session = ClientSession(json_serialize=fast_serializer_to_str)

    async def get_transaction(self, transaction_hash: str) -> dict:
        return await self.get(f"v1/transactions/by_hash/{transaction_hash}")

    async def get_block_by_hash(self, block_hash: str) -> dict:
        raise NotImplementedError

    async def get_block_by_height(self, height: int) -> dict:
        return await self.get(f"v1/blocks/by_height/{height}?with_transactions=true")

    async def get_block_latest(self) -> dict:
        latest_block_height = await self.get_block_count()
        return await self.get_block_by_height(height=latest_block_height)

    async def get_block_count(self) -> int:
        result = await self.get("v1/")
        return result["block_height"]

    async def get(self, endpoint: str) -> Dict:
        try:
            async with self.session.get(f"{self.url}/{endpoint}") as response:
                return await self._get_json_or_raise_response_error_aiohttp(response)
        except ClientError as exc:
            raise Unavailable("Node not available") from exc

    async def _get_json_or_raise_response_error_aiohttp(self, response: ClientResponse):
        # {"message":"Block not found by Block height(429339)","error_code":"block_not_found","vm_error_code":null}
        return await fast_deserialize_response(response)
