import os
from dotenv import load_dotenv
import sys

from llama_index.llms.gemini import Gemini
import google.generativeai as genai

from exception import customexception
from logger import logging


# Load Environment Variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Google Generative AI
genai.configure(api_key=GOOGLE_API_KEY)


def load_model():
    """
    Loads the selected Gemini model for NLP/Chat operations.

    Returns:
        Gemini: An instance of Gemini configured with the selected model.
    """
    try:
        logging.info("Initializing Gemini LLM model...")

        # Your selected working model
        model = Gemini(
            model="models/gemini-2.5-flash",
            api_key=GOOGLE_API_KEY
        )

        logging.info("Gemini model loaded successfully.")
        return model

    except Exception as e:
        raise customexception(e, sys)
