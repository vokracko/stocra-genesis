INPUT_ERC20_TRANSFER_PREFIX = "0xa9059cbb"
INPUT_ERC20_ADDRESS_ZEROS = 24
INPUT_ERC20_ADDRESS_OFFSET = len(INPUT_ERC20_TRANSFER_PREFIX) + INPUT_ERC20_ADDRESS_ZEROS
INPUT_ERC20_ADDRESS_LENGTH = 74
INPUT_ERC20_AMOUNT_OFFSET = INPUT_ERC20_ADDRESS_OFFSET + INPUT_ERC20_ADDRESS_LENGTH