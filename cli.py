#!/usr/bin/env python
from fire import Fire

from genesis.blockchain.factory import ADAPTERS

if __name__ == "__main__":
    Fire({blockchain: adapter("http://172.21.0.5:8332") for blockchain, adapter in ADAPTERS.items()})
