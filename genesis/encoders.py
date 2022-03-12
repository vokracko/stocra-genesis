import decimal
import json
from typing import Any

import orjson
from aiohttp import ClientResponse


class DecimalEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super().default(o)


def fast_serializer(obj: dict) -> str:
    return orjson.dumps(obj).decode()  # pylint:disable=no-member


def fast_deserializer(data: bytes) -> dict:
    return orjson.loads(data)  # pylint:disable=no-member


async def fast_deserialize_response(response: ClientResponse) -> dict:
    data = await response.read()
    return fast_deserializer(data)
