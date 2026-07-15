from langchain_core.documents import Document
from config import ROLE_LABELS

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



def format_history(history: list[dict]) -> str:
    """
    Formats conversations from list[dict] to str
    and arrange them in llm-friendly format
    """

    lines = []

    # ROLE_LABELS since we change summary to Conversation Summary, not just capitalize
    for message in history:
        lines.append(f'{ROLE_LABELS[message["role"]]}:')
        lines.append(message["content"])
        lines.append("")

    return "\n".join(lines)