from langchain_huggingface import HuggingFaceEmbeddings
from config import EMBEDDING_MODEL


def load_embeddings():
    """
    Load the embedding model that will be used 
    to convert the knowledge_base chunks into vectors
    """

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        encode_kwargs={"normalize_embeddings":True}
        )
    
    return embeddings