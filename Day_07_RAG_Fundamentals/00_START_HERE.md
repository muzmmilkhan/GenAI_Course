# Day 07 - RAG Fundamentals - Retrieval Augmented Generation

**What you will learn:** Give an LLM your own documents: load -> split -> embed -> store in a vector DB (Chroma) -> retrieve -> answer.

## Before you start
- Do the one-time setup in the [course README](../README.md) (`uv sync` + `.env`).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_07_RAG_Fundamentals
  ```
- Keys: `OPENAI_API_KEY`, `GOOGLE_API_KEY`. Read `RAG_FOR_BEGINNERS_GUIDE.md` - it explains Days 07-09. **Run step 3 before Day 09** (Day 09 reuses this vector DB).

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 1 | Intro notebook: RAG over a YouTube transcript | open 0_rag_using_langchain_intro.ipynb |
| 2 | Embedding basics | `uv run python embedding_basics.py` |
| 3 | Ingest docs/ into Chroma (creates db/chroma_db) | `uv run python 1_ingestion_pipeline.py` |
| 4 | Retrieve relevant chunks | `uv run python 2_retrieval_pipeline.py` |
| 5 | Generate an answer from the chunks | `uv run python 3_answer_generation.py` |
| 6 | Conversational RAG (remembers history) | `uv run python 4_history_aware_generation.py` |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or run `uv run jupyter lab` from the course root.

---
[<- Day_06_LangChain_Chains](../Day_06_LangChain_Chains/00_START_HERE.md) | [Day_08_RAG_Chunking_Strategies ->](../Day_08_RAG_Chunking_Strategies/00_START_HERE.md)
