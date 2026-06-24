from langchain_text_splitters import MarkdownHeaderTextSplitter
from ingestion.config import HEADERS_TO_SPLIT_ON


def split_by_headers(text: str):

    splitter = MarkdownHeaderTextSplitter(headers_to_split_on=HEADERS_TO_SPLIT_ON)
    return splitter.split_text(text)