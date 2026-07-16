from pathlib import Path

# Chunk details

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 159


# Splitter details

# used for chunking - "Whenever you see these Markdown headers, treat them as document boundaries and keep track of them."
# we store these as metadata (h1-python guide, h2-functions,etc) to find chunk source.
HEADERS_TO_SPLIT_ON = [
    ("#", "h1"),
    ("##", "h2"),
    ("###", "h3"),
]


# Path details

BASE_DIR = Path(__file__).resolve().parent
KB_PATH = BASE_DIR / "knowledge_base"
VECTOR_DB_PATH = BASE_DIR / "vector_store" / "chroma_db"


# Models

EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"
LLM_MODEL = "Qwen/Qwen2.5-7B-Instruct"
RERANKER_MODEL = "BAAI/bge-reranker-base"


# vector store

COLLECTION_NAME = "documentation_expert"


# Generation defaults

MAX_NEW_TOKENS = 512


# Retrieval

RETRIEVAL_K = 15
RERANK_TOP_K = 7


# Reranker batch size
# batch_size is set to 16 by convention , usually powers of 2 (8,16,32,64...)

RERANK_BATCH_SIZE = 16


# Role labels for history formatter

ROLE_LABELS = {
    "user" : "User",
    "assistant" : "Assistant",
    "summary" : "Conversation Summary"
}


# Turns before summarizing ( 1 turn - user quesstion + assistant response )

CONVERSATION_SUMMARY_TURNS = 10


# Threashold to be met for the context to reach llm

CONTEXT_SUFFICIENCY_THRESHOLD = 0.10