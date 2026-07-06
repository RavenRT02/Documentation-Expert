from pathlib import Path
from collections import defaultdict
from config import KB_PATH

# BASE_DIR = Path(__file__).resolve().parent.parent.parent
# KB_PATH = BASE_DIR / "knowledge_base"                  ----> imported from congif

def build_metadata(file_path: str) -> dict:
    """Function to build metadata for chunks
       based on knowledge_base path"""
    
    path = Path(file_path)
    relative_path = path.relative_to(KB_PATH)

    parts = relative_path.parts    # breaks path into parts based on \ and places it inside a tuple

    # consider "knowledge_base/python/library/pathlib.md"
    # relative path is "python/library/pathlib.md" so careful with indexing
    # *parts - unpacks tuple so it won't be Path(("library", "pathlib.md")) but Path("library", "pathlib.md")
    # path.as_posix() keeps path metadata consistent (linux format) across windows, linux / mac os.
    # win - 'library\\pathlib.md', linux and mac - 'library/pathlib.md'. Without path.as_posix()


    metadata = {
        "library" : parts[0],
        "module"  : path.stem,
        "section" : parts[1],
        "source"  : Path(*parts[1:]).as_posix(),
        "file_path" : relative_path.as_posix()
    }

    return metadata



def add_chunk_ids(chunks):
    """Add unique chunk_id metadata for all the chunks"""

    counters = defaultdict(int)
    # If someone asks for a key that doesn't exist, automatically create it with the value int() -> returns 0.
    # 1st chunk in -> no key yet so 0, next chunk in -> key exists, increments 0 -> 1. 
    # When module / library name changes , chunk_ids count separately for them. 
    # "chunk_id": "python:pathlib:0001", "chunk_id": "pandas:pandas.merge:0001", "chunk_id": "python:pathlib:0002".
    # chunk order does not matter, it keeps track seperately. 

    for chunk in chunks:

        library = chunk.metadata["library"]
        module = chunk.metadata["module"]

        key = f'{library}:{module}'   # combined key 
        counters[key]+=1

        chunk.metadata["chunk_id"] = (f'{library}:{module}:{counters[key]:04d}')
        # 04d -> min width 4 - padding with zero --> if 1 then -> 0001, if 25 -> 0025

    return chunks