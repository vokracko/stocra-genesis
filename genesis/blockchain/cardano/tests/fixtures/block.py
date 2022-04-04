from genesis.models import PlainBlock

BLOCK_JSON = {
    "id": 3339,
    "hash": "86b54dd69f404bb9656ee766e8c019dae3b5ef4ea00c04ef2e5597c9799214a8",
    "height": 3337,
    "timestamp_ms": 1506269811000.0,
}

BLOCK_DECODED = PlainBlock(
    height=3337,
    hash="86b54dd69f404bb9656ee766e8c019dae3b5ef4ea00c04ef2e5597c9799214a8",
    timestamp_ms=1506269811000,
    transactions=["dbd87b3876da9847c01b7f229a4126ea113cdd17494ba6b86e714b4ca1864fcd"],
)
