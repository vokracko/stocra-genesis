import hashlib
import json
from decimal import Decimal
from typing import ClassVar, List, cast

import base58
import logging518 as logging

from genesis.blockchain.bitcoin.adapter import BitcoinNodeAdapter
from genesis.blockchain.exceptions import UnknownScriptPubKey
from genesis.blockchain.parser import Parser
from genesis.blockchains import Blockchain
from genesis.currencies import Currency
from genesis.models import (
    Amount,
    PlainAddress,
    PlainBlock,
    PlainInput,
    PlainOutput,
    PlainTransaction,
    PlainTransactionPointer,
)

logger = logging.get_logger(__name__)


class BitcoinParser(Parser):
    BLOCKCHAIN: ClassVar[Blockchain] = Blockchain.BITCOIN
    CURRENCY: ClassVar[Currency] = Currency.BITCOIN
    node_adapter: BitcoinNodeAdapter

    def __init__(self, node_adapter: BitcoinNodeAdapter) -> None:
        super().__init__(node_adapter)

    async def decode_block(self, raw_block: dict) -> PlainBlock:
        return PlainBlock(
            height=raw_block["height"],
            hash=raw_block["hash"],
            timestamp_ms=raw_block["time"] * 1_000,
            transactions=raw_block["tx"],
        )

    async def decode_transaction_without_inputs(self, raw_transaction: dict) -> PlainTransaction:
        fee = Decimal("0")
        outputs = await self._get_outputs_with_amounts_from_raw_transaction(raw_transaction)
        transaction_hash = raw_transaction["txid"]

        return PlainTransaction(
            hash=transaction_hash,
            inputs=[],
            outputs=outputs,
            fee=Amount(
                value=fee,
                currency_symbol=self.CURRENCY.symbol,
            ),
        )

    async def decode_transaction(self, raw_transaction: dict) -> PlainTransaction:
        transaction = await self.decode_transaction_without_inputs(raw_transaction)
        is_coinbase_transaction = self._is_coinbase_transaction(raw_transaction)
        if is_coinbase_transaction:
            inputs = []
        else:
            inputs = await self._get_decoded_inputs_from_raw_transaction(raw_transaction)
            sum_of_inputs = sum([input_.amount.value for input_ in inputs])
            sum_of_outputs = sum([output.amount.value for output in transaction.outputs])
            transaction.fee = Amount(value=sum_of_inputs - sum_of_outputs, currency_symbol=self.CURRENCY.symbol)

        transaction.inputs = inputs
        return transaction

    async def _get_decoded_inputs_from_raw_transaction(self, raw_transaction: dict) -> List[PlainInput]:
        input_transactions = []
        inputs = []
        transaction_pointers = {vin["txid"]: vin["vout"] for vin in raw_transaction["vin"]}

        async for input_transaction in await self.node_adapter.get_transactions(transaction_pointers.keys()):
            input_transactions.append(input_transaction)

        transactions_sorted = sorted(input_transactions, key=lambda item: item["id"])

        for (transaction_pointer_txid, transaction_pointer_vout), transaction in zip(
            transaction_pointers.items(), transactions_sorted
        ):
            decoded_input_transaction = await self.decode_transaction_without_inputs(transaction["result"])
            input_ = PlainInput(
                address=decoded_input_transaction.outputs[transaction_pointer_vout].address,
                amount=decoded_input_transaction.outputs[transaction_pointer_vout].amount,
                transaction_pointer=PlainTransactionPointer(
                    transaction_hash=transaction_pointer_txid,
                    output_index=transaction_pointer_vout,
                ),
            )
            inputs.append(input_)
        return inputs

    async def _get_outputs_with_amounts_from_raw_transaction(self, raw_transaction: dict) -> List[PlainOutput]:
        results = []

        for vout in raw_transaction["vout"]:
            script_pub_key = vout["scriptPubKey"]
            if script_pub_key.get("address"):
                address = PlainAddress(script_pub_key["address"])
            else:
                try:
                    address = await self._decode_address_from_script_pub_key(script_pub_key)
                except UnknownScriptPubKey:
                    logger.error("raw transaction: %s", json.dumps(raw_transaction, indent=4))
                    raise

            output = PlainOutput(
                address=address,
                amount=Amount(
                    value=Decimal(str(vout["value"])),
                    currency_symbol=self.CURRENCY.symbol,
                ),
            )
            results.append(output)

        return results

    def _get_total_amount_from_raw_transaction(self, outputs: List[PlainOutput]) -> Decimal:
        return sum([output.amount.value for output in outputs], start=Decimal("0"))

    def _is_coinbase_transaction(self, raw_transaction: dict) -> bool:
        vin = raw_transaction["vin"]
        return len(vin) == 1 and vin[0].get("coinbase") is not None

    async def _decode_address_from_script_pub_key(self, script_pub_key: dict) -> str:
        addresses = script_pub_key.get("addresses", [])

        if len(addresses) == 1:
            return addresses[0]

        script_type = script_pub_key["type"]

        if script_type == "nonstandard":
            return "nonstandard"
        elif script_type == "nulldata":
            return "null"
        elif script_type == "pubkey":
            return self._p2shpubkey_to_address(script_pub_key["asm"].split(" ")[0])
        elif script_type == "multisig":
            result = await self.node_adapter.decode_script(script_pub_key["hex"])
            assert set(result.keys()).issubset({"asm", "type", "p2sh", "segwit"}), f"keys are {result.keys()}"
            return cast(str, result["p2sh"])

        raise UnknownScriptPubKey(script_type)

    def _p2shpubkey_to_address(self, p2sh_pubkey: str) -> str:
        step_1 = hashlib.sha256(bytes.fromhex(p2sh_pubkey)).digest()
        step_2 = hashlib.new("ripemd160", step_1).digest()
        step_3 = bytes.fromhex("00") + step_2
        step_4 = hashlib.sha256(step_3).digest()
        step_5 = hashlib.sha256(step_4).digest()
        step_6 = step_5[:4]  # first 4 bytes
        step_7 = step_3 + step_6
        step_8 = base58.b58encode(step_7)
        return step_8.decode()
