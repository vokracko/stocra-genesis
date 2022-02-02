class BlockchainException(Exception):
    ...


class NodeNotReady(BlockchainException):
    ...


class BlockDoesNotExist(BlockchainException):
    ...


class AdapterException(Exception):
    ...


class UnknownScriptPubKey(BlockchainException):
    ...
