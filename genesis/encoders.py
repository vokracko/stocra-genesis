from decimal import Decimal, getcontext

import orjson
from aiohttp import ClientResponse


def default_object_serializer(obj: object):
    if isinstance(obj, Decimal):
        return serialize_decimal(obj)
    raise TypeError


def fast_serializer_to_bytes(obj: dict) -> bytes:
    return orjson.dumps(obj, default=default_object_serializer)  # pylint:disable=no-member


def fast_serializer_to_str(obj: dict) -> str:
    return fast_serializer_to_bytes(obj).decode()


def fast_deserializer_from_bytes(data: bytes) -> dict:
    return orjson.loads(data)  # pylint:disable=no-member


def fast_deserializer_from_str(data: str) -> dict:
    return fast_deserializer_from_bytes(data.encode())


async def fast_deserialize_response(response: ClientResponse) -> dict:
    data = await response.read()
    return fast_deserializer_from_bytes(data)


def serialize_decimal(value: Decimal) -> str:
    if value == Decimal("0"):
        return "0"

    value_str = f"{value:.30f}"

    if "." not in value_str:
        return value_str

    stripped_value = value_str.rstrip("0")
    return stripped_value.removesuffix(".")
