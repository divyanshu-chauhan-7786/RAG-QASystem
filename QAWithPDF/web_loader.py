import requests
from bs4 import BeautifulSoup
from llama_index.core import Document
from logger import logging
from exception import customexception
import sys

def load_website(url: str):
    try:
        logging.info(f"Fetching website: {url}")

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                "AppleWebKit/537.36 (KHTML, like Gecko)"
                "Chrome/122.0.0.0 Safari/537.36"
            )
        }

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Remove unnecessary HTML noise
        for element in soup(["script", "style", "nav", "footer", "header"]):
            element.extract()

        text = soup.get_text(separator="\n", strip=True)

        # Clean unwanted short lines (<3 chars)
        cleaned_text = "\n".join([line for line in text.split("\n") if len(line) > 3])

        return [Document(text=cleaned_text, extra_info={"url": url})]

    except Exception as e:
        raise customexception(e, sys)
