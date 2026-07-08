from langchain_core.documents import Document

def format_context(documents: list[Document]) -> str:
    """
    Takes list of langchain document objects and convert 
    them to string of context for llm
    """

    parts = []

    for i,doc in enumerate(documents, start=1):
        library = doc.metadata.get("library", "unknown")
        source = doc.metadata.get("source", "unknown")

        parts.append(
            f"Document {i}\n\nLibrary: {library}\nSource: {source}\n\nContent:\n{doc.page_content}"
        )

    seperator = "\n\n" + "-" * 60 + "\n\n"
    return seperator.join(parts)