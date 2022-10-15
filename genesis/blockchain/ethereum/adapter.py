import asyncio
from typing import Dict, cast

from aiohttp import ClientError, ClientResponse, ClientSession

from genesis.blockchain.adapter import NodeAdapter
from genesis.blockchain.exceptions import DoesNotExist, Unavailable
from genesis.blockchains import Blockchain
from genesis.encoders import fast_deserialize_response, fast_serializer_to_str


class EthereumNodeAdapter(NodeAdapter):
    BLOCKCHAIN = Blockchain.ETHEREUM

    session: ClientSession

    async def init_async(self) -> None:
        self.session = ClientSession(json_serialize=fast_serializer_to_str)

    async def get_transaction(self, transaction_hash: str) -> dict:
        data = dict(
            jsonrpc="2.0",
            method="eth_getTransactionByHash",
            params=[transaction_hash],
            id=1,
        )
        return await self.post(data)

    async def get_transaction_receipt(self, transaction_hash: str) -> dict:
        data = dict(
            jsonrpc="2.0",
            method="eth_getTransactionReceipt",
            params=[transaction_hash],
            id=1,
        )
        return await self.post(data)

    async def get_block_by_hash(self, block_hash: str) -> dict:
        data = dict(
            jsonrpc="2.0",
            method="eth_getBlockByHash",
            params=[block_hash, False],
            id=1,
        )
        return await self.post(data)

    async def get_block_hash(self, height: int) -> str:
        raise NotImplementedError

    async def get_block_by_height(self, height: int) -> dict:
        data = dict(
            jsonrpc="2.0",
            method="eth_getBlockByNumber",
            params=[hex(height), False],
            id=1,
        )
        return await self.post(data)

    async def get_block_latest(self) -> dict:
        data = dict(
            jsonrpc="2.0",
            method="eth_getBlockByNumber",
            params=["latest", False],
            id=1,
        )
        return await self.post(data)

    async def get_block_count(self) -> int:
        data = dict(
            jsonrpc="2.0",
            method="eth_blockNumber",
            params=[],
            id=1,
        )
        result = await self.post(data)
        return int(result, 16)

    @property
    def headers(self) -> dict:
        return {}

    async def post(self, data: dict) -> Dict:
        try:
            async with self.session.post(self.url, json=data, headers=self.headers) as response:
                result = await self._get_json_or_raise_response_error_aiohttp(response)
                return cast(dict, result["result"])
        except ClientError as exc:
            raise Unavailable("Node not available") from exc

    @staticmethod
    async def _get_json_or_raise_response_error_aiohttp(response: ClientResponse) -> dict:
        try:
            result = await fast_deserialize_response(response)
        except asyncio.TimeoutError as exc:
            raise Unavailable("Timeout error") from exc

        if "error" in result:
            error = result["error"]
            if error["code"] == -32602:
                raise DoesNotExist(error["message"])

        if result["result"] is None:
            raise DoesNotExist()

        return result

    def __del__(self) -> None:
        if self.session:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self.session.close())
