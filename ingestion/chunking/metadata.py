from pathlib import Path


def build_metadata(file_path: str) -> dict:
    """Function to build metadata for chunks
       based on knowledge_base path"""
    
    path = Path(file_path)

    parts = path.parts    # breaks path into parts based on \ and places it inside a tuple

    # consider "knowledge_base/python/library/pathlib.md"
    # *parts - unpacks tuple so it won't be Path(("library", "pathlib.md")) but Path("library", "pathlib.md")
    # path.as_posix() keeps path metadata consistent (linux format) across windows, linux / mac os.
    # win - 'library\\pathlib.md', linux and mac - 'library/pathlib.md'. Without path.as_posix()

    source = str(Path(*parts[2:]).as_posix()) 

    metadata = {
        "library" : parts[1],
        "section" : parts[2],
        "source"  : source,
        "file_path" : str(path.as_posix())
    }

    return metadata