import logging

import logging518.config

logging518.config.fileConfig("pyproject.toml")
get_logger = logging.getLogger
logger = logging.getLogger()
