from typing import cast

import pytest
import pytest_asyncio

from genesis.blockchain.aptos.adapter import AptosNodeAdapter
from genesis.blockchain.aptos.parser import AptosParser
from genesis.blockchain.factory import NodeAdapterFactory, ParserFactory
from genesis.blockchains import Blockchain

NODE_TOKEN = "token"
NODE_URL = "http://127.0.0.1:666/"
EXPECTED_HEADERS = dict(Authorization=f"Basic {NODE_TOKEN}")


@pytest_asyncio.fixture
async def adapter() -> AptosNodeAdapter:
    client = await NodeAdapterFactory.get_client(Blockchain.APTOS, url=NODE_URL)
    return cast(AptosNodeAdapter, client)


@pytest_asyncio.fixture
async def parser(adapter: AptosNodeAdapter) -> AptosParser:
    instance = await ParserFactory.get_parser(Blockchain.APTOS, adapter)
    return cast(AptosParser, instance)
