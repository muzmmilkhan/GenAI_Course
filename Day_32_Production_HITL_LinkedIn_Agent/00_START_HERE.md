# Day 32 - Production - Human-in-the-Loop LinkedIn Agent

**What you will learn:** A production-style LangGraph app: draft -> human review -> revise -> publish, with FastAPI, SQLite checkpoints, tests, Docker and CI/CD.

## Before you start
- Finished [Day 00](../Day_00_Setup_uv_and_Python/00_START_HERE.md) once (your uv project, `.env` and notebook kernel are ready).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_32_Production_HITL_LinkedIn_Agent
  ```
- Keys: see README.md (Gemini/OpenAI + LinkedIn). `docker/` keeps this project's own lock file for the Docker image.

## 📦 Step 1 - Install today's packages
Run this in the terminal (from this Day folder or the course root — uv finds your project automatically):
```bash
uv add pydantic-settings jinja2
uv add --dev pytest
```
| Package | What it is for |
|---|---|
| `pydantic-settings` | read settings from .env into a class |
| `jinja2` | HTML templates |
| `pytest` | run tests (a *dev* dependency: needed while developing, not in production) |

> 🔎 Afterwards open `pyproject.toml` (course root) and find the new lines. We always install the **latest** versions, so your version numbers may be newer than your classmates' — that's normal.

<details>
<summary>🧯 Something went wrong? Click here</summary>

| You see... | What to do |
|---|---|
| `ModuleNotFoundError: No module named 'pydantic_settings'` | the package is not installed — run today's `uv add` command above |
| `No solution found when resolving dependencies` | two packages need versions that don't fit together. Read the error from the bottom, then try `uv add "<package>"` without a version, or limit it: `uv add "<package><X"` (see Day 00). |
| Notebook: `No module named ...` but `uv run` works | select the `.venv (Python 3.12)` kernel from the course folder |
</details>

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 0 | 🐍 **Python basics for today** — the Python used in this day, explained very simply (no API key needed) | open 00_python_basics.ipynb |
| 1 | Read README.md, ARCHITECTURE.md, open architecture_visualization.html | - |
| 2 | Run the app | `uv run python main.py` |
| 3 | Run the tests | `uv run pytest` |
| 4 | Docker | `docker compose up --build   (read DEPLOYMENT.md)` |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or `uv add jupyterlab` once and run `uv run jupyter lab`.

---
[<- Day_31_Project_Voice_Agent](../Day_31_Project_Voice_Agent/00_START_HERE.md) | [Day_33_Production_RAG_Pipeline ->](../Day_33_Production_RAG_Pipeline/00_START_HERE.md)
