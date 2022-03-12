import decimal
import json
from typing import Any

import orjson


class DecimalEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super().default(o)


def fast_serializer(obj: dict) -> str:
    return orjson.dumps(obj).decode()  # pylint:disable=no-member
