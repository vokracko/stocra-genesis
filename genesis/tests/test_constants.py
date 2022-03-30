import pytest

from genesis.blockchains import Blockchain
from genesis.currencies import Currency


def test_blockchain_name_choices() -> None:
    expected = set(
        [
            ("BITCOIN", Blockchain.BITCOIN.value, Blockchain.BITCOIN),
            ("ETHEREUM", Blockchain.ETHEREUM.value, Blockchain.ETHEREUM),
        ]
    )
    assert expected.issubset(Blockchain.choices()) is True


@pytest.mark.parametrize(
    "blockchain_name, exists",
    [
        ("BITCOIN", True),
        ("nonexisting", False),
    ],
)
def test_blockchain_name_exists(blockchain_name: str, exists: bool) -> None:
    assert Blockchain.exists(blockchain_name) is exists


def test_blockchain_name_values() -> None:
    expected = set([Blockchain.BITCOIN.value, Blockchain.ETHEREUM.value])
    assert expected.issubset(Blockchain.values()) is True


@pytest.mark.parametrize(
    "blockchain_name, exists",
    [
        (Blockchain.BITCOIN.value, True),
        ("nonexisting", False),
    ],
)
def test_blockchain_name_value_exists(blockchain_name: str, exists: bool) -> None:
    assert Blockchain.value_exists(blockchain_name) is exists


@pytest.mark.parametrize("name, expected_result", [("Bitcoin", Currency.BITCOIN), ("Ether", Currency.ETHER)])
def test_currency_from_name(name, expected_result):
    assert Currency.from_name(name) == expected_result


def test_currency_from_name_invalid():
    with pytest.raises(ValueError):
        Currency.from_name("nonexisting")


@pytest.mark.parametrize("name, expected_result", [("bitcoin", Blockchain.BITCOIN), ("ethereum", Blockchain.ETHEREUM)])
def test_blockchain_from_name(name, expected_result):
    assert Blockchain.from_name(name) == expected_result


def test_blockchain_from_name_invalid():
    with pytest.raises(ValueError):
        Blockchain.from_name("nonexisting")
