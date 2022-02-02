import asyncio
from typing import Any, Dict, Iterator, cast


class AwaitableValue:
    def __init__(self, value: Any):
        self.value = value

    def __await__(self) -> Iterator:
        future: asyncio.Future = asyncio.Future()
        future.set_result(self.value)
        return iter(future)


class CalledRequests:
    def __init__(self, requests: Dict) -> None:
        self.requests = requests

    def get_request_kwargs(self, position: int = 0) -> dict:
        kwargs = list(self.requests.values())[0][position].kwargs
        return cast(dict, kwargs)
