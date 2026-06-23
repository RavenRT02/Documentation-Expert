from pathlib import Path
import pypandoc
from tqdm import tqdm
from utils.md_cleaner import clean_markdown


BASE_DIR = Path(__file__).resolve().parent.parent
CPYTHON_DOCS = ( BASE_DIR / "cloned_repo" / "python" / "cpython" / "Doc" )
OUTPUT_DIR = ( BASE_DIR / "knowledge_base" / "python" )
SOURCE_DIRS = [ "tutorial" ]


def convert_rst_to_md(source_path : Path) -> str:
    """Helper function to convert .rst files to .md files
       using pypandoc. Returns string, no output destination"""
    
    return pypandoc.convert_file(str(source_path), "md")   


for folder in SOURCE_DIRS:
    
    source_root = CPYTHON_DOCS / folder
    rst_files = list(source_root.rglob("*.rst"))

    total_files = len(rst_files)
    success_count = 0
    failed_count = 0

    for rst_file in tqdm(rst_files):

        try:
        
            relative_path = rst_file.relative_to(CPYTHON_DOCS)               # takes only "tutotial/file.rst"
            destination = ( OUTPUT_DIR / relative_path ).with_suffix(".md")
            destination.parent.mkdir(parents=True, exist_ok=True)

            raw_md = convert_rst_to_md(rst_file)
            cleaned_md = clean_markdown(raw_md)

            destination.write_text(cleaned_md, encoding='utf-8')
            success_count+=1
            print(destination)
        
        except Exception as e:
            print(f'Failed : {rst_file}')
            failed_count+=1
            print(e)

print('\n\n')
print(f'Success : {success_count}')
print(f'Failed : {failed_count}')