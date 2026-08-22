# Documentation Expert RAG

A Retrieval-Augmented Generation (RAG) system that answers questions using the official documentation for **Python**, **Pandas**, and **LangChain**.

Instead of relying on the language model's internal knowledge, the system retrieves relevant documentation, reranks the results, and generates answers strictly from the retrieved context. When sufficient documentation cannot be found, it refuses to answer.

---

## Features

- Official documentation knowledge base
  - Python
  - Pandas
  - LangChain
- Query rewriting
- Dense vector retrieval using ChromaDB
- Cross-Encoder reranking
- Metadata-based library filtering
- Conversation history with automatic summarization
- Strict context-based answer generation
- Context sufficiency check to reduce hallucinations
- Gradio web interface
- Modular architecture for future extensions

---

## 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| LLM | Qwen2.5-7B-Instruct (4-bit) |
| Embeddings | BAAI/bge-small-en-v1.5 |
| Reranker | BAAI/bge-reranker-base |
| Vector Database | ChromaDB |
| Framework | LangChain |
| UI | Gradio |
| Development | VS Code |
| Inference | Google Colab (Tesla T4) |

---

# System Architecture

```text
                    User Question
                          │
                          ▼
              Library Selection Filter
                          │
                          ▼
                   Query Rewriting
                          │
                          ▼
                 Dense Vector Retrieval
                    (ChromaDB + BGE)
                          │
                          ▼
                Cross-Encoder Reranker
               (BAAI/bge-reranker-base)
                          │
                          ▼
             Context Sufficiency Check
                          │
             ┌────────────┴────────────┐
             │                         │
             ▼                         ▼
      Insufficient Context       Retrieved Context
             │                         │
             ▼                         ▼
      Refuse to Answer         Qwen2.5-7B-Instruct
                                      │
                                      ▼
                               Final Response
```

---

# Pipeline

1. User selects one or more documentation libraries.
2. User question and recent turns are passed to llm for query rewriting.
3. The retriever searches the Chroma vector database.
4. Top retrieval results are reranked using a Cross-Encoder.
5. Retrieved context is checked for sufficiency.
6. If sufficient, the LLM answers using only the retrieved documentation.
7. Otherwise, the system refuses to answer instead of hallucinating.

---

# Screenshots

## Python Documentation

> Correct library selected.

![Python Example](assets/python_query.png)

---

## Multiple Documentation Sources

> Answer generated using information retrieved from multiple selected libraries.

![Multiple Libraries](assets/multiple_libraries.png)

---

## Context Refusal

> Incorrect library selected. The system correctly reports insufficient context.

![Insufficient Context](assets/insufficient_context.png)

---

## Query Rewriting

> System handles follow up question with insufficient context with query rewriting.

![Query Rewriting](assets/recent_question.png)

![Query Rewriting](assets/follow_up_question.png)

---

# Dataset Statistics

| Metric | Value |
|---------|------:|
| Documentation Files | 461 |
| Final Chunks | 12,894 |
| Chunk Size | 1000 |
| Chunk Overlap | 150 |

---

# Key Design Decisions

- Preserve original documentation hierarchy
- Metadata-driven retrieval filtering
- Single Chroma collection
- Modular architecture
- Separate retrieval, reranking, generation and UI
- Conversation summarization for long chats
- Recent messages for query rewriting context
- Strict refusal when context is insufficient

---

# Future Improvements

- Source citations
- Hybrid Search (BM25 + Dense Retrieval)
- Multi-query retrieval
- Streaming responses

---

# Installation (Local)

```bash
git clone <repo-url>

cd Documentation-Expert

pip install -r requirements.txt
```

- Build the knowledge base and vector database before launching the application.
- Knowledge base - Refer ingestion/build_kb/README.md.
- Vectorstore - Refer ingestion/build_vector_store.py comments.

---

# Run (Local)

```bash
python app.py
```

---

# Run (Colab)

1. Download the notebook (raw file) from - https://github.com/RavenRT02/Documentation-Expert/blob/main/colab_app.ipynb
2. Upload file to google drive
3. Open file in drive to open it in google colab
4. Follow instructions to run

---

# Acknowledgements

- Python Documentation
- Pandas Documentation
- LangChain Documentation
- Hugging Face
- LangChain
- ChromaDB

---

# License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Third-Party Models and Resources

This project uses several third-party models and libraries, each with their own licenses and usage terms:

- Qwen2.5-7B-Instruct
- BAAI/bge-small-en-v1.5
- BAAI/bge-reranker-base
- ChromaDB
- LangChain
- Gradio

Please review the respective licenses and terms of use before using this project commercially or redistributing models.