# single file load 

"""
def load_markdown_file(file_path: str) -> Document:
    # loads a markdown file into a langchain Document object

    path = Path(file_path)
    text = path.read_text(encoding="utf-8")
    metadata = build_metadata(file_path)

    return Document(
        page_content=text,
        metadata=metadata
        )
"""

# check build_metadata function

"""
from ingestion.chunking.metadata import build_metadata

metadata = build_metadata("knowledge_base/python/library/pathlib.md")
print(metadata)

metadata = build_metadata( "knowledge_base/pandas/reference/api/pandas.merge.md")
print(metadata)
"""


# Check header splitter and sections 

"""
from ingestion.chunking.loader import load_markdown_file
from ingestion.chunking.splitter import split_by_headers

doc = load_markdown_file("knowledge_base/python/library/pathlib.md")

sections = split_by_headers(doc.page_content)

print("\nTOTAL HEADER SECTIONS")
print(len(sections))

print(type(doc))

print("\nMETADATA")

print(doc.metadata)

print("\nCONTENT PREVIEW")
print(doc.page_content[:500])
print("\nTOTAL CHARACTERS")
print(len(doc.page_content))

for i, section in enumerate(sections[:5]):

    print("\n" + "="*80)
    print(f"SECTION {i+1}")
    print(section.metadata)
    print()
    print(section.page_content[:300])


for section in sections:
    if "h3" in section.metadata:
        print(section.metadata)
        break

print()

lengths = [len(section.page_content) for section in sections]

print("Sections:", len(lengths))
print("Min:", min(lengths))
print("Max:", max(lengths))
print("Average:", sum(lengths) / len(lengths))
"""


# Checking chunk size and metadata after Recurssive splitting

"""from ingestion.chunking.loader import load_markdown_file
from ingestion.chunking.splitter import split_by_headers, split_large_sections

doc = load_markdown_file("knowledge_base/python/library/pathlib.md")
# doc - langchain Document object with page_content and metadata

header_sections = split_by_headers(doc.page_content)
# header_sections - Breaks the page_content from doc based on headers into a list of langchain Document objects --> sections
# Each section has page_content with the heading as metadata. Original metadata lost
# MarkdownHeaderTextSplitter intentionally return list of Document object after taking a string as input (page_content)

for section in header_sections:
    section.metadata.update(doc.metadata)
# Older metadata is added to the header metadata for each section so that chunks will have full metadata on recurssive_split

chunks = split_large_sections(header_sections)
# List of langchain Document objects with page_content and metadata (original+header)"""

# part above is essential to run the prints and tests below this 

"""print("Header Sections:", len(header_sections))
print("Final Chunks:", len(chunks))

for chunk in chunks[:5]:

    print("\n" + "=" * 80)

    print(chunk.metadata)

    print()

    print(len(chunk.page_content))

    print()

    print(chunk.page_content[:300])

print("\n" + "="*80)

sizes = [len(chunk.page_content) for chunk in chunks]
print(min(sizes))
print(max(sizes))
print(sum(sizes)/len(sizes))
print("\n" + "="*80)"""



# Inspect small chunks

"""small_chunks = [
    chunk
    for chunk in chunks
    if len(chunk.page_content) < 250
]

print(f'Small chunks : {len(small_chunks)}')

for chunk in small_chunks:
    print("=" * 80)
    print(len(chunk.page_content))
    print(chunk.metadata)
    print(chunk.page_content[:500])"""


# check how many bad headings like {"h1" : 'it could delete all of your files.'} exist in chunks.

"""from collections import Counter

counter = Counter()

for chunk in chunks:

    if "h1" in chunk.metadata:
        counter[chunk.metadata["h1"]] += 1

print(counter.most_common(50))

# Find text around this bad heading

text = doc.page_content
idx = text.find("it could delete all of your files")
print(idx)
print(text[idx-500:idx+500])"""


# chunker.py testing overall metrics 

"""from ingestion.chunking.loader import load_all_documents
from ingestion.chunking.splitter import split_by_headers, split_large_sections
from tqdm import tqdm
from collections import Counter


docs = load_all_documents()

all_sections = []
for doc in tqdm(docs, desc="Header splitting"):
    header_sections = split_by_headers(doc.page_content)
    for section in header_sections:
        section.metadata.update(doc.metadata)
    all_sections.extend(header_sections)


chunks = split_large_sections(all_sections)

print("\n" + "=" * 80)

print(f'Total documents loaded : {len(docs)}')
print(f'Total sections : {len(all_sections)}')
print(f'Total chunks : {len(chunks)}')

print("\n" + "=" * 80)

sizes = [len(chunk.page_content) for chunk in chunks]

print("Chunk Size Statistics")
print("-" * 40)

print(f'minimum chunk size : {min(sizes)}')
print(f'maximun chunk size : {max(sizes)}')
print(f'average chunk size : {sum(sizes)/len(sizes)}')

print("\n" + "="*80)

small_chunks = [chunk for chunk in chunks if len(chunk.page_content) < 250]
tiny_chunks = [chunk for chunk in chunks if len(chunk.page_content) < 100]

print("Small Chunk Statistics")
print("-" * 40)

print(f'Chunks below 250 char : {len(small_chunks)}')
print(f'Chunks below 100 char : {len(tiny_chunks)}')
print(f"% < 250 chars : {(len(small_chunks)/len(chunks))*100:.2f}%")

print(f"% < 100 chars : {(len(tiny_chunks)/len(chunks))*100:.2f}%")

print("\n" + "="*80)

libraries = {
    chunk.metadata["library"]
    for chunk in chunks
    if "library" in chunk.metadata
}

modules = {
    chunk.metadata["module"]
    for chunk in chunks
    if "module" in chunk.metadata
}

library_counter = Counter(
    chunk.metadata["library"]
    for chunk in chunks
)

print("Metadata Statistics")
print("-" * 40)

print(f"Unique libraries : {len(libraries)}")
print(f"Unique modules   : {len(modules)}")
print("library counter : \n")
print(library_counter)

print("\n" + "=" * 80)


h1_counter = Counter()

for chunk in chunks:
    if "h1" in chunk.metadata:
        h1_counter[chunk.metadata["h1"]] += 1

chunks_with_h2 = sum(
    1 for chunk in chunks
    if "h2" in chunk.metadata
)

chunks_with_h3 = sum(
    1 for chunk in chunks
    if "h3" in chunk.metadata
)


print("Structure Statistics")
print("-" * 40)

print(f"Chunks with h2 : {chunks_with_h2}")
print(f"Chunks with h3 : {chunks_with_h3}")

print(f"% with h2 : {(chunks_with_h2/len(chunks))*100:.2f}%")

print(f"% with h3 : {(chunks_with_h3/len(chunks))*100:.2f}%")

print("\n" + "=" * 80)


print("Top 20 H1 Values")
print("-" * 40)

for h1, count in h1_counter.most_common(20):
    print(f"{count:5d}  {h1}")

print("\n" + "=" * 80)

for doc in docs[60:76]:
    print(doc.metadata["library"])"""



# chunk_id metadata testing 

from ingestion.chunking.chunker import chunk_documents

chunks = chunk_documents()

print(len(chunks))
print(chunks[0].metadata)
print(chunks[-1].metadata)
print("\n" + "=" * 80)

print(chunks[500].metadata)
print("-" * 80)
print(chunks[500].page_content[:500])
print("\n" + "=" * 80)

print(chunks[5000].metadata)
print("-" * 80)
print(chunks[5000].page_content[:500])
print("\n" + "=" * 80)

print(chunks[10000].metadata)
print("-" * 80)
print(chunks[10000].page_content[:500])