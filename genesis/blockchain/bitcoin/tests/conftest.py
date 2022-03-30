from typing import cast

import pytest

from genesis.blockchain.bitcoin.adapter import BitcoinNodeAdapter
from genesis.blockchain.factory import NodeAdapterFactory
from genesis.blockchains import Blockchain

NODE_TOKEN = "token"
NODE_URL = "http://127.0.0.1:666/"
EXPECTED_HEADERS = dict(Authorization=f"Basic {NODE_TOKEN}")


@pytest.fixture
def adapter() -> BitcoinNodeAdapter:
    client = NodeAdapterFactory.get_client(Blockchain.BITCOIN, url=NODE_URL, token=NODE_TOKEN)
    return cast(BitcoinNodeAdapter, client)
