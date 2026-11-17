# Day 13 - Tools & Human-in-the-Loop

**What you will learn:** Let the LLM call tools (search, calculator, stock price) with ToolNode, then pause the graph for human approval (interrupt / resume).

## Before you start
- Finished [Day 00](../Day_00_Setup_uv_and_Python/00_START_HERE.md) once (your uv project, `.env` and notebook kernel are ready).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_13_LangGraph_Tools_and_Human_in_the_Loop
  ```
- Keys: `OPENAI_API_KEY`.

## 📦 Step 1 - Install today's packages
Run this in the terminal (from this Day folder or the course root — uv finds your project automatically):
```bash
uv add ddgs
```
| Package | What it is for |
|---|---|
| `ddgs` | DuckDuckGo search (free web search tool) |

> 🔎 Afterwards open `pyproject.toml` (course root) and find the new lines. We always install the **latest** versions, so your version numbers may be newer than your classmates' — that's normal.

<details>
<summary>🧯 Something went wrong? Click here</summary>

| You see... | What to do |
|---|---|
| `ModuleNotFoundError: No module named 'ddgs'` | the package is not installed — run today's `uv add` command above |
| `No solution found when resolving dependencies` | two packages need versions that don't fit together. Read the error from the bottom, then try `uv add "<package>"` without a version, or limit it: `uv add "<package><X"` (see Day 00). |
| Notebook: `No module named ...` but `uv run` works | select the `.venv (Python 3.12)` kernel from the course folder |
</details>

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 0 | 🐍 **Python basics for today** — the Python used in this day, explained very simply (no API key needed) | open 00_python_basics.ipynb |
| 1 | Tool calling | open 01_tools.ipynb |
| 2 | Human-in-the-loop | open 02_human_in_the_loop.ipynb |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or `uv add jupyterlab` once and run `uv run jupyter lab`.

---
[<- Day_12_LangGraph_Memory_and_Persistence](../Day_12_LangGraph_Memory_and_Persistence/00_START_HERE.md) | [Day_14_LangGraph_MapReduce_and_MultiAgent ->](../Day_14_LangGraph_MapReduce_and_MultiAgent/00_START_HERE.md)
