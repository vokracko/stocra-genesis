from typing import cast

import pytest_asyncio

from genesis.blockchain.eos.adapter import EosNodeAdapter
from genesis.blockchain.eos.parser import EosParser
from genesis.blockchain.factory import NodeAdapterFactory, ParserFactory
from genesis.blockchains import Blockchain

NODE_URL = "http://127.0.0.1:666/"


@pytest_asyncio.fixture
async def adapter() -> EosNodeAdapter:
    client = await NodeAdapterFactory.get_client(Blockchain.EOS, NODE_URL)
    return cast(EosNodeAdapter, client)


@pytest_asyncio.fixture
async def parser(adapter: EosNodeAdapter) -> EosParser:
    instance = await ParserFactory.get_parser(Blockchain.EOS, adapter)
    return cast(EosParser, instance)
