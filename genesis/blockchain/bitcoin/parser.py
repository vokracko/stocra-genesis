import hashlib
import json
from decimal import Decimal
from typing import ClassVar, List, cast

import base58
import logging518 as logging

from genesis.blockchain.bitcoin.adapter import BitcoinNodeAdapter
from genesis.blockchain.exceptions import UnknownScriptPubKey
from genesis.blockchain.parser import Parser
from genesis.constants import BlockchainName
from genesis.models import (
    PlainAddress,
    PlainBlock,
    PlainInput,
    PlainOutput,
    PlainTransaction,
    PlainTransactionPointer,
)
from genesis.profiling import log_duration

logger = logging.get_logger(__name__)


class BitcoinParser(Parser):
    BLOCKCHAIN: ClassVar[BlockchainName] = BlockchainName.BITCOIN
    node_adapter: BitcoinNodeAdapter

    def __init__(self, node_adapter: BitcoinNodeAdapter) -> None:
        super().__init__(node_adapter)

    async def decode_block(self, raw_block: dict) -> PlainBlock:
        transactions = await self.decode_transactions(raw_block)
        return PlainBlock(
            height=raw_block["height"],
            hash=raw_block["hash"],
            timestamp=raw_block["time"],
            transactions=raw_block["tx"],
        )

    async def decode_transactions(self, raw_block: dict) -> List[str]:
        return raw_block["tx"]
        # transactions = []
        # transaction_count = raw_block["nTx"]
        #
        # for index, raw_transaction in enumerate(raw_block["tx"], start=1):
        #     if isinstance(raw_transaction, str):
        #         transactions.append(raw_transaction)
        #
        #     logger.debug("Decoding transaction %s/%s: %s", index, transaction_count, raw_transaction["hash"])
        #     transaction = await self.decode_transaction(raw_transaction)
        #     logger.debug("Transaction decoded %s/%s: %s", index, transaction_count, transaction.hash)
        #     transactions.append(transaction)
        #
        # return transactions

    async def decode_transaction(self, raw_transaction: dict) -> PlainTransaction:
        is_coinbase_transaction = await self._is_coinbase_transaction(raw_transaction)
        if is_coinbase_transaction:
            inputs = []
            fee = Decimal("0")
        else:
            inputs = await self.get_inputs_from_raw_transaction(raw_transaction)
            fee = await self.get_fee_from_raw_transaction(raw_transaction)

        outputs = await self.get_outputs_with_amounts_from_raw_transaction(raw_transaction)
        amount = await self.get_total_amount_from_raw_transaction(raw_transaction)
        transaction_hash = raw_transaction["txid"]

        return PlainTransaction(hash=transaction_hash, inputs=inputs, outputs=outputs, amount=amount, fee=fee)

    async def get_inputs_from_raw_transaction(self, raw_transaction: dict) -> List[PlainInput]:
        results = []

        for vin in raw_transaction["vin"]:
            transaction_input = PlainInput(
                transaction_pointer=PlainTransactionPointer(
                    transaction_hash=vin["txid"],
                    output_index=vin["vout"],
                )
            )
            results.append(transaction_input)

        return results

    async def get_outputs_with_amounts_from_raw_transaction(self, raw_transaction: dict) -> List[PlainOutput]:
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
                amount=Decimal(vout["value"]),
            )
            results.append(output)

        return results

    async def get_total_amount_from_raw_transaction(self, raw_transaction: dict) -> Decimal:
        return sum([Decimal(vout["value"]) for vout in raw_transaction["vout"]], start=Decimal(0))

    async def get_fee_from_raw_transaction(self, raw_transaction: dict) -> Decimal:
        return Decimal(raw_transaction["fee"])

    async def _is_coinbase_transaction(self, raw_transaction: dict) -> bool:
        vin = raw_transaction["vin"]
        return len(vin) == 1 and vin[0].get("coinbase") is not None

    async def _decode_address_from_script_pub_key(self, script_pub_key: dict) -> str:
        script_type = script_pub_key["type"]

        if script_type == "nonstandard":
            return "nonstandard"
        elif script_type == "nulldata":
            return "null"
        elif script_type == "pubkey":
            return await self._p2shpubkey_to_address(script_pub_key["asm"].split(" ")[0])
        elif script_type == "multisig":
            with log_duration("Decode script"):
                result = await self.node_adapter.decode_script(script_pub_key["hex"])
                assert set(result.keys()).issubset({"asm", "type", "p2sh", "segwit"}), f"keys are {result.keys()}"
                return cast(str, result["p2sh"])

        raise UnknownScriptPubKey(script_type)

    async def _p2shpubkey_to_address(self, p2sh_pubkey: str) -> str:
        step_1 = hashlib.sha256(bytes.fromhex(p2sh_pubkey)).digest()
        step_2 = hashlib.new("ripemd160", step_1).digest()
        step_3 = bytes.fromhex("00") + step_2
        step_4 = hashlib.sha256(step_3).digest()
        step_5 = hashlib.sha256(step_4).digest()
        step_6 = step_5[:4]  # first 4 bytes
        step_7 = step_3 + step_6
        step_8 = base58.b58encode(step_7)
        return step_8.decode()