from decimal import Decimal


class Decoder:
    @staticmethod
    async def matches(input_data: str) -> bool:
        raise NotImplementedError

    @staticmethod
    async def get_amount(input_data: str) -> Decimal:
        raise NotImplementedError

    @staticmethod
    async def get_output_address(input_data: str) -> str:
        raise NotImplementedError
