from rag import RAGPipeline
from ui.interface import create_interface


def main():

    # Initialize RAG pipeline
    pipeline = RAGPipeline()

    # Build UI
    gradio_app = create_interface(pipeline=pipeline)

    # Launch app
    gradio_app.launch()


if __name__ == '__main__':
    main()