from copy import deepcopy

import pytest

from genesis.models import PlainBlock


@pytest.fixture
def transaction_dict() -> dict:
    return dict(
        hash="0x2",
        inputs=[],
        outputs=[],
        amount="10",
        fee="1",
    )


@pytest.fixture
def block_dict(transaction_dict: dict) -> dict:
    return dict(
        height=1,
        hash="0x1",
        timestamp=1234567890,
        transactions=[transaction_dict],
    )


@pytest.fixture
def plain_block(block_dict: dict) -> PlainBlock:
    return PlainBlock(**block_dict)


def test_plainblock_asdict(plain_block: PlainBlock, block_dict: dict) -> None:
    assert plain_block.asdict() == block_dict


def test_plainblock_asdict_exclude_transactions(plain_block: PlainBlock, block_dict: dict) -> None:
    block_dict_without_transactions = deepcopy(block_dict)
    block_dict_without_transactions.pop("transactions")
    assert plain_block.asdict(exclude="transactions") == block_dict_without_transactions
