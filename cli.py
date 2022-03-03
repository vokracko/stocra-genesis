#!/usr/bin/env python
from fire import Fire

from genesis.blockchain.factory import ADAPTERS

TOKEN = "d2VmaWplcmtsajprbDIzMDk0ODIzMDlmbV9hd2RjJV5AJQ=="

if __name__ == "__main__":
    Fire({blockchain.value: adapter("http://dogecoin-node-1:8000", TOKEN) for blockchain, adapter in ADAPTERS.items()})
