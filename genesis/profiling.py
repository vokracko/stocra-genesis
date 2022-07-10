import timeit
from contextlib import contextmanager
from typing import Generator

from genesis.logging import logger


@contextmanager
def log_duration(name: str) -> Generator:
    start_time = timeit.default_timer()
    try:
        yield
    finally:
        elapsed_seconds = timeit.default_timer() - start_time
        logger.info("%s: elapsed seconds: %.10f", name, elapsed_seconds)
