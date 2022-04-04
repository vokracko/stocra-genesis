from decimal import Decimal
from typing import ClassVar, List

import logging518 as logging

from genesis.blockchain.cardano.adapter import CardanoNodeAdapter
from genesis.blockchain.parser import Parser
from genesis.blockchains import Blockchain
from genesis.currencies import Currency
from genesis.models import (
    Amount,
    PlainBlock,
    PlainInput,
    PlainOutput,
    PlainTransaction,
    PlainTransactionPointer,
)

logger = logging.get_logger(__name__)


class CardanoParser(Parser):
    BLOCKCHAIN: ClassVar[Blockchain] = Blockchain.CARDANO
    CURRENCY: ClassVar[Currency] = Currency.ADA
    node_adapter: CardanoNodeAdapter

    LOVELACE_SCALE: Decimal = Decimal("1e-6")

    def __init__(self, node_adapter: CardanoNodeAdapter) -> None:
        super().__init__(node_adapter)

    async def decode_block(self, raw_block: dict) -> PlainBlock:
        transactions_raw = await self.node_adapter.get_list_of_transactions_in_block(raw_block["id"])
        transactions = [transaction["hash"] for transaction in transactions_raw]
        return PlainBlock(
            height=raw_block["height"],
            hash=raw_block["hash"],
            timestamp_ms=raw_block["timestamp_ms"],
            transactions=transactions,
        )

    async def decode_transaction(self, raw_transaction: dict) -> PlainTransaction:
        outputs = self._get_outputs_with_amounts_from_raw_transaction(raw_transaction["inputs_outputs"])
        inputs = self._get_inputs_from_raw_transaction(raw_transaction["inputs_outputs"])
        amount = self._get_total_amount_from_raw_transaction(outputs)
        fee = sum([input_.amount.value for input_ in inputs]) - amount

        return PlainTransaction(
            hash=raw_transaction["hash"],
            inputs=inputs,
            outputs=outputs,
            amount=Amount(
                value=amount,
                currency_symbol=self.CURRENCY.symbol,
            ),
            fee=Amount(value=fee, currency_symbol=self.CURRENCY.symbol),
        )

    def _get_inputs_from_raw_transaction(self, inputs_outputs: List[dict]) -> List[PlainInput]:
        inputs = []

        for input_output in inputs_outputs:
            if not input_output["transaction_pointer_hash"]:
                continue
            input_ = PlainInput(
                address=input_output["address"],
                amount=Amount(
                    value=Decimal(str(input_output["amount"])) * self.LOVELACE_SCALE,
                    currency_symbol=self.CURRENCY.symbol,
                ),
                transaction_pointer=PlainTransactionPointer(
                    transaction_hash=input_output["transaction_pointer_hash"],
                    output_index=input_output["transaction_pointer_index"],
                ),
            )
            inputs.append(input_)

        return inputs

    def _get_outputs_with_amounts_from_raw_transaction(self, inputs_outputs: List[dict]) -> List[PlainOutput]:
        outputs = []

        for input_output in inputs_outputs:
            if input_output["transaction_pointer_hash"]:
                continue
            output = PlainOutput(
                address=input_output["address"],
                amount=Amount(
                    value=Decimal(str(input_output["amount"])) * self.LOVELACE_SCALE,
                    currency_symbol=self.CURRENCY.symbol,
                ),
            )
            outputs.append(output)

        return outputs

    def _get_total_amount_from_raw_transaction(self, outputs: List[PlainOutput]) -> Decimal:
        return sum([output.amount.value for output in outputs], start=Decimal("0"))
