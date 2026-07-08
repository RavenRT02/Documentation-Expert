# python script to convert .rst files to .md and store them in knowledge_base for python documentation
# use "python -m ingestion.build_kb.build_python_kb" in terminal to run

from pathlib import Path
import pypandoc
from tqdm import tqdm
from utils.md_cleaner import clean_markdown
from config import BASE_DIR


# BASE_DIR = Path(__file__).resolve().parent.parent --> imported from congif
CPYTHON_DOCS = ( BASE_DIR / "cloned_repo" / "python" / "cpython" / "Doc" )
OUTPUT_DIR = ( BASE_DIR / "knowledge_base" / "python" )
SOURCE_DIRS = [ "tutorial", "library" ]


def convert_rst_to_md(source_path : Path) -> str:
    """Helper function to convert .rst files to .md files
       using pypandoc. Returns string, no output destination"""
    
    return pypandoc.convert_file(str(source_path), "md")   



def main():

    success_count = 0
    failed_count = 0

    for folder in SOURCE_DIRS:
        
        source_root = CPYTHON_DOCS / folder
        rst_files = list(source_root.rglob("*.rst"))

        print(f"\nProcessing {folder}: {len(rst_files)} files")

        for rst_file in tqdm(rst_files, desc=folder):

            try:
            
                relative_path = rst_file.relative_to(CPYTHON_DOCS)               # takes only "tutotial/file.rst"
                destination = ( OUTPUT_DIR / relative_path ).with_suffix(".md")

                if destination.exists():
                    continue

                raw_md = convert_rst_to_md(rst_file)
                cleaned_md = clean_markdown(raw_md)

                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_text(cleaned_md, encoding='utf-8')
                success_count+=1
                tqdm.write(str(destination))             # use tqdm.write as print() interferes with progress bar
            
            except Exception as e:
                tqdm.write(f"Failed: {rst_file}")         
                tqdm.write(str(e))
                failed_count+=1

    print("\n\n")
    print("=" * 40)
    print(f"Success : {success_count}")
    print(f"Failed  : {failed_count}")
    print("=" * 40)


if __name__ == '__main__':
    main()