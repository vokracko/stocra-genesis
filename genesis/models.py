import json
from dataclasses import asdict, dataclass, field
from decimal import Decimal
from typing import List, Optional

from genesis.encoders import DecimalEncoder

PlainAddress = str
PlainTransactionHash = str
PlainOutputIndex = int


@dataclass
class PlainTransactionPointer:
    transaction_hash: PlainTransactionHash
    output_index: PlainOutputIndex

    def asdict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, dict_data: Optional[dict]) -> Optional["PlainTransactionPointer"]:
        if not dict_data:
            return None

        return cls(**dict_data)


@dataclass
class PlainInput:
    address: Optional[PlainAddress] = None
    transaction_pointer: Optional[PlainTransactionPointer] = None
    amount: Optional[Decimal] = None

    def __post_init__(self) -> None:
        assert self.address or self.transaction_pointer

    def asdict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, dict_data: dict) -> "PlainInput":
        return cls(
            address=dict_data.get("address"),
            transaction_pointer=PlainTransactionPointer.from_dict(dict_data.get("transaction_pointer")),
        )


@dataclass
class PlainOutput:
    address: PlainAddress
    amount: Decimal

    def asdict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, dict_data: dict) -> "PlainOutput":
        return cls(address=dict_data["address"], amount=Decimal(dict_data["amount"]))


@dataclass
class PlainTransaction:
    hash: PlainTransactionHash
    inputs: List[PlainInput]
    outputs: List[PlainOutput]
    amount: Decimal
    fees: Decimal

    def asdict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, dict_data: dict) -> "PlainTransaction":
        dict_data["inputs"] = [PlainInput.from_dict(i) for i in dict_data["inputs"]]
        dict_data["outputs"] = [PlainOutput.from_dict(i) for i in dict_data["outputs"]]
        return cls(**dict_data)


@dataclass
class PlainBlock:
    height: int
    hash: str
    timestamp: int
    transactions: List[PlainTransaction] = field(default_factory=list)

    def __post_init__(self) -> None:
        # I don't really care if this runs even after 2286
        assert len(str(self.timestamp)) == 10, "Timestamp must be in seconds"
        self.height = int(self.height)
        self.timestamp = int(self.timestamp)

    def asdict(self, exclude: Optional[list] = None) -> dict:
        data_dict = asdict(self)

        if exclude is not None:
            for key in exclude:
                del data_dict[key]

        return data_dict

    @classmethod
    def deserialize(cls, data: str) -> "PlainBlock":
        dict_data = json.loads(data)
        dict_data["transactions"] = [PlainTransaction.from_dict(t) for t in dict_data["transactions"]]
        return cls(**dict_data)

    def serialize(self) -> str:
        return json.dumps(asdict(self), cls=DecimalEncoder)
