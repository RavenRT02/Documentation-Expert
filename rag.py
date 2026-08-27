from ingestion.embedding.vector_store import load_vector_store
from retrieval.retriever import retrieve
from retrieval.reranker import load_reranker, rerank
from llm.client import load_llm
from llm.response_prompt import get_system_prompt, get_user_prompt
from llm.conversations import should_summarize, archive_messages, build_history, update_recent_messages
from llm.conversation_summary_prompt import build_conversation_summary_prompt
from llm.query_rewriter import rewrite_query
from utils.formatter import format_context
from utils.greeting import handle_greeting
from utils.message_builder import build_messages
from config import RETRIEVAL_K, RERANK_TOP_K, RERANKER_MODEL, CONTEXT_SUFFICIENCY_THRESHOLD



class RAGPipeline:

    def __init__(self, db_path=None):
        """
        Load long-term instance variables including tokenizer,
        model and vector_store
        """

        self.llm = load_llm()
        self.vector_store = load_vector_store(db_path)
        self.reranker = load_reranker(RERANKER_MODEL)
        self.summaries = []
        self.active_messages = []
        self.recent_messages = []

    
    def reset_conversation(self):
        """
        Clears chat conversation by clearning active_messages
        and summaries
        """

        self.active_messages.clear()
        self.recent_messages.clear()
        self.summaries.clear()

    
    def ask(self, question: str, libraries: list[str] | None = None):

        """
        Performs retrieval, formats retrieved contents and 
        queries llm to answer user question
        """

        # Handle greetings

        greeting = handle_greeting(question=question)

        if greeting is not None:
            return greeting

        # building history - before appending current question so history is does not repeat question in user prompt
        history = build_history(summaries=self.summaries, active_messages=self.active_messages)

        # build recent messages history
        recent_messages = self.recent_messages.copy()

        # query re-writing - handles 1st question without llm call inside rewrite_query 
        retrieval_query = rewrite_query(llm=self.llm, current_question=question, recent_messages=recent_messages)
        
        # Add user question to conversation list
        user_question = {
                            "role" : "user",
                            "content" : question
                        }

        self.active_messages.append(user_question)

        # Use re-written query if history list is not zero
        documents = retrieve(vector_store=self.vector_store, query=retrieval_query, k=RETRIEVAL_K, libraries=libraries)
        reranked_docs = rerank(reranker=self.reranker, query=retrieval_query, documents=documents, top_k=RERANK_TOP_K)

        # Checks if the highest scored chunk has more than 10% relevance to user question.
        # If lower than 10% llm is not called.
        if reranked_docs[0].metadata["rerank_score"] < CONTEXT_SUFFICIENCY_THRESHOLD:

            return {
                "response" : "I do not have sufficient context to answer this question",
                "documents" : reranked_docs
            }


        # Format reranked documents for llm
        context = format_context(reranked_docs)

        # Build messages for response generation
        system_prompt = get_system_prompt()
        user_prompt = get_user_prompt(question=question, context=context, history=history)

        # build messages for llm
        response_messages = build_messages(system_prompt=system_prompt, user_prompt=user_prompt)

        # call llm
        llm_response = self.llm.generate(messages=response_messages)

        # Add llm response to conversation list
        assistant_response = {
                                "role" : "assistant",
                                "content" : llm_response
                             }

        self.active_messages.append(assistant_response)

        # update recent messages list 
        update_recent_messages(recent_messages=self.recent_messages, messages=[user_question, assistant_response])

        # Summarize conversation history 
        if should_summarize(active_messages=self.active_messages):

            # Build messages for summarization
            summary_prompt = build_conversation_summary_prompt(self.active_messages)
            summary_messages = build_messages(system_prompt=summary_prompt)

            # llm call and archiving
            summary = self.llm.generate(messages=summary_messages)
            archive_messages(summaries=self.summaries, active_messages=self.active_messages, summary=summary)
        
        return {
            "response" : llm_response,
            "documents" : reranked_docs
        }