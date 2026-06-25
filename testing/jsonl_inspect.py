from pathlib import Path
import json
from ingestion.chunking.chunker import chunk_documents

BASE_DIR = Path(__file__).parent.parent
output_path = BASE_DIR / "testing" / "chunks_inspect.jsonl"

chunks = chunk_documents()


def save_chunks_jsonl(chunks,output_path):
    """A function to save chunk contents and metadata
       as a jsonl file to inspect"""
    
    with open(output_path, "w", encoding='utf-8') as f:

        for chunk in chunks:
            # ** operator is called dictionary unpacking. 
            # It takes every key-value pair from one dictionary and inserts it into another dictionary.
            record = {
                "content" : chunk.page_content,
                **chunk.metadata
            }

            # json.dumps() converts a Python object into a JSON string. 
            # dump() → dump data into a file, dumps() → dump data into a string.
            # ensure_ascii=False tells json.dumps() not to escape non-ASCII Unicode characters. 
            # Instead, write them directly into the JSON string.
            # "\n" - write line by line not json array

            f.write(
                json.dumps(record, ensure_ascii=False) + "\n"
            )

save_chunks_jsonl(chunks, output_path)