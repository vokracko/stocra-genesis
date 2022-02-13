#!/usr/bin/env python
from fire import Fire

from genesis.blockchain.factory import ADAPTERS

if __name__ == "__main__":
    Fire({blockchain.value: adapter("http://nodes-bitcoin-1:8332") for blockchain, adapter in ADAPTERS.items()})
