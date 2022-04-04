from decimal import Decimal

import pytest
from flexmock import flexmock

from genesis.blockchain.ethereum.parser import EthereumParser
from genesis.blockchain.ethereum.tests.fixtures.transaction import (
    TRANSACTION_DECODED,
    TRANSACTION_JSON,
)
from genesis.blockchain.ethereum.tests.fixtures.transaction_erc20 import (
    ERC20_ADDRESS,
    ERC20_AMOUNT,
    ERC20_TRANSACTION_DECODED,
    ERC20_TRANSACTION_JSON,
)
from genesis.blockchain.ethereum.tests.fixtures.transaction_erc20_unknown import (
    ERC20_TRANSACTION_UNKNOWN_DECODED,
    ERC20_TRANSACTION_UNKNOWN_JSON,
)
from genesis.blockchain.ethereum.tests.fixtures.transaction_receipt import (
    TRANSACTION_RECEIPT_GAS_PRICE,
    TRANSACTION_RECEIPT_GAS_USED,
    TRANSACTION_RECEIPT_JSON,
)
from genesis.blockchain.ethereum.tests.fixtures.transaction_receipt_erc20 import (
    ERC20_TRANSACTION_RECEIPT_JSON,
)
from genesis.blockchain.tests.utils import AwaitableValue


@pytest.mark.asyncio
async def test_decode_block(parser: EthereumParser) -> None:
    from genesis.blockchain.ethereum.tests.fixtures.block import (
        BLOCK_DECODED,
        BLOCK_JSON,
    )

    decoded_transaction = await parser.decode_block(BLOCK_JSON)
    assert decoded_transaction == BLOCK_DECODED


@pytest.mark.asyncio
async def test_decode_transaction(parser: EthereumParser) -> None:
    flexmock(parser.node_adapter).should_receive("get_transaction_receipt").and_return(
        AwaitableValue(TRANSACTION_RECEIPT_JSON)
    )
    decoded_transaction = await parser.decode_transaction(TRANSACTION_JSON)
    assert decoded_transaction == TRANSACTION_DECODED


@pytest.mark.asyncio
async def test_decode_erc20_transaction(parser: EthereumParser) -> None:
    flexmock(parser.node_adapter).should_receive("get_transaction_receipt").and_return(
        AwaitableValue(ERC20_TRANSACTION_RECEIPT_JSON)
    )
    decoded_transaction = await parser.decode_transaction(ERC20_TRANSACTION_JSON)
    assert decoded_transaction == ERC20_TRANSACTION_DECODED


@pytest.mark.asyncio
async def test_decode_erc20_transaction_unknown_token(parser: EthereumParser) -> None:
    flexmock(parser.node_adapter).should_receive("get_transaction_receipt").and_return(
        AwaitableValue(ERC20_TRANSACTION_RECEIPT_JSON)
    )
    decoded_transaction = await parser.decode_transaction(ERC20_TRANSACTION_UNKNOWN_JSON)
    assert decoded_transaction == ERC20_TRANSACTION_UNKNOWN_DECODED


@pytest.mark.parametrize(
    "raw_receipt, expected_result",
    [
        (TRANSACTION_RECEIPT_JSON, TRANSACTION_RECEIPT_GAS_USED),
    ],
)
def test_parse_gas_used(parser: EthereumParser, raw_receipt: dict, expected_result: Decimal) -> None:
    result = parser._parse_gas_used(raw_receipt)
    assert result == expected_result


@pytest.mark.parametrize(
    "raw_receipt, expected_result",
    [
        (TRANSACTION_RECEIPT_JSON, TRANSACTION_RECEIPT_GAS_PRICE),
    ],
)
def test_parse_gas_price(parser: EthereumParser, raw_receipt: dict, expected_result: Decimal) -> None:
    result = parser._parse_gas_price(raw_receipt)
    assert result == expected_result
