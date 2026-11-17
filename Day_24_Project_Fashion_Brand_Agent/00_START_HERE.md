# Day 24 - Project - Fashion Brand Shopping Agent

**What you will learn:** A shopping assistant agent that queries a MySQL product catalogue, with a FastAPI backend and HTML frontend.

## Before you start
- Finished [Day 00](../Day_00_Setup_uv_and_Python/00_START_HERE.md) once (your uv project, `.env` and notebook kernel are ready).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_24_Project_Fashion_Brand_Agent
  ```
- Keys: `GROQ_API_KEY` + MySQL settings (`MYSQL_*`) in `.env`. Needs a running MySQL server.

## 📦 Step 1 - Install today's packages
Run this in the terminal (from this Day folder or the course root — uv finds your project automatically):
```bash
uv add langchain-groq mysql-connector-python
```
| Package | What it is for |
|---|---|
| `langchain-groq` | very fast Groq-hosted models |
| `mysql-connector-python` | connect to a MySQL database |

> 🔎 Afterwards open `pyproject.toml` (course root) and find the new lines. We always install the **latest** versions, so your version numbers may be newer than your classmates' — that's normal.

<details>
<summary>🧯 Something went wrong? Click here</summary>

| You see... | What to do |
|---|---|
| `ModuleNotFoundError: No module named 'langchain_groq'` | the package is not installed — run today's `uv add` command above |
| `No solution found when resolving dependencies` | two packages need versions that don't fit together. Read the error from the bottom, then try `uv add "<package>"` without a version, or limit it: `uv add "<package><X"` (see Day 00). |
| Notebook: `No module named ...` but `uv run` works | select the `.venv (Python 3.12)` kernel from the course folder |
| `Can't connect to MySQL server` | Install and start MySQL (macOS: `brew install mysql`, then `brew services start mysql` · Windows: `winget install Oracle.MySQL` · or with Docker: `docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=pass mysql:8`) and check the `MYSQL_*` values in `.env`. |
</details>

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 0 | 🐍 **Python basics for today** — the Python used in this day, explained very simply (no API key needed) | open 00_python_basics.ipynb |
| 1 | Create the database | `cd backend; uv run python setup_fashion_db.py` |
| 2 | Start the API | `uv run python main.py` |
| 3 | Open the UI | open ../frontend/index.html |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or `uv add jupyterlab` once and run `uv run jupyter lab`.

---
[<- Day_23_Project_Trip_Planner_Multi_Agent](../Day_23_Project_Trip_Planner_Multi_Agent/00_START_HERE.md) | [Day_25_MCP_Fundamentals_and_Servers ->](../Day_25_MCP_Fundamentals_and_Servers/00_START_HERE.md)
