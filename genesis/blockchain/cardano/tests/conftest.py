from typing import cast

import pytest_asyncio
from flexmock import flexmock

from genesis.blockchain.cardano.adapter import CardanoNodeAdapter
from genesis.blockchain.cardano.parser import CardanoParser
from genesis.blockchain.factory import NodeAdapterFactory, ParserFactory
from genesis.blockchain.tests.utils import AwaitableValue
from genesis.blockchains import Blockchain

NODE_TOKEN = "token"
NODE_URL = "postgres://localhost"


@pytest_asyncio.fixture
async def adapter() -> CardanoNodeAdapter:
    flexmock(CardanoNodeAdapter).should_receive("init_async").and_return(AwaitableValue(None))
    client = await NodeAdapterFactory.get_client(Blockchain.CARDANO, url=NODE_URL, token="")
    return cast(CardanoNodeAdapter, client)


@pytest_asyncio.fixture
async def parser(adapter: CardanoNodeAdapter) -> CardanoParser:
    instance = await ParserFactory.get_parser(Blockchain.CARDANO, adapter)
    return cast(CardanoParser, instance)
