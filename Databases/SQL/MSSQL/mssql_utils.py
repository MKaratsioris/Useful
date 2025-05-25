import logging
import time


# TODO: Add logs in the functionality

# Set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Log to console
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

file_handler = logging.FileHandler("mysql-errors.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)