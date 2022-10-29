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


class SkippedBlock(NodeException):
    """
    In POS blockchain there might be a gap between blocks
    where a particular number of sequence might be missing
    """

    ...


class UnknownNodeException(NodeException):
    ...


class UnknownScriptPubKey(NodeException):
    ...
