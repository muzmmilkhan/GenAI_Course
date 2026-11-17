# Day 14 - Map-Reduce & Your First Multi-Agent System

**What you will learn:** Process many documents in parallel with Send() (map-reduce over financial PDFs) and build a research agent + chart agent team.

## Before you start
- Finished [Day 00](../Day_00_Setup_uv_and_Python/00_START_HERE.md) once (your uv project, `.env` and notebook kernel are ready).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_14_LangGraph_MapReduce_and_MultiAgent
  ```
- Keys: `OPENAI_API_KEY`, `GOOGLE_API_KEY`. `chart.html` and `xray_graph.png` are sample outputs of notebook 02.

## 📦 Step 1 - Install today's packages
Run this in the terminal (from this Day folder or the course root — uv finds your project automatically):
```bash
uv add pdfminer.six plotly
```
| Package | What it is for |
|---|---|
| `pdfminer.six` | extract text from PDFs |
| `plotly` | interactive charts |

> 🔎 Afterwards open `pyproject.toml` (course root) and find the new lines. We always install the **latest** versions, so your version numbers may be newer than your classmates' — that's normal.

<details>
<summary>🧯 Something went wrong? Click here</summary>

| You see... | What to do |
|---|---|
| `ModuleNotFoundError: No module named 'pdfminer'` | the package is not installed — run today's `uv add` command above |
| `No solution found when resolving dependencies` | two packages need versions that don't fit together. Read the error from the bottom, then try `uv add "<package>"` without a version, or limit it: `uv add "<package><X"` (see Day 00). |
| Notebook: `No module named ...` but `uv run` works | select the `.venv (Python 3.12)` kernel from the course folder |
</details>

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 0 | 🐍 **Python basics for today** — the Python used in this day, explained very simply (no API key needed) | open 00_python_basics.ipynb |
| 1 | Map-reduce over PDFs in shared_data/financial_pdfs | open 01_map_reduce.ipynb |
| 2 | Multi-agent: researcher + Plotly chart generator | open 02_multiagent_research_and_chart.ipynb |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or `uv add jupyterlab` once and run `uv run jupyter lab`.

---
[<- Day_13_LangGraph_Tools_and_Human_in_the_Loop](../Day_13_LangGraph_Tools_and_Human_in_the_Loop/00_START_HERE.md) | [Day_15_Advanced_RAG_with_LangGraph ->](../Day_15_Advanced_RAG_with_LangGraph/00_START_HERE.md)
