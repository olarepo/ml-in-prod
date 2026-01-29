import logging
import sys
from typing import Optional


def setup_logger(
    name: str,
    level: str = "INFO",
    stream: Optional[object] = None,
) -> logging.Logger:
    """
    Creates a structured, consistent logger for the platform.
    """

    logger = logging.getLogger(name)
    logger.setLevel(level)

    if logger.handlers:
        return logger  # Prevent duplicate handlers

    handler = logging.StreamHandler(stream or sys.stdout)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
