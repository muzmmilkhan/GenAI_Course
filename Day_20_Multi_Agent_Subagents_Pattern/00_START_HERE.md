# Day 20 - Multi-Agent Pattern 1 - Supervisor & Sub-agents

**What you will learn:** A supervisor agent that delegates work to specialist sub-agents (travel planner, personal assistant, deep research).

## Before you start
- Finished [Day 00](../Day_00_Setup_uv_and_Python/00_START_HERE.md) once (your uv project, `.env` and notebook kernel are ready).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_20_Multi_Agent_Subagents_Pattern
  ```
- Keys: `GOOGLE_API_KEY`, `OPENAI_API_KEY`. `reports/` contains reports produced by notebook 03.

## 📦 Step 1 - Install today's packages
Run this in the terminal (from this Day folder or the course root — uv finds your project automatically):
```bash
uv add langchain-opentutorial
```
| Package | What it is for |
|---|---|
| `langchain-opentutorial` | helpers to draw agent graphs |

> 🔎 Afterwards open `pyproject.toml` (course root) and find the new lines. We always install the **latest** versions, so your version numbers may be newer than your classmates' — that's normal.

<details>
<summary>🧯 Something went wrong? Click here</summary>

| You see... | What to do |
|---|---|
| `ModuleNotFoundError: No module named 'langchain_opentutorial'` | the package is not installed — run today's `uv add` command above |
| `No solution found when resolving dependencies` | two packages need versions that don't fit together. Read the error from the bottom, then try `uv add "<package>"` without a version, or limit it: `uv add "<package><X"` (see Day 00). |
| Notebook: `No module named ...` but `uv run` works | select the `.venv (Python 3.12)` kernel from the course folder |
</details>

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 0 | 🐍 **Python basics for today** — the Python used in this day, explained very simply (no API key needed) | open 00_python_basics.ipynb |
| 1 | Overview of all patterns | open visualizations/multi_agent_patterns_visualization.html |
| 2 | Travel planner with sub-agents | open 01_travel_planner_subagents.ipynb |
| 3 | Personal assistant with sub-agents | open 02_personal_assistant_subagents.ipynb |
| 4 | Hierarchical deep research | open 03_deep_research_multi_agent.ipynb |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or `uv add jupyterlab` once and run `uv run jupyter lab`.

---
[<- Day_19_LangChain_Agents_RAG_SQL_Middleware](../Day_19_LangChain_Agents_RAG_SQL_Middleware/00_START_HERE.md) | [Day_21_Multi_Agent_Handoffs_and_Swarm ->](../Day_21_Multi_Agent_Handoffs_and_Swarm/00_START_HERE.md)
