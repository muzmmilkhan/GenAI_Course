# Day 16 - Short-Term & Long-Term Memory

**What you will learn:** Trim / summarise chat history (short-term) and store facts about the user across sessions (long-term) in memory and in Postgres.

## Before you start
- Finished [Day 00](../Day_00_Setup_uv_and_Python/00_START_HERE.md) once (your uv project, `.env` and notebook kernel are ready).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_16_Short_and_Long_Term_Memory
  ```
- Keys: `OPENAI_API_KEY`, `GOOGLE_API_KEY`. Needs Docker Desktop for notebook 03 (Postgres on port 5442).

## 📦 Step 1 - Install today's packages
Run this in the terminal (from this Day folder or the course root — uv finds your project automatically):
```bash
uv add langgraph-checkpoint-postgres "psycopg[binary]"
```
| Package | What it is for |
|---|---|
| `langgraph-checkpoint-postgres` | save memory and long-term store in PostgreSQL |
| `psycopg[binary]` | the PostgreSQL driver for Python |

> 🔎 Afterwards open `pyproject.toml` (course root) and find the new lines. We always install the **latest** versions, so your version numbers may be newer than your classmates' — that's normal.

<details>
<summary>🧯 Something went wrong? Click here</summary>

| You see... | What to do |
|---|---|
| `ModuleNotFoundError: No module named 'langgraph.checkpoint.postgres'` | the package is not installed — run today's `uv add` command above |
| `No solution found when resolving dependencies` | two packages need versions that don't fit together. Read the error from the bottom, then try `uv add "<package>"` without a version, or limit it: `uv add "<package><X"` (see Day 00). |
| Notebook: `No module named ...` but `uv run` works | select the `.venv (Python 3.12)` kernel from the course folder |
| `connection refused` on port 5442 | Postgres is not running. Start Docker Desktop, then run `docker compose up -d` in this folder. |
</details>

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 0 | 🐍 **Python basics for today** — the Python used in this day, explained very simply (no API key needed) | open 00_python_basics.ipynb |
| 1 | Short-term memory (trimming, summarising) | open 01_short_term_memory.ipynb |
| 2 | Long-term memory with InMemoryStore | open 02_long_term_memory_inmemorystore.ipynb |
| 3 | Start Postgres | `docker compose up -d` |
| 4 | Long-term memory in Postgres | open 03_long_term_memory_postgres.ipynb |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or `uv add jupyterlab` once and run `uv run jupyter lab`.

---
[<- Day_15_Advanced_RAG_with_LangGraph](../Day_15_Advanced_RAG_with_LangGraph/00_START_HERE.md) | [Day_17_Project_WhatsApp_Agent ->](../Day_17_Project_WhatsApp_Agent/00_START_HERE.md)
