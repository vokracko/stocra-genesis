import decimal
import json
from dataclasses import asdict, dataclass, field
from decimal import Decimal
from typing import Any, List, Optional

RedisAddress = str
RedisTransactionHash = str
RedisOutputIndex = int


class DecimalEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)


@dataclass
class RedisTransactionPointer:
    transaction_hash: RedisTransactionHash
    output_index: RedisOutputIndex

    def asdict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, dict_data: Optional[dict]) -> Optional["RedisTransactionPointer"]:
        if not dict_data:
            return None

        return cls(**dict_data)


@dataclass
class RedisInput:
    address: Optional[RedisAddress] = None
    transaction_pointer: Optional[RedisTransactionPointer] = None

    def __post_init__(self) -> None:
        assert self.address or self.transaction_pointer

    def asdict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, dict_data: dict) -> "RedisInput":
        return cls(
            address=dict_data.get("address"),
            transaction_pointer=RedisTransactionPointer.from_dict(dict_data.get("transaction_pointer")),
        )


@dataclass
class RedisOutput:
    address: RedisAddress
    amount: Decimal

    def asdict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, dict_data: dict) -> "RedisOutput":
        return cls(address=dict_data["address"], amount=Decimal(dict_data["amount"]))


@dataclass
class RedisTransaction:
    hash: RedisTransactionHash
    inputs: List[RedisInput]
    outputs: List[RedisOutput]
    amount: Decimal
    fees: Decimal

    def asdict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, dict_data: dict) -> "RedisTransaction":
        dict_data["inputs"] = [RedisInput.from_dict(i) for i in dict_data["inputs"]]
        dict_data["outputs"] = [RedisOutput.from_dict(i) for i in dict_data["outputs"]]
        return cls(**dict_data)


@dataclass
class RedisBlock:
    height: int
    hash: str
    timestamp: int
    transactions: List[RedisTransaction] = field(default_factory=list)

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
    def deserialize(cls, data: str) -> "RedisBlock":
        dict_data = json.loads(data)
        dict_data["transactions"] = [RedisTransaction.from_dict(t) for t in dict_data["transactions"]]
        return cls(**dict_data)

    def serialize(self) -> str:
        return json.dumps(asdict(self), cls=DecimalEncoder)
