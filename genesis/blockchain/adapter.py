from datetime import timedelta
from typing import ClassVar, Dict, Optional, cast

import aiohttp
from aiohttp import ClientConnectorError, ClientResponse

from genesis.blockchain.exceptions import Unavailable
from genesis.constants import BlockchainName


class NodeAdapter:
    BLOCKCHAIN: ClassVar[BlockchainName]
    BLOCK_TIME: ClassVar[timedelta]

    url: str

    def __init__(self, url: str) -> None:
        self.url = url

    async def get_transaction(self, transaction_hash: str) -> dict:
        raise NotImplementedError

    async def get_block_by_hash(self, block_hash: str, *, include_transactions: bool) -> dict:
        raise NotImplementedError

    async def get_block_hash(self, height: int, *, include_transactions: bool) -> str:
        raise NotImplementedError

    async def get_block_by_height(self, height: int, *, include_transactions: bool) -> dict:
        raise NotImplementedError

    async def get_block_latest(self, *, include_transactions: bool) -> dict:
        raise NotImplementedError

    async def get_block_including_transactions(self, height: int) -> Optional[dict]:
        return await self._get_block_including_transactions(height)

    async def _get_block_including_transactions(self, height: int) -> Optional[dict]:
        raise NotImplementedError

    @property
    def headers(self) -> dict:
        raise NotImplementedError

    async def post(self, data: dict) -> Dict:
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(self.url, json=data, headers=self.headers) as response:
                    response_json = await self._get_json_or_raise_response_error_aiohttp(response)
                    return cast(dict, response_json["result"])
            except ClientConnectorError:
                raise Unavailable()

    @staticmethod
    async def _get_json_or_raise_response_error_aiohttp(response: ClientResponse) -> dict:
        raise NotImplementedError
