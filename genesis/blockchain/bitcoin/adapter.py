from base64 import b64encode
from datetime import timedelta
from typing import ClassVar, cast

from aiohttp import ClientResponse

from genesis.blockchain.adapter import NodeAdapter
from genesis.blockchain.exceptions import (
    AdapterException,
    BlockDoesNotExist,
    NodeNotReady,
)
from genesis.constants import BlockchainName
from genesis.profiling import log_duration


class BitcoinNodeAdapter(NodeAdapter):
    BLOCKCHAIN: ClassVar[BlockchainName] = BlockchainName.BITCOIN
    BLOCK_TIME: ClassVar[timedelta] = timedelta(seconds=10)

    async def get_transaction(self, transaction_hash: str, verbose: bool = True) -> dict:
        return await self.post(dict(method="getrawtransaction", params=[transaction_hash, verbose]))

    async def get_block_by_hash(self, block_hash: str, verbosity: int = 2) -> dict:
        data = dict(
            method="getblock",
            params=[block_hash, verbosity],
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

    async def get_block_by_height(self, height: int, verbosity: int = 2) -> dict:
        with log_duration("Get block hash"):
            block_hash = await self.get_block_hash(height)

        with log_duration("Get block by hash"):
            return await self.get_block_by_hash(block_hash, verbosity)

    async def get_block_latest(self) -> dict:
        block_height = await self.post(
            dict(
                method="getblockcount",
            )
        )
        return await self.get_block_by_height(block_height)

    async def _get_block_including_transactions(self, height: int) -> dict:
        block_hash = await self.get_block_hash(height)
        return await self.get_block_by_hash(block_hash)

    async def decode_script(self, script: str) -> dict:
        result = await self.post(dict(method="decodescript", params=[script]))
        return result

    @property
    def headers(self) -> dict:
        token = b64encode(b"rpcuser:rpcpassword").decode("ascii")
        return dict(Authorization=f"Basic {token}")

    @staticmethod
    async def _get_json_or_raise_response_error_aiohttp(response: ClientResponse) -> dict:
        if response.status == 400:
            response_json = await response.json()
            response_error = response_json.get("error")
            if response_error["code"] == -28:
                raise NodeNotReady(response_error["message"])
            raise AdapterException(response_error)
        elif response.status == 500:
            response_json = await response.json()
            response_error = response_json.get("error")
            if response_error["code"] == -8:
                raise BlockDoesNotExist(response_error["message"])
            raise AdapterException(response_error)

        response.raise_for_status()
        result = await response.json()
        return cast(dict, result)
