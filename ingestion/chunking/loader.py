from pathlib import Path
from langchain_core.documents import Document
from ingestion.chunking.metadata import build_metadata


def load_markdown_file(file_path: str) -> Document:
    """Loads a markdown file into a langchain Document object"""

    path = Path(file_path)
    text = path.read_text(encoding="utf-8")
    metadata = build_metadata(file_path)

    return Document(
        page_content=text,
        metadata=metadata
        )