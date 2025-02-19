from src.logger import logging
from src.exception import CUSTOM_EXCEPTION
import sys

if __name__ == "__main__":
    logging.info("Starting the application")
    logging.info("Application started successfully")

    try:
        x = 1/0
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        logging.error(f"An error occurred: {CUSTOM_EXCEPTION}")
        raise CUSTOM_EXCEPTION(e, sys)
