from typing import cast

import pytest
import pytest_asyncio

from genesis.blockchain.bitcoin.adapter import BitcoinNodeAdapter
from genesis.blockchain.bitcoin.parser import BitcoinParser
from genesis.blockchain.factory import NodeAdapterFactory, ParserFactory
from genesis.blockchains import Blockchain

NODE_TOKEN = "token"
NODE_URL = "http://127.0.0.1:666/"
EXPECTED_HEADERS = dict(Authorization=f"Basic {NODE_TOKEN}")


@pytest_asyncio.fixture
async def adapter() -> BitcoinNodeAdapter:
    client = await NodeAdapterFactory.get_client(Blockchain.BITCOIN, url=NODE_URL, token=NODE_TOKEN)
    return cast(BitcoinNodeAdapter, client)


@pytest_asyncio.fixture
async def parser(adapter: BitcoinNodeAdapter) -> BitcoinParser:
    instance = await ParserFactory.get_parser(Blockchain.BITCOIN, adapter)
    return cast(BitcoinParser, instance)
