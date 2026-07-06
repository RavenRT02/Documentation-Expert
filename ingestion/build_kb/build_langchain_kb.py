# python script to convert .mdx files .md and store them in knowledge_base for langchain documentation
# use "python -m ingestion.build_kb.build_langchain_kb" in terminal to run

# from pathlib import Path
from tqdm import tqdm
from ingestion.md_cleaner import clean_markdown
from config import BASE_DIR


# BASE_DIR = Path(__file__).resolve().parent.parent --> imported from congif
LANGCHAIN_SOURCE = BASE_DIR / "cloned_repo" / "langchain_repo"
OUTPUT_DIR = BASE_DIR / "knowledge_base" / "langchain"
SOURCE_DIRS = [ "concepts", "langchain", "splitters" ]



def main():

    success_count = 0
    failed_count = 0

    for folder in SOURCE_DIRS:
        
        source_root = LANGCHAIN_SOURCE / folder
        mdx_files = list(source_root.rglob("*.mdx"))

        print(f"\nProcessing {folder}: {len(mdx_files)} files")

        for mdx_file in tqdm(mdx_files, desc=folder):

            try:
            
                relative_path = mdx_file.relative_to(LANGCHAIN_SOURCE)      
                destination = ( OUTPUT_DIR / relative_path ).with_suffix(".md")

                if destination.exists():
                    continue

                raw_content = mdx_file.read_text(encoding='utf-8', errors="ignore")
                cleaned_md = clean_markdown(raw_content)

                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_text(cleaned_md, encoding='utf-8')
                success_count+=1
                tqdm.write(str(destination))             # use tqdm.write as print() interferes with progress bar
            
            except Exception as e:
                tqdm.write(f"Failed: {mdx_file}")         
                tqdm.write(str(e))
                failed_count+=1

    print("\n\n")
    print("=" * 40)
    print(f"Success : {success_count}")
    print(f"Failed  : {failed_count}")
    print("=" * 40)


if __name__ == '__main__':
    main()