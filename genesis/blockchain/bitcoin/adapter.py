from base64 import b64encode
from datetime import timedelta
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


class BitcoinNodeAdapter(NodeAdapter):
    BLOCKCHAIN: ClassVar[BlockchainName] = BlockchainName.BITCOIN
    BLOCK_TIME: ClassVar[timedelta] = timedelta(seconds=10)

    async def get_transactions(self, transaction_hashes: List[str], verbose: bool = True) -> Iterable[dict]:
        data = [
            dict(id=i, method="getrawtransaction", params=[transaction_hash, verbose])
            for i, transaction_hash in enumerate(transaction_hashes, start=1)
        ]
        return self.post_list(data)

    async def get_transaction(self, transaction_hash: str, verbose: bool = True) -> dict:
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
        block_height = await self.post(dict(method="getblockcount"))
        return await self.get_block_by_height(block_height, include_transactions=include_transactions)

    async def get_block_including_transactions(self, height: int) -> dict:
        block_hash = await self.get_block_hash(height)
        return await self.get_block_by_hash(block_hash, include_transactions=True)

    async def decode_script(self, script: str) -> dict:
        result = await self.post(dict(method="decodescript", params=[script]))
        return result

    @property
    def headers(self) -> dict:
        token = b64encode(b"rpcuser:rpcpassword").decode("ascii")
        return dict(Authorization=f"Basic {token}")

    @staticmethod
    async def _get_json_or_raise_response_error_aiohttp(response: ClientResponse) -> Union[List, Dict]:
        if not response.ok:
            if response.status == 503:
                raise TooManyRequests("Too many requests")
            elif response.status == 500:
                response_json = await response.json()
                response_error = response_json.get("error")
                response_error_code = response_error["code"]
                response_error_message = response_error["message"]

                if response_error_code in [-1, -5, -8]:
                    raise DoesNotExist(response_error_message)
                elif response_error_code == -28:
                    raise NodeNotReady(response_error_message)

                # TODO this must be logged and investigated
                raise UnknownNodeException(await response.text())

            # TODO this must be logged and investigated
            raise UnknownNodeException(await response.text())

        result = await response.json()
        return cast(dict, result)

    async def post(self, *args, **kwargs) -> Dict:
        result = await super().post(*args, **kwargs)
        return cast(dict, result["result"])

    async def post_list(self, *args, **kwargs) -> Iterable[Dict]:
        result = await super().post(*args, **kwargs)
        for item in result:
            yield item
