from importlib.metadata import version, PackageNotFoundError

packages = [
    "pypandoc",
    "tqdm",
    "nbformat",
    "nbconvert",
    "langchain",
    "langchain-text-splitters",
    "sentence-transformers",
    "chromadb",
    "langchain-chroma",
    "langchain-huggingface",
    "python-dotenv",
    "torch",
    "transformers",
    "huggingface_hub",
    "bitsandbytes",
    "accelerate",
]

for pkg in packages:
    try:
        print(f"{pkg}: {version(pkg)}")
    except PackageNotFoundError:
        print(f"{pkg}: Not installed")