from llm.model import login_huggingface
from rag import RAGPipeline


def main(question):

    login_huggingface()

    pipeline = RAGPipeline()

    result = pipeline.ask(question)

    print(result["response"])


if __name__ == '__main__':
    main("What is RecursiveCharacterTextSplitter ?")