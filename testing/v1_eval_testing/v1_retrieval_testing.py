from langchain_core.documents import Document
from config import BASE_DIR, RETRIEVAL_K, RERANK_TOP_K, RERANKER_MODEL
from ingestion.embedding.vector_store import load_vector_store
from retrieval.retriever import retrieve
from retrieval.reranker import load_reranker, rerank


# Initial test data path
# OUTPUT_PATH = BASE_DIR / "testing" / "v1_eval_testing" / "reports" / "retrieval_eval.md"

# Intense test data path
OUTPUT_PATH = BASE_DIR / "testing" / "v1_eval_testing" / "reports" / "retrieval_intense_eval.md"


# 1. Valid documentation questions (should retrieve good context)
DOCUMENTATION_QUESTIONS = [
    "What is RecursiveCharacterTextSplitter and how does it work?",
    "How do I read a CSV file into a Pandas DataFrame?",
    "What is the purpose of RunnableSequence in LangChain?",
]

# 2. Out-of-domain questions (should retrieve little or no useful context)
OUT_OF_DOMAIN_QUESTIONS = [
    "Hi",
    "Hello",
    "How are you?",
    "Who won the FIFA World Cup?",
    "How do I crack coding interviews?",
    "What is the capital of France?",
]

# 3. Ambiguous questions
AMBIGUOUS_QUESTIONS = [
    "How do I create a path?",
    "How do I merge data?",
    "What is metadata?",
]

# 4. Cross-library questions
CROSS_LIBRARY_QUESTIONS = [
    "How do pathlib.Path and os.path differ?",
    "How can I use Pandas with pathlib?",
]

# Initial test questions
# QUESTIONS = (DOCUMENTATION_QUESTIONS + OUT_OF_DOMAIN_QUESTIONS + AMBIGUOUS_QUESTIONS + CROSS_LIBRARY_QUESTIONS)


# Intesensive test questions
QUESTIONS = [
    # ---------------------------
    # Valid documentation questions (10)
    # ---------------------------
    "How do I read a CSV file into a pandas DataFrame?",
    "How can I select multiple columns from a pandas DataFrame?",
    "What is the difference between loc and iloc in pandas?",
    "How do I merge two DataFrames on a common column in pandas?",
    "How can I remove duplicate rows from a pandas DataFrame?",
    "How do I create a virtual environment in Python?",
    "What is the difference between a list and a tuple in Python?",
    "How do I define a function with default arguments in Python?",
    "How do I create a simple LangChain prompt template?",
    "How can I split text into chunks before indexing with LangChain?",

    # ---------------------------
    # Ambiguous documentation questions (10)
    # ---------------------------
    "How do I load my data?",
    "How can I improve performance?",
    "What's the recommended way to process large datasets?",
    "Why is my DataFrame operation so slow?",
    "How should I organize my Python project?",
    "How do I connect my LLM?",
    "Why isn't my chain working?",
    "How do I save the results?",
    "What's the best way to filter data?",
    "How do I handle missing values?",

    # ---------------------------
    # Completely unrelated questions (10)
    # ---------------------------
    "What's the capital of France?",
    "Who won the FIFA World Cup in 2022?",
    "How do I bake sourdough bread?",
    "What's the best way to train for a marathon?",
    "How does photosynthesis work?",
    "Recommend some good sci-fi movies.",
    "What's the weather like in Tokyo today?",
    "How do I change a flat tire on a bicycle?",
    "Who painted the Mona Lisa?",
    "What's the difference between coffee and espresso?",

    # ---------------------------
    # Greetings (10)
    # ---------------------------
    "Hi",
    "Hello",
    "Hey there!",
    "Good morning",
    "Good afternoon",
    "Good evening",
    "How are you?",
    "Nice to meet you!",
    "What's up?",
    "Can you help me?",

    # ---------------------------
    # Coding questions outside supported libraries (10)
    # ---------------------------
    "How do I create a REST API using Express.js?",
    "How do I build a React component with hooks?",
    "How do I write a SQL query to find duplicate records?",
    "How do I configure authentication in Spring Boot?",
    "How do I build a Flutter app with navigation?",
    "How do I create an ASP.NET Core Web API?",
    "How do I use TensorFlow.js for image classification?",
    "How do I create a Docker Compose file for multiple services?",
    "How do I build a responsive layout using Tailwind CSS?",
    "How do I write a recursive function in Rust?",

    # ---------------------------
    # General knowledge questions (10)
    # ---------------------------
    "What are the 7 wonders of the world ?",
    "How many countries are there in the world ?",
    "Why is the sky blue?",
    "What causes earthquakes?",
    "How does GPS determine your location?",
    "What is quantum computing?",
    "Why do leap years exist?",
    "What is the fastest animal in earth ?",
    "What are black holes?",
    "What is the difference between renewable and non-renewable energy sources?"
]


class RetrievalEvaluator:

    def __init__(self):

        self.vector_store = load_vector_store()
        self.reranker = load_reranker(RERANKER_MODEL)

    def retrieve_documents(self, question: str, libraries: list[str] | None = None) -> list[Document]:

        return retrieve(vector_store=self.vector_store, query=question, k=RETRIEVAL_K, libraries=libraries)

    def rerank_documents(self, question: str, documents: list[Document]) -> list[Document]:

        return rerank(reranker=self.reranker, query=question, documents=documents, top_k=RERANK_TOP_K,)


def write_document(file, rank: int, document: Document):

    metadata = document.metadata

    file.write(f"## Rank {rank}\n\n")

    file.write("| Field | Value |\n")
    file.write("|------|-------|\n")

    file.write(f"| Library | {metadata.get('library', '-') } |\n")
    file.write(f"| Module | {metadata.get('module', '-') } |\n")
    file.write(f"| Section | {metadata.get('section', '-') } |\n")
    file.write(f"| Source | {metadata.get('source', '-') } |\n")
    file.write(f"| Chunk ID | {metadata.get('chunk_id', '-') } |\n")

    if "rerank_score" in metadata:
        file.write(f"| Rerank Score | {metadata['rerank_score']:.4f} |\n")

    file.write("\n")

    file.write("### Content\n\n")

    file.write("```text\n")
    file.write(document.page_content.strip())
    file.write("\n```\n\n")


def write_section(file, title: str, documents: list[Document]):

    file.write(f"# {title}\n\n")

    for rank, document in enumerate(documents, start=1):
        write_document(file, rank, document)

    file.write("\n---\n\n")


def main():

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    evaluator = RetrievalEvaluator()

    with open(OUTPUT_PATH, "w", encoding="utf-8") as report:

        report.write("# Retrieval Evaluation Report\n\n")

        report.write(f"- Retrieval K: {RETRIEVAL_K}\n")

        report.write(f"- Rerank Top K: {RERANK_TOP_K}\n\n")

        for index, question in enumerate(QUESTIONS, start=1):

            print(f"[{index}/{len(QUESTIONS)}] {question}")

            retrieved = evaluator.retrieve_documents(question)

            reranked = evaluator.rerank_documents(question,retrieved)

            report.write(f"# Question {index}\n\n")

            report.write(f"**Question:** {question}\n\n")

            write_section(report, "Dense Retrieval", retrieved[:RERANK_TOP_K])

            write_section(report, "Reranked Retrieval", reranked)

            report.write("## Observation\n\n")

            report.write("_Write your observations here._\n\n")

            report.write("============================================================\n\n")

    print(f"\nReport written to:\n{OUTPUT_PATH}")


if __name__ == "__main__":
    main()