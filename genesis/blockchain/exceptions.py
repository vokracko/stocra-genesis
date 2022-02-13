class NodeException(Exception):
    ...


class NodeNotReady(NodeException):
    ...


class DoesNotExist(NodeException):
    ...


class TransactionDoesNotExists(NodeException):
    ...


class TooManyRequests(NodeException):
    ...


class Unavailable(NodeException):
    ...


class InvalidHash(NodeException):
    ...


class UnknownNodeException(NodeException):
    ...


class UnknownScriptPubKey(NodeException):
    ...
