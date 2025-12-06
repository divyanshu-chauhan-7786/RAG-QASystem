from llama_index.core import SimpleDirectoryReader
import sys
from exception import customexception
from logger import logging

def load_data(data_path="data"):
    """
    Load PDF documents from a specified directory.

    Parameters:
    - data_path (str): The folder path where PDF files exist.

    Returns:
    - A list of loaded PDF documents.
    """
    try:
        logging.info(f"Starting data loading from folder: {data_path}")

        loader = SimpleDirectoryReader(data_path)
        documents = loader.load_data()

        logging.info(f"Data loading completed. Total documents loaded: {len(documents)}")
        return documents

    except Exception as e:
        logging.error("Error occurred during document loading.")
        raise customexception(e, sys)
