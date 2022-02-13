from decimal import Decimal
from typing import List, Optional

from pydantic import BaseModel, root_validator, validator

PlainAddress = str
PlainTransactionHash = str
PlainOutputIndex = int


class PlainTransactionPointer(BaseModel):
    transaction_hash: PlainTransactionHash
    output_index: PlainOutputIndex


class PlainInput(BaseModel):
    address: Optional[PlainAddress] = None
    transaction_pointer: Optional[PlainTransactionPointer] = None
    amount: Optional[Decimal] = None

    @root_validator
    def validate_address_or_pointer(cls, values) -> None:
        assert values["address"] or values["transaction_pointer"]


class PlainOutput(BaseModel):
    address: PlainAddress
    amount: Decimal


class PlainTransaction(BaseModel):
    hash: PlainTransactionHash
    inputs: List[PlainInput]
    outputs: List[PlainOutput]
    amount: Decimal
    fee: Decimal


class PlainBlock(BaseModel):
    height: int
    hash: str
    timestamp: int
    transactions: List[str] = []

    @validator("timestamp")
    def validate_timestamp(cls, value) -> None:
        # I don't really care if this runs even after 2286
        assert len(str(value)) == 10, "Timestamp must be in seconds"
