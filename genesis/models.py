from decimal import Decimal
from typing import List, Optional

from pydantic import BaseModel, root_validator, validator

from genesis.blockchain_types import BlockchainType
from genesis.encoders import serialize_decimal
from genesis.token_types import TokenType

PlainAddress = str
PlainTransactionHash = str
PlainOutputIndex = int


class PlainTransactionPointer(BaseModel):
    transaction_hash: PlainTransactionHash
    output_index: PlainOutputIndex


class PlainInput(BaseModel):
    address: Optional[PlainAddress] = None
    amount: Optional[Decimal] = None
    transaction_pointer: Optional[PlainTransactionPointer] = None

    class Config:
        json_encoders = {Decimal: serialize_decimal}

    @root_validator
    def validate_address_or_pointer(cls, values) -> None:  # pylint: disable=no-self-argument
        if not (values["address"] or values["transaction_pointer"]):
            raise ValueError("Either address or transaction pointer must be specified")

        return values


class PlainOutput(BaseModel):
    address: PlainAddress
    amount: Decimal

    class Config:
        json_encoders = {Decimal: serialize_decimal}


class PlainTransaction(BaseModel):
    hash: PlainTransactionHash
    inputs: List[PlainInput]
    outputs: List[PlainOutput]
    amount: Decimal
    fee: Decimal
    currency_symbol: str

    class Config:
        json_encoders = {Decimal: serialize_decimal}


class PlainBlock(BaseModel):
    height: int
    hash: str
    timestamp_ms: int
    transactions: List[str] = []

    @validator("timestamp_ms")
    def validate_timestamp_ms(cls, value) -> None:  # pylint: disable=no-self-argument
        # I don't really care if this runs even after 2286
        if len(str(value)) != 13:
            raise ValueError("Timestamp must be in miliseconds")

        return value


class CurrencyInfo(BaseModel):
    symbol: str
    name: str

    class Config:
        frozen = True


class TokenInfo(BaseModel):
    currency: CurrencyInfo
    scaling: Decimal
    type: TokenType

    class Config:
        json_encoders = {Decimal: serialize_decimal}
        frozen = True


class BlockchainInfo(BaseModel):
    name: str
    type: BlockchainType

    class Config:
        frozen = True
