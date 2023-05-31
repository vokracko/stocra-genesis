# Genesis library
Library to interact with blockchain nodes

## Installation
```bash
poetry add git+https://github.com/vokracko/stocra-genesis.git
```

## Usage
```python
from genesis.blockchain.factory import NodeAdapterFactory, ParserFactory

adapter = await NodeAdapterFactory.get_client("<node_blockchain>", url="<node_url>", token="<node_token>")
parser = await ParserFactory.get_parser("<node_blockchain>", adapter)
raw_block = await adapter.get_block_by_height(height="<block_height>")
await parser.decode_block(raw_block)
```

## Development
### Adding new blockchains/currencies
1. Add new blockchain to [genesis/blockchains.py](genesis/blockchains.py)
2. Add new currency to [genesis/currencies.py](genesis/currencies.py)
3. Add new token type in [genesis/tokens.py](genesis/tokens.py)
4. Define new adapter in [genesis/blockchain/adapters](genesis/blockchain/adapters)
5. Define new parser in [genesis/blockchain/parsers](genesis/blockchain/parsers)
6. Add adapter and parser into [genesis/blockchain/factory.py](genesis/blockchain/factory.py)
