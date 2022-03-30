from typing import cast

from aiohttp import ClientResponse

from genesis.blockchain.adapter import NodeAdapter
from genesis.blockchain.exceptions import DoesNotExist
from genesis.blockchains import Blockchain
from genesis.encoders import fast_deserialize_response


class EthereumNodeAdapter(NodeAdapter):
    BLOCKCHAIN = Blockchain.ETHEREUM

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
        block_height = await self.get_block_count()
        return await self.get_block_by_height(block_height)

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

    async def post(self, *args, **kwargs) -> dict:
        result = await super().post(*args, **kwargs)
        return cast(dict, result["result"])

    @staticmethod
    async def _get_json_or_raise_response_error_aiohttp(response: ClientResponse) -> dict:
        result = await fast_deserialize_response(response)
        # TODO test busy, not responding, timeout, crashed
        if "error" in result:
            error = result["error"]
            if error["code"] == -32602:
                raise DoesNotExist(error["message"])

        if result["result"] is None:
            raise DoesNotExist()

        return result
