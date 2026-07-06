from llm.model import login_huggingface, load_model, generate_response
from config import LLM_MODEL

def main():

    # Huggingface login performed in colab notebook using 
    # HF_TOKEN must be present in secrets, run the lines below in colab cell
    # from google.colab import userdata
    # login_huggingface(userdata.get("HF_TOKEN"))

    # if being run locally import login_huggingface from llm.model 
    # HF_TOKEN must be present in .env file, run the line below
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


# colab cells for testing

# cell 1 : !git clone link

# cell 2 : 
# %cd Documentation-Expert
# !pip install -q -r requirements.txt

# cell 3 : 
# from google.colab import userdata
# from llm.model import login_huggingface
# login_huggingface(userdata.get("HF_TOKEN"))

# cell 4 :
# from testing.test_generation import main
# main()