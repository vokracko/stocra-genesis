from typing import cast

import pytest
import pytest_asyncio

from genesis.blockchain.ethereum.adapter import EthereumNodeAdapter
from genesis.blockchain.ethereum.parser import EthereumParser
from genesis.blockchain.ethereum.tests.test_adapter import NODE_URL
from genesis.blockchain.factory import NodeAdapterFactory, ParserFactory
from genesis.blockchains import Blockchain


@pytest_asyncio.fixture
@pytest.mark.asyncio
async def adapter() -> EthereumNodeAdapter:
    client = await NodeAdapterFactory.get_client(Blockchain.ETHEREUM, url=NODE_URL, token="")
    return cast(EthereumNodeAdapter, client)


@pytest.fixture
async def parser(adapter: EthereumNodeAdapter) -> EthereumParser:
    instance = await ParserFactory.get_parser(Blockchain.ETHEREUM, adapter)
    return cast(EthereumParser, instance)
