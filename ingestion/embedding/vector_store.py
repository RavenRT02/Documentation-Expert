from langchain_core.documents import Document
from langchain_chroma import Chroma
from ingestion.embedding.embedder import load_embeddings
from ingestion.config import VECTOR_DB_PATH, COLLECTION_NAME
import shutil



def build_vector_store(chunks: list[Document]) -> Chroma:
    """
    Function that takes the chunks as argument and uses the embedder to vectorize the chunks.
    Build and persist the Chroma vector store from the provided document chunks.
    """

    # persist_directory → where the database lives on disk
    # collection_name → which collection inside that database

    print("Loading embedding model...")
    embeddings = load_embeddings()
    print("Embedding model loaded.")

    if VECTOR_DB_PATH.exists():
        shutil.rmtree(VECTOR_DB_PATH)     # rmtree -> remove tree - deletes the directory and everything inside it recursively
        VECTOR_DB_PATH.mkdir(parents=True, exist_ok=True)
        print("Deleted existing datastore")

    # take the chunks, use the embeddings to embed them, use persist_directory as the location to save the collection, 
    # and use collection_name as the collection's name
    print(f"Embedding and indexing {len(chunks)} chunks, This may take upto 30 minutes...")
    vector_store = Chroma.from_documents(
        documents=chunks, embedding=embeddings, 
        persist_directory=VECTOR_DB_PATH, collection_name=COLLECTION_NAME
        )
    print(f'vector_store created successfully')

    return vector_store



def load_vector_store() -> Chroma:
    """
    Loads the existing vector store and the corresponding embeddings
    """

    if not VECTOR_DB_PATH.exists():
        raise FileNotFoundError("vector_store not found, build vector_store to use this function")

    embeddings = load_embeddings()

    # using Chrome and not Chroma.from_documents() as we are opening an existing vector_store and not creating a new one
    vector_store = Chroma(persist_directory=VECTOR_DB_PATH, collection_name=COLLECTION_NAME, embedding_function=embeddings)

    return vector_store