# Day 15 - Advanced RAG with LangGraph (Self-RAG / Corrective RAG)

**What you will learn:** Agentic RAG: grade retrieved documents, rewrite queries, fall back to web search and check answers for hallucination.

## Before you start
- Do the one-time setup in the [course README](../README.md) (`uv sync` + `.env`).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_15_Advanced_RAG_with_LangGraph
  ```
- Keys: `OPENAI_API_KEY`, `GOOGLE_API_KEY`, `SERPAPI_API_KEY`. `Advance_RAG_App/data_gathering.py` is a link to `RAG_embedding/data_gathering.py` (one copy only).

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 1 | Open self_rag_vs_crag_comparison.html | double-click |
| 2 | Advanced RAG notebook (uses the ready FAISS index) | open 01_advance_rag.ipynb |
| 3 | (Optional) rebuild the FAISS index | `cd RAG_embedding && uv run python embedding.py` |
| 4 | Streamlit app | `cd Advance_RAG_App && uv run streamlit run app.py` |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or run `uv run jupyter lab` from the course root.

---
[<- Day_14_LangGraph_MapReduce_and_MultiAgent](../Day_14_LangGraph_MapReduce_and_MultiAgent/00_START_HERE.md) | [Day_16_Short_and_Long_Term_Memory ->](../Day_16_Short_and_Long_Term_Memory/00_START_HERE.md)
