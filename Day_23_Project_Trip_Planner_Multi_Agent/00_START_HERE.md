# Day 23 - Project - Multi-Agent Trip Planner

**What you will learn:** A full app: hotel + flight sub-agents, human approval before booking, SQLite persistence, FastAPI backend with web UI.

## Before you start
- Finished [Day 00](../Day_00_Setup_uv_and_Python/00_START_HERE.md) once (your uv project, `.env` and notebook kernel are ready).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_23_Project_Trip_Planner_Multi_Agent
  ```
- Keys: `GOOGLE_API_KEY`.

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
| 1 | Architecture | open trip_planner_visualization.html |
| 2 | Notebook walkthrough | open Trip_Planner_Subagents_HITL_Notebook.ipynb |
| 3 | Run the web app -> http://localhost:8000 | `uv run python app.py` |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or `uv add jupyterlab` once and run `uv run jupyter lab`.

---
[<- Day_22_MapReduce_and_Router_Agents](../Day_22_MapReduce_and_Router_Agents/00_START_HERE.md) | [Day_24_Project_Fashion_Brand_Agent ->](../Day_24_Project_Fashion_Brand_Agent/00_START_HERE.md)
