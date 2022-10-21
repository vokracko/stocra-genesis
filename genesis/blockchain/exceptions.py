class NodeException(Exception):
    ...


class DoesNotExist(NodeException):
    ...


class Unavailable(NodeException):
    ...


class NodeNotReady(Unavailable):
    ...


class TooManyRequests(Unavailable):
    ...


class UnableToLoadDataFromStorage(NodeException):
    ...


class UnknownNodeException(NodeException):
    ...


class UnknownScriptPubKey(NodeException):
    ...
