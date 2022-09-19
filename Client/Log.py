import logging
import logging.handlers
from pathlib import Path

from Constants import LOG_DIR


def create_logger(log_location: Path, logger_name: str, file_name: str):
    log = logging.getLogger(logger_name)
    log.setLevel(logging.DEBUG)
    rotating_fhandler = logging.handlers.RotatingFileHandler(
        filename=log_location / file_name, maxBytes=10 * 1024 * 1024, backupCount=10
    )
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s : %(message)s"
    )
    rotating_fhandler.setFormatter(formatter)
    log.addHandler(rotating_fhandler)
    return log


APP_LOGGER = create_logger(log_location=LOG_DIR, logger_name="APP", file_name="app.log")
