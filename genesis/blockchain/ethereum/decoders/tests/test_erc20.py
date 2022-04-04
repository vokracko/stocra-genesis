import pytest

from genesis.blockchain.ethereum.decoders.erc20 import ERC20Decoder
from genesis.blockchain.ethereum.tests.fixtures.transaction import TRANSACTION_JSON
from genesis.blockchain.ethereum.tests.fixtures.transaction_erc20 import (
    ERC20_ADDRESS,
    ERC20_AMOUNT,
    ERC20_TRANSACTION_JSON,
)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "raw_transaction, expected_result",
    [
        (TRANSACTION_JSON, False),
        (ERC20_TRANSACTION_JSON, True),
    ],
)
async def test_matches(raw_transaction: dict, expected_result: bool) -> None:
    result = await ERC20Decoder.matches(raw_transaction["input"])
    assert result == expected_result


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "raw_transaction, expected_result",
    [
        (ERC20_TRANSACTION_JSON, ERC20_ADDRESS),
    ],
)
async def test_get_output_address(raw_transaction: dict, expected_result: bool) -> None:
    result = await ERC20Decoder.get_output_address(raw_transaction["input"])
    assert result == expected_result


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "raw_transaction, expected_result",
    [
        (ERC20_TRANSACTION_JSON, ERC20_AMOUNT),
    ],
)
async def test_get_amount(raw_transaction: dict, expected_result: bool) -> None:
    result = await ERC20Decoder.get_amount(raw_transaction["input"])
    assert result == expected_result
