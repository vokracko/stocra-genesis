from decimal import Decimal

from genesis.blockchain.ethereum.decoders.decoder import Decoder

TRANSFER_PREFIX = "0xa9059cbb"
ADDRESS_ZEROS = 24
ADDRESS_OFFSET = len(TRANSFER_PREFIX) + ADDRESS_ZEROS
ADDRESS_LENGTH = 74
AMOUNT_OFFSET = ADDRESS_OFFSET + ADDRESS_LENGTH


class ERC20Decoder(Decoder):
    @staticmethod
    def matches(input_data: str) -> bool:
        return input_data.startswith(TRANSFER_PREFIX)

    def get_amount(self) -> Decimal:
        amount_hex = self.input_data[AMOUNT_OFFSET:]
        return Decimal(int(amount_hex, 16))

    def get_output_address(self) -> str:
        address_without_prefix = self.input_data[ADDRESS_OFFSET:ADDRESS_LENGTH]
        return f"0x{address_without_prefix}"
