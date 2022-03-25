from typing import Optional, cast

from aiohttp import ClientResponse

from genesis.blockchain.adapter import NodeAdapter
from genesis.constants import BlockchainName
from genesis.encoders import fast_deserialize_response


class EthereumNodeAdapter(NodeAdapter):
    BLOCKCHAIN = BlockchainName.ETHEREUM

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

    async def get_block_by_hash(self, block_hash: str, *, include_transactions: bool) -> dict:
        data = dict(
            jsonrpc="2.0",
            method="eth_getBlockByHash",
            params=[block_hash, include_transactions],
            id=1,
        )
        return await self.post(data)

    async def get_block_hash(self, height: int) -> str:
        raise NotImplementedError

    async def get_block_by_height(self, height: int, *, include_transactions: bool = True) -> dict:
        data = dict(
            jsonrpc="2.0",
            method="eth_getBlockByNumber",
            params=[hex(height), include_transactions],
            id=1,
        )
        return await self.post(data)

    async def get_block_latest(self, *, include_transactions: bool) -> dict:
        raise NotImplementedError

    @property
    def headers(self) -> dict:
        return {}

    async def post(self, *args, **kwargs) -> dict:
        result = await super().post(*args, **kwargs)
        return cast(dict, result["result"])

    @staticmethod
    async def _get_json_or_raise_response_error_aiohttp(response: ClientResponse) -> dict:
        # TODO handle error cases
        result = await fast_deserialize_response(response)
        return result
