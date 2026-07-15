from llm.model import login_huggingface, load_model, generate_response
from config import LLM_MODEL

def main():

    # To run on colab check test_generation.ipynb file

    # if being run locally import login_huggingface from llm.model 
    # HF_TOKEN must be present in .env file, remove # from the line below
    # login_huggingface()

    tokenizer, model = load_model(LLM_MODEL)

    question = "What is RecursiveCharacterTextSplitter?"

    # dummy chunk for testing
    context = """
    RecursiveCharacterTextSplitter recursively splits text while preserving
    larger semantic units whenever possible.

    Example:

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=0
    )

    texts = text_splitter.split_text(document)
    """


    response = generate_response(tokenizer=tokenizer, model=model, question=question, context=context)

    print(response)


if __name__ == '__main__':
    main()


# run using - python -m testing.test_generation