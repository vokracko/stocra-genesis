from decimal import Decimal

import pytest

from genesis.currencies import Currency
from genesis.models import Amount, PlainTransaction


def test_amount_add():
    x = Amount(value=Decimal("1"), currency_symbol=Currency.BITCOIN.symbol)
    y = Amount(value=Decimal("2"), currency_symbol=Currency.BITCOIN.symbol)
    assert x + y == Amount(value=Decimal("3"), currency_symbol=Currency.BITCOIN.symbol)


def test_amount_add_wrong_currency():
    x = Amount(value=Decimal("1"), currency_symbol=Currency.BITCOIN.symbol)
    y = Amount(value=Decimal("2"), currency_symbol=Currency.ETHER.symbol)
    with pytest.raises(ValueError):
        x + y


def test_amount_add_wrong_type():
    x = Amount(value=Decimal("1"), currency_symbol=Currency.BITCOIN.symbol)
    with pytest.raises(ValueError):
        x + Decimal("2")


@pytest.mark.parametrize(
    "first, second, expected_result",
    [
        (
            Amount(value=Decimal("1"), currency_symbol=Currency.BITCOIN.symbol),
            Amount(value=Decimal("1"), currency_symbol=Currency.BITCOIN.symbol),
            True,
        ),
        (
            Amount(value=Decimal("1"), currency_symbol=Currency.BITCOIN.symbol),
            Amount(value=Decimal("2"), currency_symbol=Currency.BITCOIN.symbol),
            False,
        ),
        (
            Amount(value=Decimal("1"), currency_symbol=Currency.BITCOIN.symbol),
            Amount(value=Decimal("1"), currency_symbol=Currency.ETHER.symbol),
            False,
        ),
    ],
)
def test_amount_equal(first, second, expected_result):
    result = first == second
    assert result is expected_result


def test_amount_equal_wrong_type():
    with pytest.raises(ValueError):
        Amount(value=Decimal("1"), currency_symbol=Currency.BITCOIN.symbol) == Decimal("1")


def test_negative_fee():
    with pytest.raises(ValueError):
        PlainTransaction(
            fee=Amount(value=Decimal("-1"), currency_symbol=Currency.BITCOIN.value)
        )
