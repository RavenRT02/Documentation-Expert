# test pandoc working

"""
import pypandoc
from pathlib import Path

# print(pypandoc.get_pandoc_version())

BASE_DIR = Path(__file__).parent
source_path = BASE_DIR / "cloned_repo" / "python" / "cpython" / "Doc" / "tutorial" / "classes.rst"
destination_path = BASE_DIR / "pandoc_test_output" / "classes.md"

destination_path.parent.mkdir(exist_ok=True)

pypandoc.convert_file(str(source_path), "md", outputfile=str(destination_path))
"""


# Test if vector_store has embedded all chunks

"""
from ingestion.embedding.vector_store import load_vector_store

vs = load_vector_store()
print(vs._collection.count())
"""