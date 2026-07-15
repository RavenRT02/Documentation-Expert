from ingestion.embedding.vector_store import load_vector_store
from retrieval.reranker import load_reranker, rerank
from retrieval.retriever import retrieve
from config import RERANKER_MODEL, RETRIEVAL_K, BASE_DIR
from langchain_core.documents import Document


output_path = BASE_DIR / "testing" / "compare_retrieval.md"


class RetrievalComparison:

    def __init__(self):
        
        self.vector_store = load_vector_store()
        self.reranker = load_reranker(RERANKER_MODEL)

    def base_retrieval(self, question: str, libraries: list[str] | None = None) -> list[Document]:

        base_context = retrieve(vector_store=self.vector_store, query=question, k=RETRIEVAL_K, libraries=libraries)
        self.base_context = base_context
        return base_context[:5]
    
    def reranked_retrieval(self, question: str) -> list[Document]:

        reranked_context = rerank(self.reranker,query=question, documents=self.base_context, top_k=5)
        return reranked_context
    

questions = [
    "What is RecursiveCharacterTextSplitter and how does it work?",
    "Explain the difference between pandas.merge() and pandas.concat().",
    "How do I create a pathlib.Path object and check whether a file exists?",
    "What is the difference between a Python list and a tuple?",
    "How do I read a CSV file into a Pandas DataFrame?",
    "What is the purpose of RunnableSequence in LangChain?",
    "How can I filter rows in a Pandas DataFrame using multiple conditions?",
    "Explain the difference between os.path and pathlib.",
    "What are Python dictionary comprehensions? Provide an example.",
    "What is the purpose of metadata in LangChain Document objects?"
]

r_pipeline = RetrievalComparison()


for question in questions:
    base_context = r_pipeline.base_retrieval(question=question)
    reranked_context = r_pipeline.reranked_retrieval(question=question)

    with open(output_path, "a", encoding="utf-8") as f:
        f.write(f"# Question\n\n")
        f.write(f"{question}\n\n")

        f.write(f"# Base retrieval\n\n")

        for i, doc in enumerate(base_context, start=1):
            f.write(f"## Rank {i}\n\n")
            f.write("### Content\n\n")
            f.write("```text\n")
            f.write(doc.page_content)
            f.write("\n```\n\n")
        f.write("\n---\n\n")

        f.write(f"# Reranked retrieval\n\n")

        for i, doc in enumerate(reranked_context, start=1):
            f.write(f"## Rank {i}\n\n")
            f.write("### Content\n\n")
            f.write("```text\n")
            f.write(doc.page_content)
            f.write("\n```\n\n")
        f.write("\n---\n\n")


# Clear previous output (optional)
# open("retrieval_results.md", "w").close()