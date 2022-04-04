import asyncio
from typing import ClassVar, Dict, Iterable, List, Union, cast

from aiohttp import ClientError, ClientResponse, ClientSession

from genesis.blockchain.adapter import NodeAdapter
from genesis.blockchain.exceptions import (
    DoesNotExist,
    NodeNotReady,
    TooManyRequests,
    Unavailable,
    UnknownNodeException,
)
from genesis.blockchains import Blockchain
from genesis.encoders import fast_deserialize_response, fast_serializer_to_str


class BitcoinNodeAdapter(NodeAdapter):
    BLOCKCHAIN: ClassVar[Blockchain] = Blockchain.BITCOIN
    session: ClientSession

    async def init_async(self):
        self.session = ClientSession(json_serialize=fast_serializer_to_str)

    async def get_transaction(self, transaction_hash: str) -> dict:
        return await self.post(dict(method="getrawtransaction", params=[transaction_hash, True]))

    async def get_block_by_hash(self, block_hash: str) -> dict:
        data = dict(
            method="getblock",
            params=[block_hash, 1],
        )
        return await self.post(data)

    async def get_block_hash(self, height: int) -> str:
        block_hash = await self.post(
            dict(
                method="getblockhash",
                params=[height],
            )
        )
        return cast(str, block_hash)

    async def get_block_by_height(self, height: int) -> dict:
        block_hash = await self.get_block_hash(height)
        return await self.get_block_by_hash(block_hash)

    async def get_block_latest(self) -> dict:
        block_height = await self.get_block_count()
        return await self.get_block_by_height(block_height)

    async def get_block_count(self) -> int:
        return await self.post(dict(method="getblockcount"))

    async def decode_script(self, script: str) -> dict:
        return await self.post(dict(method="decodescript", params=[script]))

    async def get_transactions(self, transaction_hashes: List[str]) -> Iterable[dict]:
        data = [
            dict(id=i, method="getrawtransaction", params=[transaction_hash, True])
            for i, transaction_hash in enumerate(transaction_hashes, start=1)
        ]
        return self.post_multiple(data)

    @property
    def headers(self) -> dict:
        return dict(Authorization=f"Basic {self.token}")

    @staticmethod
    async def _get_json_or_raise_response_error_aiohttp(response: ClientResponse) -> Union[List, Dict]:
        if not response.ok:
            if response.status == 503:
                raise TooManyRequests("Too many requests")

            if response.status == 500:
                response_json = await fast_deserialize_response(response)
                response_error = response_json.get("error")
                response_error_code = response_error["code"]
                response_error_message = response_error["message"]

                if response_error_code in [-1, -5, -8]:
                    raise DoesNotExist(response_error_message)

                if response_error_code == -28:
                    raise NodeNotReady(response_error_message)

            raise UnknownNodeException(await response.text())

        return await fast_deserialize_response(response)

    async def post(self, data: dict) -> Dict:
        result = await self._post(data)
        return cast(dict, result["result"])

    async def _post(self, data: dict) -> Union[Dict]:
        try:
            async with self.session.post(self.url, json=data, headers=self.headers) as response:
                return await self._get_json_or_raise_response_error_aiohttp(response)
        except ClientError as exc:
            raise Unavailable("Node not available") from exc

    async def post_multiple(self, *args, **kwargs) -> Iterable[Dict]:
        result = await self._post(*args, **kwargs)
        for item in result:
            yield item

    def __del__(self):
        if self.session:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self.session.close())
