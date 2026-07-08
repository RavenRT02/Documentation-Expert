# python script to convert .rst files and ipynb files to .md and store them in knowledge_base for pandas documentation
# use "python -m ingestion.build_kb.build_pandas_kb" in terminal to run

from pathlib import Path
from tqdm import tqdm
import pypandoc
from utils.md_cleaner import clean_markdown
import nbformat
from nbconvert import MarkdownExporter
from config import BASE_DIR


# BASE_DIR = Path(__file__).resolve().parent.parent --> impoted from config
PANDAS_SOURCE = BASE_DIR / "cloned_repo" / "pandas" / "doc" / "source"
OUTPUT_DIR = BASE_DIR / "knowledge_base" / "pandas"
SOURCE_DIRS = [ "reference", "user_guide" ]


def convert_rst_to_md(source_path : Path) -> str:
    """Helper function to convert .rst files to .md files
       using pypandoc. Returns string, no output destination"""
    
    return pypandoc.convert_file(str(source_path), "md")  



def convert_ipynb_to_md(source_path : Path) -> str:
    """Helper function to convert .ipynb files to .md files
       using nbconvert. Returns string, no output destination"""
    
    with open(source_path, encoding='utf-8') as f:
        # parse notebook json, an ipynb is actually a json
        # nbformat.read() reads that JSON and converts it into a Notebook object.
        notebook = nbformat.read(f, as_version=4)

    exporter = MarkdownExporter()  # convert notebook cells into Markdown
    body, _ = exporter.from_notebook_node(notebook) # returns markdown_text, resources.

    return body   # taking markdown alone


def convert_to_md(source_path : Path) -> str:
    """Use rst to md or ipynb to md conversion
       based on extension suffix and return a string"""
    
    suffix = source_path.suffix.lower()

    if suffix == ".rst":
        return convert_rst_to_md(source_path)

    elif suffix == ".ipynb":
        return convert_ipynb_to_md(source_path)

    else:
        raise ValueError(f'Unsupported file type: {suffix}')
    


def main():

    success_count = 0
    failed_count = 0

    for folder in SOURCE_DIRS:
        
        source_root = PANDAS_SOURCE / folder
        # files_to_process = (list(source_root.rglob("*.rst")) + list(source_root.rglob("*.ipynb")))
        files_to_process = [ p for p in source_root.rglob("*") if p.suffix.lower() in {".rst", ".ipynb"} ]  # fits other formats by adding to set

        print(f"\nProcessing {folder}: {len(files_to_process)} files")

        for source_file in tqdm(files_to_process, desc=folder):

            try:
            
                relative_path = source_file.relative_to(PANDAS_SOURCE)               
                destination = ( OUTPUT_DIR / relative_path ).with_suffix(".md")

                if destination.exists():
                    continue

                raw_md = convert_to_md(source_file)
                cleaned_md = clean_markdown(raw_md)

                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_text(cleaned_md, encoding='utf-8')
                success_count+=1
                tqdm.write(str(destination))             # use tqdm.write as print() interferes with progress bar
            
            except Exception as e:
                tqdm.write(f"Failed: {source_file}")         
                tqdm.write(str(e))
                failed_count+=1

    print("\n\n")
    print("=" * 40)
    print(f"Success : {success_count}")
    print(f"Failed  : {failed_count}")
    print("=" * 40)


if __name__ == '__main__':
    main()