import timeit
from contextlib import contextmanager
from typing import Generator

import logging518 as logging


@contextmanager
def log_duration(name: str) -> Generator:
    start_time = timeit.default_timer()
    try:
        yield
    finally:
        elapsed_seconds = timeit.default_timer() - start_time
        logging.logger.info("%s: elapsed seconds: %s", name, elapsed_seconds)
