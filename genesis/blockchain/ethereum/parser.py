from decimal import Decimal
from typing import ClassVar, Dict, List

from genesis.blockchain.ethereum.adapter import EthereumNodeAdapter
from genesis.blockchain.ethereum.decoders.decoder import Decoder
from genesis.blockchain.ethereum.decoders.erc20 import ERC20Decoder
from genesis.blockchain.ethereum.tokens import TOKENS
from genesis.blockchain.parser import Parser
from genesis.blockchains import Blockchain
from genesis.currencies import Currency
from genesis.logging import get_logger
from genesis.models import Amount, PlainBlock, PlainInput, PlainOutput, PlainTransaction

logger = get_logger(__name__)


class EthereumParser(Parser):
    BLOCKCHAIN = Blockchain.ETHEREUM
    CURRENCY: ClassVar[Currency] = Currency.ETHER
    node_adapter: EthereumNodeAdapter

    TOKENS: ClassVar[Dict] = TOKENS
    SCALING_FACTOR = Decimal("1e-18")
    DECODERS: List[Decoder] = [
        ERC20Decoder,
    ]

    def __init__(self, node_adapter: EthereumNodeAdapter) -> None:
        super().__init__(node_adapter)

    async def decode_block(self, raw_block: dict) -> PlainBlock:
        return PlainBlock(
            height=int(raw_block["number"], 16),
            hash=raw_block["hash"],
            timestamp_ms=int(raw_block["timestamp"], 16) * 1_000,
            transactions=raw_block["transactions"],
        )

    async def decode_transaction(self, raw_transaction: dict) -> PlainTransaction:
        receipt = await self.node_adapter.get_transaction_receipt(raw_transaction["hash"])
        fee_amount = self._get_fee_amount(receipt)
        was_successful = self._was_transaction_successful(receipt)
        input_data = raw_transaction["input"]
        inputs = []
        outputs = []

        for decoder in self.DECODERS:
            if decoder.matches(input_data):
                currency_symbol = raw_transaction["to"] or receipt["contractAddress"]
                output_address = decoder.get_output_address(input_data)
                amount_token = Amount(
                    value=decoder.get_amount(input_data),
                    currency_symbol=currency_symbol,
                )
                inputs.append(
                    PlainInput(
                        address=raw_transaction["from"],
                        amount=fee_amount,
                    )
                )

                if was_successful:
                    inputs.append(
                        PlainInput(
                            address=raw_transaction["from"],
                            amount=amount_token,
                        )
                    )
                    outputs.append(
                        PlainOutput(
                            address=output_address,
                            amount=amount_token,
                        )
                    )
                break
        else:
            currency_symbol = self.CURRENCY.symbol
            output_address = raw_transaction["to"]
            output_amount = Amount(
                value=Decimal(int(raw_transaction["value"], 16)) * self.SCALING_FACTOR,
                currency_symbol=currency_symbol,
            )
            inputs = [
                (
                    PlainInput(
                        address=raw_transaction["from"],
                        amount=output_amount + fee_amount if was_successful else fee_amount,
                    )
                )
            ]

            if was_successful:
                outputs = [
                    PlainOutput(
                        address=output_address,
                        amount=output_amount,
                    )
                ]

        return PlainTransaction(
            hash=raw_transaction["hash"],
            inputs=inputs,
            outputs=outputs,
            fee=fee_amount,
        )

    def _get_fee_amount(self, receipt) -> Amount:
        gas_used = self._parse_gas_used(receipt)
        gas_price = self._parse_gas_price(receipt)
        return Amount(
            value=gas_used * gas_price * self.SCALING_FACTOR,
            currency_symbol=self.CURRENCY.symbol,
        )

    def _parse_gas_used(self, raw_receipt: dict) -> Decimal:
        gas_used_hex = raw_receipt["gasUsed"]
        return Decimal(int(gas_used_hex, 16))

    def _parse_gas_price(self, raw_receipt: dict) -> Decimal:
        return Decimal(int(raw_receipt["effectiveGasPrice"], 16))

    def _was_transaction_successful(self, raw_receipt: dict) -> bool:
        return raw_receipt["status"] == "0x1"
