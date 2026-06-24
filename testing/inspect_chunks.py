"""from ingestion.chunking.metadata import build_metadata

metadata = build_metadata("knowledge_base/python/library/pathlib.md")
print(metadata)

metadata = build_metadata( "knowledge_base/pandas/reference/api/pandas.merge.md")
print(metadata)"""


from ingestion.chunking.loader import load_markdown_file
from ingestion.chunking.splitter import split_by_headers

doc = load_markdown_file("knowledge_base/python/library/pathlib.md")

sections = split_by_headers(doc.page_content)

print("\nTOTAL HEADER SECTIONS")
print(len(sections))

"""print(type(doc))

print("\nMETADATA")
print(doc.metadata)

print("\nCONTENT PREVIEW")
print(doc.page_content[:500])
print("\nTOTAL CHARACTERS")
print(len(doc.page_content))"""

for i, section in enumerate(sections[:5]):

    print("\n" + "="*80)
    print(f"SECTION {i+1}")
    print(section.metadata)
    print()
    print(section.page_content[:300])