from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from config import HEADERS_TO_SPLIT_ON, CHUNK_SIZE, CHUNK_OVERLAP



header_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=HEADERS_TO_SPLIT_ON)
recurssive_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
    separators=[
        "\n### ",
        "\n## ",
        "\n\n",
        " ",
        ""
    ]
    )


def split_by_headers(text: str):
    """It first splits the document into sections 
       based on Markdown headers and attaches header information as metadata."""
    
    return header_splitter.split_text(text)


def split_large_sections(documents):
    """chunk sections created by split_by_headers
       while maintaining the metadata"""
    
    return recurssive_splitter.split_documents(documents)