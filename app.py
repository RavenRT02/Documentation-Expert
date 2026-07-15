from rag import RAGPipeline
from ui.interface import create_interface


def main(db_path: str | None = None):

    # Initialize RAG pipeline
    pipeline = RAGPipeline(db_path=db_path)

    # Build UI
    gradio_app = create_interface(pipeline=pipeline)

    # Launch app
    gradio_app.launch(debug=True)


if __name__ == '__main__':
    main()