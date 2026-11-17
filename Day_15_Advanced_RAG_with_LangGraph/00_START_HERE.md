# Day 15 - Advanced RAG with LangGraph (Self-RAG / Corrective RAG)

**What you will learn:** Agentic RAG: grade retrieved documents, rewrite queries, fall back to web search and check answers for hallucination.

## Before you start
- Finished [Day 00](../Day_00_Setup_uv_and_Python/00_START_HERE.md) once (your uv project, `.env` and notebook kernel are ready).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_15_Advanced_RAG_with_LangGraph
  ```
- Keys: `OPENAI_API_KEY`, `GOOGLE_API_KEY`, `SERPAPI_API_KEY`. The PDF download script lives in `RAG_embedding/data_gathering.py`.

## 📦 Step 1 - Install today's packages
Run this in the terminal (from this Day folder or the course root — uv finds your project automatically):
```bash
uv add pypdf google-search-results
```
| Package | What it is for |
|---|---|
| `pypdf` | read PDF files |
| `google-search-results` | SerpAPI web search (used for the web-search fallback) |

> 🔎 Afterwards open `pyproject.toml` (course root) and find the new lines. We always install the **latest** versions, so your version numbers may be newer than your classmates' — that's normal.

<details>
<summary>🧯 Something went wrong? Click here</summary>

| You see... | What to do |
|---|---|
| `ModuleNotFoundError: No module named 'pypdf'` | the package is not installed — run today's `uv add` command above |
| `No solution found when resolving dependencies` | two packages need versions that don't fit together. Read the error from the bottom, then try `uv add "<package>"` without a version, or limit it: `uv add "<package><X"` (see Day 00). |
| Notebook: `No module named ...` but `uv run` works | select the `.venv (Python 3.12)` kernel from the course folder |
</details>

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 0 | 🐍 **Python basics for today** — the Python used in this day, explained very simply (no API key needed) | open 00_python_basics.ipynb |
| 1 | Open self_rag_vs_crag_comparison.html | double-click |
| 2 | Advanced RAG notebook (uses the ready FAISS index) | open 01_advance_rag.ipynb |
| 3 | (Optional) rebuild the FAISS index | `cd RAG_embedding; uv run python embedding.py` |
| 4 | Streamlit app | `cd Advance_RAG_App; uv run streamlit run app.py` |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or `uv add jupyterlab` once and run `uv run jupyter lab`.

---
[<- Day_14_LangGraph_MapReduce_and_MultiAgent](../Day_14_LangGraph_MapReduce_and_MultiAgent/00_START_HERE.md) | [Day_16_Short_and_Long_Term_Memory ->](../Day_16_Short_and_Long_Term_Memory/00_START_HERE.md)
