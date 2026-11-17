# Day 09 - Advanced Retrieval

**What you will learn:** Better retrieval: similarity / MMR / threshold search, multi-query, reciprocal rank fusion, hybrid (BM25 + vector) search and re-ranking.

## Before you start
- Finished [Day 00](../Day_00_Setup_uv_and_Python/00_START_HERE.md) once (your uv project, `.env` and notebook kernel are ready).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_09_RAG_Advanced_Retrieval
  ```
- Keys: `OPENAI_API_KEY`, `GOOGLE_API_KEY`, `COHERE_API_KEY` (re-ranker). Scripts 9-11 read the vector DB created in **Day 07 step 3**.

## 📦 Step 1 - Install today's packages
Run this in the terminal (from this Day folder or the course root — uv finds your project automatically):
```bash
uv add langchain-classic langchain-cohere rank-bm25
```
| Package | What it is for |
|---|---|
| `langchain-classic` | older LangChain helpers, e.g. EnsembleRetriever |
| `langchain-cohere` | Cohere models and the Cohere re-ranker |
| `rank-bm25` | keyword search (BM25) used by BM25Retriever |

> 🔎 Afterwards open `pyproject.toml` (course root) and find the new lines. We always install the **latest** versions, so your version numbers may be newer than your classmates' — that's normal.

<details>
<summary>🧯 Something went wrong? Click here</summary>

| You see... | What to do |
|---|---|
| `ModuleNotFoundError: No module named 'langchain_classic'` | the package is not installed — run today's `uv add` command above |
| `No solution found when resolving dependencies` | two packages need versions that don't fit together. Read the error from the bottom, then try `uv add "<package>"` without a version, or limit it: `uv add "<package><X"` (see Day 00). |
| Notebook: `No module named ...` but `uv run` works | select the `.venv (Python 3.12)` kernel from the course folder |
| `Could not import rank_bm25` | You skipped today's install: `uv add rank-bm25`. |
</details>

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 0 | 🐍 **Python basics for today** — the Python used in this day, explained very simply (no API key needed) | open 00_python_basics.ipynb |
| 1 | Retrieval methods | `uv run python 9_retrieval_methods.py` |
| 2 | Multi-query retrieval | `uv run python 10_multi_query_retrieval.py` |
| 3 | Reciprocal Rank Fusion | `uv run python 11_reciprocal_rank_fusion.py` |
| 4 | Hybrid search | open 12_hybrid_search.ipynb |
| 5 | Re-ranker | open 13_reranker.ipynb |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or `uv add jupyterlab` once and run `uv run jupyter lab`.

---
[<- Day_08_RAG_Chunking_Strategies](../Day_08_RAG_Chunking_Strategies/00_START_HERE.md) | [Day_10_Agents_From_Scratch_ReAct ->](../Day_10_Agents_From_Scratch_ReAct/00_START_HERE.md)
