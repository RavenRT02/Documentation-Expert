# script that creates the vector database , run in terminal to create a vector_store
# run with "python -m ingestion.build_vector_store in terminal"
# vector_store will be created inside vector_store folder
# Initial encoder model loadin will take time, it is not silently failing or lagging.
# Embedding for 12894 chunks took ~30mins , again no lag or fail, takes time , no progress bar.

from ingestion.chunking.chunker import chunk_documents
from ingestion.embedding.vector_store import build_vector_store

def main():

    chunks = chunk_documents()
    build_vector_store(chunks)


if __name__ == '__main__':
    main()