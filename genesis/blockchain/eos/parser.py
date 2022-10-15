from datetime import datetime
from decimal import Decimal
from typing import ClassVar

from genesis.blockchain.eos.adapter import EosNodeAdapter
from genesis.blockchain.parser import Parser
from genesis.blockchains import Blockchain
from genesis.currencies import Currency
from genesis.logging import get_logger
from genesis.models import Amount, PlainBlock, PlainInput, PlainOutput, PlainTransaction

logger = get_logger(__name__)


class EosParser(Parser):
    BLOCKCHAIN: ClassVar[Blockchain] = Blockchain.EOS
    CURRENCY: ClassVar[Currency] = Currency.EOS
    node_adapter: EosNodeAdapter

    async def decode_block(self, raw_block: dict) -> PlainBlock:
        transactions = [self.get_transaction_id(raw_transaction) for raw_transaction in raw_block["transactions"]]

        return PlainBlock(
            height=raw_block["block_num"],
            hash=raw_block["id"],
            timestamp_ms=datetime.fromisoformat(raw_block["timestamp"]).timestamp() * 1_000,
            transactions=transactions,
        )

    async def decode_transaction(self, raw_transaction: dict) -> PlainTransaction:
        inputs = []
        outputs = []
        fee = Decimal(0)
        raw_trx = raw_transaction["trx"]

        for action in raw_trx["transaction"]["actions"]:
            if action["account"] != "eosio.token":
                continue

            if action["name"] != "transfer":
                continue

            amount = self.parse_amount(action["data"]["quantity"])
            input_ = PlainInput(
                address=action["data"]["from"],
                amount=Amount(
                    value=amount,
                    currency_symbol=self.CURRENCY.symbol,
                ),
            )
            inputs.append(input_)

            output = PlainOutput(
                address=action["data"]["to"],
                amount=Amount(
                    value=amount,
                    currency_symbol=self.CURRENCY.symbol,
                ),
            )
            outputs.append(output)

        return PlainTransaction(
            hash=raw_trx["id"],
            inputs=inputs,
            outputs=outputs,
            fee=Amount(
                value=fee,
                currency_symbol=self.CURRENCY.symbol,
            ),
        )

    def get_transaction_id(self, raw_transaction: dict) -> str:
        raw_trx = raw_transaction["trx"]

        if isinstance(raw_trx, dict):
            return raw_trx["id"]
        else:
            return raw_trx

    def parse_amount(self, amount: str) -> Decimal:
        return Decimal(amount.removesuffix(" EOS"))
