from decimal import Decimal


class Decoder:
    input_data: str

    def __init__(self, input_data: str):
        self.input_data = input_data

    @staticmethod
    def matches(input_data: str) -> bool:
        raise NotImplementedError

    def get_amount(self) -> Decimal:
        raise NotImplementedError

    def get_output_address(self) -> str:
        raise NotImplementedError
