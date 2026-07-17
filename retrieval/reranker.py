from langchain_core.documents import Document
from sentence_transformers import CrossEncoder
from config import RERANK_BATCH_SIZE


def load_reranker(model_name: str) -> CrossEncoder:
    """
    Loads the reranker model
    """
    
    reranker = CrossEncoder(model_name)
    print("Reranker loaded successfully !") 
    return reranker



def rerank(reranker: CrossEncoder, query: str, documents: list[Document], top_k: int) -> list[Document]:
    """
    Uses the reranker model to score similarty of query with
    every provided document content, rerank the documents and 
    return top_k reranked documents
    """

    if not documents:
        return []

    # list of (question, chunk) tuple pairs
    pairs = [
        (query, doc.page_content) for doc in documents
    ]

    # numpy.ndarray , eg : array([ 7.8234, -3.1142,  6.9017], dtype=float32)
    # set show_progress_bar=True for testing if needed.
    # Using batch_size for efficient inference, without batch size it will perform
    # one forward pass for each document, with batching , one pass for batch_size documents.
    scores = reranker.predict(pairs, batch_size=RERANK_BATCH_SIZE, show_progress_bar=False) 

    # Adding rerank_score metadata to chunks
    for doc, score in zip(documents, scores):
        doc.metadata["rerank_score"] = float(score)

    # soreted creates new list , preserves input list[Documents]
    # key -> considers rerank_score metadata for sorting, reverse=True -> Descending order
    sorted_documents = sorted(
        documents,
        key=lambda doc: doc.metadata["rerank_score"],
        reverse=True
    )

    # if there are > top_k slicing handles it and returns all docs
    return sorted_documents[:top_k]