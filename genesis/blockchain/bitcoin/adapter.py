from typing import ClassVar, Dict, Iterable, List, Union, cast

from aiohttp import ClientResponse

from genesis.blockchain.adapter import NodeAdapter
from genesis.blockchain.exceptions import (
    DoesNotExist,
    NodeNotReady,
    TooManyRequests,
    UnknownNodeException,
)
from genesis.constants import BlockchainName
from genesis.encoders import fast_deserialize_response


class BitcoinNodeAdapter(NodeAdapter):
    BLOCKCHAIN: ClassVar[BlockchainName] = BlockchainName.BITCOIN

    async def get_transactions(self, transaction_hashes: List[str], *, verbose: bool = True) -> Iterable[dict]:
        data = [
            dict(id=i, method="getrawtransaction", params=[transaction_hash, verbose])
            for i, transaction_hash in enumerate(transaction_hashes, start=1)
        ]
        return self.post_list(data)

    async def get_transaction(self, transaction_hash: str, *, verbose: bool = True) -> dict:
        return await self.post(dict(method="getrawtransaction", params=[transaction_hash, verbose]))

    async def get_block_by_hash(self, block_hash: str, *, include_transactions: bool) -> dict:
        data = dict(
            method="getblock",
            params=[block_hash, 2 if include_transactions else 1],
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

    async def get_block_by_height(self, height: int, *, include_transactions: bool) -> dict:
        block_hash = await self.get_block_hash(height)
        return await self.get_block_by_hash(block_hash, include_transactions=include_transactions)

    async def get_block_latest(self, *, include_transactions: bool) -> dict:
        block_height = await self.get_block_count()
        return await self.get_block_by_height(block_height, include_transactions=include_transactions)

    async def get_block_count(self) -> int:
        return await self.post(dict(method="getblockcount"))

    async def decode_script(self, script: str) -> dict:
        result = await self.post(dict(method="decodescript", params=[script]))
        return result

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

        result = await fast_deserialize_response(response)
        return result

    async def post(self, *args, **kwargs) -> Dict:
        result = await super().post(*args, **kwargs)
        return cast(dict, result["result"])

    async def post_list(self, *args, **kwargs) -> Iterable[Dict]:
        result = await super().post(*args, **kwargs)
        for item in result:
            yield item
