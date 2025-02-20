from src.components.data_ingestion import DataIngestion
from src.logger import logging
from src.exception import CUSTOM_EXCEPTION
import sys

if __name__ == "__main__":
    logging.info("Starting the application")
    logging.info("Application started successfully")

    try:
        x = data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

        
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        logging.error(f"An error occurred: {CUSTOM_EXCEPTION}")
        raise CUSTOM_EXCEPTION(e, sys)
