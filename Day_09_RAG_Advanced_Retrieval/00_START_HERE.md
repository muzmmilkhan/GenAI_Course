# Day 09 - Advanced Retrieval

**What you will learn:** Better retrieval: similarity / MMR / threshold search, multi-query, reciprocal rank fusion, hybrid (BM25 + vector) search and re-ranking.

## Before you start
- Do the one-time setup in the [course README](../README.md) (`uv sync` + `.env`).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_09_RAG_Advanced_Retrieval
  ```
- Keys: `OPENAI_API_KEY`, `GOOGLE_API_KEY`, `COHERE_API_KEY` (re-ranker). Scripts 9-11 read the vector DB created in **Day 07 step 3**.

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 1 | Retrieval methods | `uv run python 9_retrieval_methods.py` |
| 2 | Multi-query retrieval | `uv run python 10_multi_query_retrieval.py` |
| 3 | Reciprocal Rank Fusion | `uv run python 11_reciprocal_rank_fusion.py` |
| 4 | Hybrid search | open 12_hybrid_search.ipynb |
| 5 | Re-ranker | open 13_reranker.ipynb |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or run `uv run jupyter lab` from the course root.

---
[<- Day_08_RAG_Chunking_Strategies](../Day_08_RAG_Chunking_Strategies/00_START_HERE.md) | [Day_10_Agents_From_Scratch_ReAct ->](../Day_10_Agents_From_Scratch_ReAct/00_START_HERE.md)
