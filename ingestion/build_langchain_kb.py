from pathlib import Path
from ingestion.md_cleaner import clean_markdown


BASE_DIR = Path(__file__).resolve().parent.parent
LANGCHAIN_SOURCE = BASE_DIR / "cloned_repo" / "langchain" / "docs" / "src" / "oss"
OUTPUT_DIR = BASE_DIR / "knowledge_base" / "langchain"
SOURCE_DIRS = [ "concepts", "integrations/splitters", "langchain" ]