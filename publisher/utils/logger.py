import logging


def get_logger(logger_name: str) -> logging.Logger:
    logger = logging.getLogger(logger_name)
    handler = logging.StreamHandler()
    logger.setLevel(logging.INFO)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
