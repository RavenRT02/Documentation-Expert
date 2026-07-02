from retrieval.retriever import retrieve
from ingestion.config import BASE_DIR

output_file = BASE_DIR / "retrieval_results.md"


def save_query_results(
    question: str,
    output_file: str = output_file,
    k: int = 5,
):
    results = retrieve(question, k=k)

    with open(output_file, "a", encoding="utf-8") as f:
        f.write(f"# Question\n\n")
        f.write(f"{question}\n\n")

        if not results:
            f.write("No results found.\n\n---\n\n")
            return

        for i, doc in enumerate(results, start=1):
            f.write(f"## Rank {i}\n\n")
            f.write(f"- **Chunk ID:** {doc.metadata['chunk_id']}\n")
            f.write(f"- **Library:** {doc.metadata['library']}\n")
            f.write(f"- **Source:** {doc.metadata['source']}\n\n")

            f.write("### Content\n\n")
            f.write("```text\n")
            f.write(doc.page_content)
            f.write("\n```\n\n")

        f.write("\n---\n\n")


# Example questions
questions = [
    "How do I create directories recursively?",
    "How do I merge DataFrames?",
    "What is PromptTemplate?",
    "How do i read a CSV?",
    "How do I iterate over a directory?",
    "What is RecursiveCharacterTextSplitter?"
]

# Clear previous output (optional)
# open("retrieval_results.md", "w").close()

for question in questions:
    save_query_results(question)