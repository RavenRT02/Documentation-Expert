CHUNK_SIZE = 1000
CHUNK_OVERLAP = 159


# used for chunking - "Whenever you see these Markdown headers, treat them as document boundaries and keep track of them."
# we store these as metadata (h1-python guide, h2-functions,etc) to find chunk source.
HEADERS_TO_SPLIT_ON = [
    ("#", "h1"),
    ("##", "h2"),
    ("###", "h3"),
]