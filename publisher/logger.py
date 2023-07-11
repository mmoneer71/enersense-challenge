import logging

logger = None


def get_logger() -> logging.Logger:
    global logger
    if not logger:
        logger = logging.getLogger("publisher_logger")
        handler = logging.StreamHandler()
        logger.setLevel(logging.INFO)
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger
