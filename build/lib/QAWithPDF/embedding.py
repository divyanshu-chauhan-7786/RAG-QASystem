import sys
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.settings import Settings
from logger import logging
from exception import customexception


def create_or_load_index(model, documents, persist_dir: str = "./storage"):
    """
    Creates a vector index using HuggingFace Embeddings or loads an existing one.
    
    Args:
        model: The Gemini LLM model instance.
        documents: List of Document objects to index.
        persist_dir (str): Path to save/load index.

    Returns:
        query_engine: A LlamaIndex QueryEngine instance.
    """
    try:
        logging.info("Checking if index already exists...")

        # --- Try loading existing index first ---
        storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
        index = load_index_from_storage(storage_context)

        logging.info("Existing index found and loaded successfully.")
        return index.as_query_engine()

    except Exception:
        logging.warning("No existing index found. Creating new index...")

        try:
            # Load HuggingFace embedding model (Free + Unlimited)
            logging.info("Initializing HuggingFace Embedding Model...")
            embed_model = HuggingFaceEmbedding("sentence-transformers/all-MiniLM-L6-v2")

            # Apply global settings
            Settings.llm = model
            Settings.embed_model = embed_model
            Settings.chunk_size = 1000
            Settings.chunk_overlap = 20

            # Create new index from documents
            logging.info("Building new index from documents...")
            index = VectorStoreIndex.from_documents(documents)

            # Save index for reuse
            logging.info("Saving index to storage...")
            index.storage_context.persist(persist_dir)

            logging.info("Index created and saved successfully.")
            return index.as_query_engine()

        except Exception as e:
            raise customexception(e, sys)
