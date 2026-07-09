from llm.model import load_model, generate_response
from ingestion.embedding.vector_store import load_vector_store
from retrieval.retriever import retrieve
from retrieval.reranker import load_reranker, rerank
from utils.context_formatter import format_context
from config import LLM_MODEL, RETRIEVAL_K, RERANK_TOP_K, RERANKER_MODEL


class RAGPipeline:

    def __init__(self, db_path=None):
        """
        Load long-term instance variables including tokenizer,
        model and vector_store
        """

        self.tokenizer, self.model = load_model(LLM_MODEL)
        self.vector_store = load_vector_store(db_path)
        self.reranker = load_reranker(RERANKER_MODEL)

    
    def ask(self, question: str, libraries: list[str] | None = None, history: str | None = None):

        """
        Performs retrieval, formats retrieved contents and 
        queries llm to answer user question
        """

        documents = retrieve(vector_store=self.vector_store, query=question, k= RETRIEVAL_K, libraries=libraries)
        reranked_docs = rerank(reranker=self.reranker, query=question, documents=documents, top_k=RERANK_TOP_K)
        context = format_context(reranked_docs)
        llm_response = generate_response(self.tokenizer, self.model, question=question, context=context, history=history)
        
        return {
            "response" : llm_response,
            "documents" : reranked_docs
        }