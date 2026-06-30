# Running the Knowledge Base Build Scripts

Run each of the following build scripts separately to populate the `knowledge_base`.

## Commands

### 1. Build the Python Knowledge Base

```bash
python -m ingestion.build_kb.build_python_kb
```

### 2. Build the Pandas Knowledge Base

```bash
python -m ingestion.build_kb.build_pandas_kb
```

### 3. Build the LangChain Knowledge Base

```bash
python -m ingestion.build_kb.build_langchain_kb
```

> **Note:** Run all three commands individually from the project's root directory.