from pathlib import Path
from tqdm import tqdm
from langchain_core.documents import Document
from ingestion.chunking.metadata import build_metadata
from ingestion.config import KB_PATH


# BASE_DIR = Path(__file__).resolve().parent.parent.parent
# KB_PATH = BASE_DIR / "knowledge_base"                     --> imported from config 



def load_all_documents() -> list[Document]:
    """Load all markdown files from the knowledge_base"""

    md_files = list(KB_PATH.rglob("*.md"))
    loaded_docs = []

    for md_file_path in tqdm(md_files, desc="Loading documents"):

        try:
            text = md_file_path.read_text(encoding='utf-8')
            metadata = build_metadata(md_file_path)
            
            loaded_docs.append(Document(page_content=text, metadata=metadata))
        
        except Exception as e:
            tqdm.write(f'Failed to load {md_file_path} : {e}')
    
    return loaded_docs