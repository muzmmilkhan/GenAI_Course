# Day 08 - RAG Chunking Strategies & Multi-modal RAG

**What you will learn:** How you split documents changes answer quality: recursive, semantic and agentic (LLM-driven) chunking, plus RAG over PDFs with images and tables.

## Before you start
- Do the one-time setup in the [course README](../README.md) (`uv sync` + `.env`).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_08_RAG_Chunking_Strategies
  ```
- Keys: `OPENAI_API_KEY`, `GOOGLE_API_KEY`. Notebook 8 needs system tools: `brew install poppler tesseract libmagic`. `dbv2/` is the vector DB the notebook builds.

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 1 | Recursive character splitter | `uv run python 5_recursive_character_text_splitter.py` |
| 2 | Semantic chunking | `uv run python 6_semantic_chunking.py` |
| 3 | Agentic chunking | `uv run python 7_agentic_chunking.py` |
| 4 | Multi-modal RAG on docs/attention-is-all-you-need.pdf | open 8_multi_modal_rag.ipynb |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or run `uv run jupyter lab` from the course root.

---
[<- Day_07_RAG_Fundamentals](../Day_07_RAG_Fundamentals/00_START_HERE.md) | [Day_09_RAG_Advanced_Retrieval ->](../Day_09_RAG_Advanced_Retrieval/00_START_HERE.md)
