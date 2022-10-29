from decimal import Decimal
from typing import ClassVar

from genesis.blockchain.aptos.adapter import AptosNodeAdapter
from genesis.blockchain.parser import Parser
from genesis.blockchains import Blockchain
from genesis.currencies import Currency
from genesis.logging import get_logger
from genesis.models import Amount, PlainBlock, PlainInput, PlainOutput, PlainTransaction

logger = get_logger(__name__)


class AptosParser(Parser):
    BLOCKCHAIN: ClassVar[Blockchain] = Blockchain.APTOS
    CURRENCY: ClassVar[Currency] = Currency.APTOS
    SCALING_FACTOR: ClassVar[Decimal] = Decimal("1e-8")
    node_adapter: AptosNodeAdapter

    async def decode_block(self, raw_block: dict) -> PlainBlock:
        return PlainBlock(
            timestamp_ms=int(raw_block["block_timestamp"]) / 1_000,
            height=raw_block["block_height"],
            hash=raw_block["block_hash"],
            transactions=[transaction["hash"] for transaction in raw_block["transactions"]],
        )

    async def decode_transaction(self, raw_transaction: dict) -> PlainTransaction:
        if raw_transaction["type"] != "user_transaction":
            return self._decode_non_user_transaction(raw_transaction)

        if not raw_transaction["success"]:
            return self._decode_empty_user_transaction(raw_transaction)

        payload = raw_transaction.get("payload")
        function = payload.get("function")

        if self._is_aptos_account_transfer(function):
            return self._decode_aptos_account_transfer(raw_transaction)
        elif self._is_aptos_coin_transfer(function):
            return self._decode_aptos_coin_transfer(raw_transaction)
        else:
            return self._decode_empty_user_transaction(raw_transaction)

    def _decode_aptos_coin_transfer(self, raw_transaction: dict) -> PlainTransaction:
        payload = raw_transaction.get("payload")
        coin_name = payload["type_arguments"][0]
        amount = self._scale_amount(Decimal(payload["arguments"][1]))
        fee = self._get_fee(raw_transaction)

        return PlainTransaction(
            hash=raw_transaction["hash"],
            inputs=[
                PlainInput(
                    address=raw_transaction["sender"],
                    amount=Amount(
                        value=fee,
                        currency_symbol=self.CURRENCY.symbol,
                    ),
                ),
                PlainInput(
                    address=raw_transaction["sender"],
                    amount=Amount(
                        value=amount,
                        currency_symbol=coin_name,
                    ),
                ),
            ],
            outputs=[
                PlainOutput(
                    address=payload["arguments"][0],
                    amount=Amount(
                        value=amount,
                        currency_symbol=coin_name,
                    ),
                )
            ],
            fee=Amount(
                value=fee,
                currency_symbol=self.CURRENCY.symbol,
            ),
        )

    def _decode_aptos_account_transfer(self, raw_transaction: dict) -> PlainTransaction:
        payload = raw_transaction.get("payload")
        amount = self._scale_amount(Decimal(payload["arguments"][1]))
        fee = self._get_fee(raw_transaction)

        return PlainTransaction(
            hash=raw_transaction["hash"],
            inputs=[
                PlainInput(
                    address=raw_transaction["sender"],
                    amount=Amount(
                        value=amount + fee,
                        currency_symbol=self.CURRENCY.symbol,
                    ),
                )
            ],
            outputs=[
                PlainOutput(
                    address=payload["arguments"][0],
                    amount=Amount(
                        value=amount,
                        currency_symbol=self.CURRENCY.symbol,
                    ),
                )
            ],
            fee=Amount(
                value=fee,
                currency_symbol=self.CURRENCY.symbol,
            ),
        )

    def _decode_empty_user_transaction(self, raw_transaction: dict) -> PlainTransaction:
        fee = self._get_fee(raw_transaction)
        return PlainTransaction(
            hash=raw_transaction["hash"],
            inputs=[
                PlainInput(
                    address=raw_transaction["sender"],
                    amount=Amount(
                        value=fee,
                        currency_symbol=self.CURRENCY.symbol,
                    ),
                )
            ],
            outputs=[],
            fee=Amount(
                value=fee,
                currency_symbol=self.CURRENCY.symbol,
            ),
        )

    def _decode_non_user_transaction(self, raw_transaction):
        return PlainTransaction(
            hash=raw_transaction["hash"],
            inputs=[],
            outputs=[],
            fee=Amount(
                value=Decimal(0),
                currency_symbol=self.CURRENCY.symbol,
            ),
        )

    def _scale_amount(self, amount: Decimal) -> Decimal:
        return amount * self.SCALING_FACTOR

    def _get_fee(self, raw_transaction: dict) -> Decimal:
        gas_used = Decimal(raw_transaction["gas_used"])
        gas_price = self._scale_amount(Decimal(raw_transaction["gas_unit_price"]))
        return gas_price * gas_used

    def _is_aptos_account_transfer(self, function_name: str) -> bool:
        return function_name == "0x1::aptos_account::transfer"

    def _is_aptos_coin_transfer(self, function_name: str) -> bool:
        return function_name == "0x1::coin::transfer"
