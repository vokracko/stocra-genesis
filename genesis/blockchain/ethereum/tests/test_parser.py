from decimal import Decimal

import pytest

from genesis.blockchain.ethereum.adapter import EthereumNodeAdapter
from genesis.blockchain.ethereum.parser import EthereumParser
from genesis.constants import CurrencySymbol


@pytest.fixture
def adapter() -> EthereumNodeAdapter:
    return EthereumNodeAdapter(url="", token="")


@pytest.fixture
def parser(adapter: EthereumNodeAdapter) -> EthereumParser:
    return EthereumParser(adapter)


# @pytest.mark.asyncio
# async def test_decode_block(parser: EthereumParser) -> None:
#     from genesis.blockchain.ethereum.tests.fixtures.block import (
#         BLOCK_DECODED,
#         BLOCK_JSON,
#     )
#
#     decoded_transaction = await parser.decode_block(BLOCK_JSON)
#     assert decoded_transaction == BLOCK_DECODED
#
#
# @pytest.mark.asyncio
# async def test_decode_coinbase_transaction(parser: EthereumParser) -> None:
#     raise NotImplementedError
#

#     from nodes.bitcoin.tests.fixtures.coinbase_transaction import (
#         TRANSACTION_DECODED,
#         TRANSACTION_JSON,
#     )
#
#     decoded_transaction = await parser.decode_transaction(TRANSACTION_JSON)
#     assert decoded_transaction == TRANSACTION_DECODED

#
# @pytest.mark.asyncio
# async def test_decode_transaction(parser: EthereumParser) -> None:
#     from genesis.blockchain.ethereum.tests.fixtures.transaction import (
#         TRANSACTION_DECODED,
#         TRANSACTION_JSON,
#     )
#
#     decoded_transaction = await parser.decode_transaction(TRANSACTION_JSON, decode_inputs=False)
#     assert decoded_transaction == TRANSACTION_DECODED


from genesis.blockchain.ethereum.tests.fixtures.transaction import TRANSACTION_JSON
from genesis.blockchain.ethereum.tests.fixtures.transaction_erc20 import (
    ERC20_ADDRESS,
    ERC20_AMOUNT,
    ERC20_AMOUNT_SCALED,
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
async def test_is_erc_20(parser: EthereumParser, raw_transaction: dict, expected_result: bool) -> None:
    result = await parser.is_erc20_transfer(raw_transaction)
    assert result == expected_result


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "raw_transaction, expected_result",
    [
        (ERC20_TRANSACTION_JSON, ERC20_ADDRESS),
    ],
)
async def test_parse_erc_20_recipient(parser: EthereumParser, raw_transaction: dict, expected_result: bool) -> None:
    result = await parser.parse_erc20_recipient(raw_transaction)
    assert result == expected_result


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "raw_transaction, expected_result",
    [
        (ERC20_TRANSACTION_JSON, ERC20_AMOUNT),
    ],
)
async def test_parse_erc_20_amount(parser: EthereumParser, raw_transaction: dict, expected_result: bool) -> None:
    result = await parser.parse_erc20_amount(raw_transaction)
    assert result == expected_result


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "currency, amount, expected_result",
    [
        (CurrencySymbol.USDT, ERC20_AMOUNT, ERC20_AMOUNT_SCALED),
    ],
)
async def test_scale_erc20_amount(
    parser: EthereumParser, currency: CurrencySymbol, amount: Decimal, expected_result: Decimal
) -> None:
    result = await parser.scale_erc20_amount(currency, amount)
    assert result == expected_result
