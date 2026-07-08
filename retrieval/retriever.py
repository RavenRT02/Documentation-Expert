from langchain_core.documents import Document
from ingestion.embedding.vector_store import load_vector_store
from pathlib import Path

# libraries -> parameter name, list[str] | None -> is a list of str or None, = None -> default value
def retrieve(query: str, k: int = 5, libraries: list[str] | None = None, db_path: str | Path | None = None) -> list[Document]:
    """
    Retrieves the most relevant chunks based on the query
    and selected libraries based on similarity_search
    """

    vector_store = load_vector_store(db_path)

    # dict to unpack later using ** operator. Trailing , after k to support more keyword arguments
    search_kwargs = {
        "k" : k,
    }

    # if libraries are selected in gradio UI, list of libraries will be passed as arguments in this function.
    # Then libraries will not be None, making this black True and start execution (only when libraries are selected) in gradio UI.
    # filter keyword is added to search_kwargs along with k ( using the trailing ,).
    # filter searchers library metadata in the chunks for selected librarbies and filters those chunks before similarity_search.
    # "$in" is from vector database, that says "metadata must be one of these values(libraries parameter)"  
    if libraries:
        search_kwargs["filter"] = {
            "library" : {
                "$in" : libraries
            }
        }

    # the query is embedded during the similarity search. embed_query(query) <- performed internally by LangChain. 
    # Then vector similarity search is performed.
    relevant_chunks = vector_store.similarity_search(
        query=query,
        **search_kwargs,
    )

    return relevant_chunks