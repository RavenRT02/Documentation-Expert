from llm.model import load_model, generate_response
from ingestion.embedding.vector_store import load_vector_store
from retrieval.retriever import retrieve
from utils.context_formatter import format_context
from config import LLM_MODEL, RETRIEVAL_K


class RAGPipeline:

    def __init__(self, db_path=None):
        """
        Load long-term instance variables including tokenizer,
        model and vector_store
        """

        self.tokenizer, self.model = load_model(LLM_MODEL)
        self.vector_store = load_vector_store(db_path)

    
    def ask(self, question: str, libraries: list[str] | None = None, history: str | None = None):

        """
        Performs retrieval, formats retrieved contents and 
        queries llm to answer user question
        """

        documents = retrieve(vector_store=self.vector_store, query=question, K= RETRIEVAL_K, libraries=libraries)
        context = format_context(documents)
        llm_response = generate_response(self.tokenizer, self.model, question=question, context=context, history=history)
        
        return {
            "response" : llm_response,
            "documents" : documents
        }