import pytest

from genesis.constants import BlockchainName


def test_blockchain_name_choices() -> None:
    expected = set(
        [
            ("BITCOIN", BlockchainName.BITCOIN.value),
            ("ETHEREUM", BlockchainName.ETHEREUM.value),
        ]
    )
    assert expected.issubset(BlockchainName.choices()) is True


@pytest.mark.parametrize(
    "blockchain_name, exists",
    [
        ("BITCOIN", True),
        ("nonexisting", False),
    ],
)
def test_blockchain_name_exists(blockchain_name: str, exists: bool) -> None:
    assert BlockchainName.exists(blockchain_name) is exists


def test_blockchain_name_values() -> None:
    expected = set([BlockchainName.BITCOIN.value, BlockchainName.ETHEREUM.value])
    assert expected.issubset(BlockchainName.values()) is True


@pytest.mark.parametrize(
    "blockchain_name, exists",
    [
        (BlockchainName.BITCOIN.value, True),
        ("nonexisting", False),
    ],
)
def test_blockchain_name_value_exists(blockchain_name: str, exists: bool) -> None:
    assert BlockchainName.value_exists(blockchain_name) is exists
