# Day 07 - RAG Fundamentals - Retrieval Augmented Generation

**What you will learn:** Give an LLM your own documents: load -> split -> embed -> store in a vector DB (Chroma) -> retrieve -> answer.

## Before you start
- Finished [Day 00](../Day_00_Setup_uv_and_Python/00_START_HERE.md) once (your uv project, `.env` and notebook kernel are ready).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_07_RAG_Fundamentals
  ```
- Keys: `OPENAI_API_KEY`, `GOOGLE_API_KEY`. Read `RAG_FOR_BEGINNERS_GUIDE.md` - it explains Days 07-09. **Run step 3 before Day 09** (Day 09 reuses this vector DB).

## 📦 Step 1 - Install today's packages
Run this in the terminal (from this Day folder or the course root — uv finds your project automatically):
```bash
uv add langchain-community langchain-text-splitters langchain-chroma faiss-cpu youtube-transcript-api
```
| Package | What it is for |
|---|---|
| `langchain-community` | hundreds of community integrations (loaders, vector stores, tools) |
| `langchain-text-splitters` | cut documents into chunks |
| `langchain-chroma` | the Chroma vector database for LangChain |
| `faiss-cpu` | Facebook's fast vector search library |
| `youtube-transcript-api` | download YouTube transcripts |

> 🔎 Afterwards open `pyproject.toml` (course root) and find the new lines. We always install the **latest** versions, so your version numbers may be newer than your classmates' — that's normal.

<details>
<summary>🧯 Something went wrong? Click here</summary>

| You see... | What to do |
|---|---|
| `ModuleNotFoundError: No module named 'langchain_community'` | the package is not installed — run today's `uv add` command above |
| `No solution found when resolving dependencies` | two packages need versions that don't fit together. Read the error from the bottom, then try `uv add "<package>"` without a version, or limit it: `uv add "<package><X"` (see Day 00). |
| Notebook: `No module named ...` but `uv run` works | select the `.venv (Python 3.12)` kernel from the course folder |
</details>

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 0 | 🐍 **Python basics for today** — the Python used in this day, explained very simply (no API key needed) | open 00_python_basics.ipynb |
| 1 | Intro notebook: RAG over a YouTube transcript | open 0_rag_using_langchain_intro.ipynb |
| 2 | Embedding basics | `uv run python embedding_basics.py` |
| 3 | Ingest docs/ into Chroma (creates db/chroma_db) | `uv run python 1_ingestion_pipeline.py` |
| 4 | Retrieve relevant chunks | `uv run python 2_retrieval_pipeline.py` |
| 5 | Generate an answer from the chunks | `uv run python 3_answer_generation.py` |
| 6 | Conversational RAG (remembers history) | `uv run python 4_history_aware_generation.py` |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or `uv add jupyterlab` once and run `uv run jupyter lab`.

---
[<- Day_06_LangChain_Chains](../Day_06_LangChain_Chains/00_START_HERE.md) | [Day_08_RAG_Chunking_Strategies ->](../Day_08_RAG_Chunking_Strategies/00_START_HERE.md)
