# Day 19 - LangChain v1 Agents - RAG Agent, SQL Agent & Middleware

**What you will learn:** `create_agent` from LangChain v1: a RAG agent, and a SQL agent protected by human-approval and PII-redaction middleware.

## Before you start
- Finished [Day 00](../Day_00_Setup_uv_and_Python/00_START_HERE.md) once (your uv project, `.env` and notebook kernel are ready).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_19_LangChain_Agents_RAG_SQL_Middleware
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
| 1 | RAG agent | open 01_rag_agent.ipynb |
| 2 | SQL agent + HITL + PII middleware | open 02_sql_agent_hitl_pii_middleware.ipynb |
| 3 | Read LANGCHAIN_STREAMING_RESEARCH.md | - |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or `uv add jupyterlab` once and run `uv run jupyter lab`.

---
[<- Day_18_Planning_and_Deep_Research_Agents](../Day_18_Planning_and_Deep_Research_Agents/00_START_HERE.md) | [Day_20_Multi_Agent_Subagents_Pattern ->](../Day_20_Multi_Agent_Subagents_Pattern/00_START_HERE.md)
