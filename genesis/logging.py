import logging.config

import yaml

with open("logging_config.yaml", encoding="utf-8") as fd:
    logging_config = yaml.safe_load(fd)

logging.config.dictConfig(logging_config)
get_logger = logging.getLogger
logger = logging.getLogger()
