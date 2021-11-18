import decimal
import json
from typing import Any


class DecimalEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)
