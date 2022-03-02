from datetime import timedelta
from typing import ClassVar, Dict, List, Optional, Union

import aiohttp
from aiohttp import ClientConnectorError, ClientResponse

from genesis.blockchain.exceptions import Unavailable
from genesis.constants import BlockchainName


class NodeAdapter:
    BLOCKCHAIN: ClassVar[BlockchainName]

    url: str
    token: str
    session: aiohttp.ClientSession()

    def __init__(self, url: str, token: str) -> None:
        self.url = url
        self.token = token
        self.session = aiohttp.ClientSession()

    async def get_transactions(self, transaction_hashes: List[str], *, verbose: bool = True) -> List[dict]:
        raise NotImplementedError

    async def get_transaction(self, transaction_hash: str, *, verbose: bool = True) -> dict:
        raise NotImplementedError

    async def get_block_by_hash(self, block_hash: str, *, include_transactions: bool) -> dict:
        raise NotImplementedError

    async def get_block_hash(self, height: int) -> str:
        raise NotImplementedError

    async def get_block_by_height(self, height: int, *, include_transactions: bool) -> dict:
        raise NotImplementedError

    async def get_block_latest(self, *, include_transactions: bool) -> dict:
        raise NotImplementedError

    async def get_block_including_transactions(self, height: int) -> Optional[dict]:
        raise NotImplementedError

    async def get_block_count(self) -> int:
        raise NotImplementedError

    @property
    def headers(self) -> dict:
        raise NotImplementedError

    async def post(self, data: dict) -> Union[Dict]:
        try:
            async with self.session.post(self.url, json=data, headers=self.headers) as response:
                return await self._get_json_or_raise_response_error_aiohttp(response)
        except ClientConnectorError as exc:
            raise Unavailable() from exc

    @staticmethod
    async def _get_json_or_raise_response_error_aiohttp(response: ClientResponse) -> dict:
        raise NotImplementedError
