from ingestion.chunking.loader import load_all_documents
from ingestion.chunking.splitter import split_by_headers, split_large_sections
from ingestion.chunking.metadata import add_chunk_ids
from tqdm import tqdm


def chunk_documents():

    docs = load_all_documents()

    all_sections = []
    for doc in tqdm(docs, desc="Header splitting"):
        header_sections = split_by_headers(doc.page_content)
        for section in header_sections:
            section.metadata.update(doc.metadata)
        all_sections.extend(header_sections)


    chunks = split_large_sections(all_sections)
    chunks = add_chunk_ids(chunks)

    return chunks