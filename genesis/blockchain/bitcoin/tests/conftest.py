from typing import cast

import pytest

from genesis.blockchain.bitcoin.adapter import BitcoinNodeAdapter
from genesis.blockchain.factory import NodeAdapterFactory
from genesis.constants import BlockchainName

EXPECTED_HEADERS = dict(Authorization="Basic cnBjdXNlcjpycGNwYXNzd29yZA==")
NODE_URL = "http://127.0.0.1:666/"


@pytest.fixture
def adapter() -> BitcoinNodeAdapter:
    client = NodeAdapterFactory.get_client(BlockchainName.BITCOIN, url=NODE_URL)
    return cast(BitcoinNodeAdapter, client)
