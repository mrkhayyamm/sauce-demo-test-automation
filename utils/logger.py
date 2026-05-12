import logging
import os


def get_logger():

    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("saucedemo")

    logger.setLevel(logging.INFO)

    # Aynı handler tekrar eklenmesin
    if logger.hasHandlers():
        logger.handlers.clear()

    # FILE HANDLER
    file_handler = logging.FileHandler(
        "logs/test.log",
        encoding="utf-8"
    )

    # CONSOLE HANDLER
    console_handler = logging.StreamHandler()

    # FORMAT
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger