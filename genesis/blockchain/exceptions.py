class NodeException(Exception):
    ...


class NodeNotReady(NodeException):
    ...


class DoesNotExist(NodeException):
    ...


class TooManyRequests(NodeException):
    ...


class Unavailable(NodeException):
    ...


class UnknownNodeException(NodeException):
    ...


class UnknownScriptPubKey(NodeException):
    ...
