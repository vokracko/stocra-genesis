from decimal import Decimal

import pytest

from genesis.encoders import serialize_decimal


@pytest.mark.parametrize(
    "value, expected_result",
    [
        (Decimal("005"), "5"),
        (Decimal("0.5"), "0.5"),
        (Decimal("10"), "10"),
        (Decimal("0.000000"), "0"),
        (Decimal("0.000010"), "0.00001"),
        (Decimal("1.2345e-18"), "0.0000000000000000012345"),
    ],
)
def test_serialize_decimal(value: Decimal, expected_result: str):
    assert serialize_decimal(value) == expected_result
