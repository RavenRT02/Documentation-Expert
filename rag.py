from ingestion.embedding.vector_store import load_vector_store
from retrieval.retriever import retrieve
from retrieval.reranker import load_reranker, rerank
from llm.model import load_model, generate_response
from llm.prompt import get_system_prompt, get_user_prompt
from llm.conversations import should_summarize, archive_messages, build_history
from llm.conversation_summary_prompt import build_conversation_summary_prompt
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
        self.summaries = []
        self.active_messages = []

    
    def ask(self, question: str, libraries: list[str] | None = None):

        """
        Performs retrieval, formats retrieved contents and 
        queries llm to answer user question
        """
        
        # Add user question to conversation list
        self.active_messages.append(
            {
                "role" : "user",
                "content" : question
            }
        )

        # Retrieve documents, rerank documents and build conversation history
        documents = retrieve(vector_store=self.vector_store, query=question, k= RETRIEVAL_K, libraries=libraries)
        reranked_docs = rerank(reranker=self.reranker, query=question, documents=documents, top_k=RERANK_TOP_K)
        history = build_history(summaries=self.summaries, active_messages=self.active_messages)

        # Format reranked documents for llm
        context = format_context(reranked_docs)

        # Build messages for response generation
        system_prompt = get_system_prompt()
        user_prompt = get_user_prompt(question=question, context=context, history=history)
        
        response_messages = [
            {
                "role" : "system",
                "content" : system_prompt
            },
            {
                "role" : "user",
                "content" : user_prompt
            }
        ]

        # call llm
        llm_response = generate_response(self.tokenizer, self.model, messages=response_messages)

        # Add llm response to conversation list
        self.active_messages.append(
            {
                "role" : "assistant",
                "content" : llm_response
            }
        )

        # Summarize conversation history 
        if should_summarize(active_messages=self.active_messages):

            # Build messages for summarization
            summary_prompt = build_conversation_summary_prompt(self.active_messages)
            summary_messages = [
                {
                    "role" : "system",
                    "content" : summary_prompt
                }
            ]
            summary = generate_response(self.tokenizer, self.model, messages=summary_messages)
            archive_messages(summaries=self.summaries, active_messages=self.active_messages, summary=summary)
        
        return {
            "response" : llm_response,
            "documents" : reranked_docs
        }