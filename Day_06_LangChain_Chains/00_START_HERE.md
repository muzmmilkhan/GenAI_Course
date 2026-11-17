# Day 06 - LangChain Chains (LCEL)

**What you will learn:** Connect prompts, models and parsers with the `|` operator: simple, sequential, parallel and conditional (branching) chains.

## Before you start
- Finished [Day 00](../Day_00_Setup_uv_and_Python/00_START_HERE.md) once (your uv project, `.env` and notebook kernel are ready).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_06_LangChain_Chains
  ```
- Keys: `OPENAI_API_KEY`.

## 📦 Step 1 - Install today's packages
✅ **Nothing new to install today** — everything you need was installed on earlier days.

Check what you have so far with `uv tree --depth 1`.

<details>
<summary>🧯 Something went wrong? Click here</summary>

| You see... | What to do |
|---|---|
| `ModuleNotFoundError: No module named ...` | a package from an earlier day is missing — check that day's 📦 step, or run `uv sync` |
| `No solution found when resolving dependencies` | two packages need versions that don't fit together. Read the error from the bottom, then try `uv add "<package>"` without a version, or limit it: `uv add "<package><X"` (see Day 00). |
| Notebook: `No module named ...` but `uv run` works | select the `.venv (Python 3.12)` kernel from the course folder |
</details>

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 0 | 🐍 **Python basics for today** — the Python used in this day, explained very simply (no API key needed) | open 00_python_basics.ipynb |
| 1 | Simple chain | `uv run python 1_simple_chain.py` |
| 2 | Sequential chain | `uv run python 2_sequential_chain.py` |
| 3 | Parallel chain | `uv run python 3_parallel_chain.py` |
| 4 | Conditional chain | `uv run python 4_conditional_chain.py` |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or `uv add jupyterlab` once and run `uv run jupyter lab`.

---
[<- Day_05_Structured_Output_and_Parsers](../Day_05_Structured_Output_and_Parsers/00_START_HERE.md) | [Day_07_RAG_Fundamentals ->](../Day_07_RAG_Fundamentals/00_START_HERE.md)
