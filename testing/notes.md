The files in testing folder are moved here after completing tests.
They may not work properly if run from here.
test_pandoc.py , pandoc_test_output and cleaned_markdown were initially under the project dir not inside testing dir.
Path may not work properly due to the movement of the files.
performed chunking methods and inspected chunks in inspect_chunks.py.
Final chunks result is stored as jsonl file under chunks_inspect.jsonl.
General testing contains small tests - pypandoc, vector_store.