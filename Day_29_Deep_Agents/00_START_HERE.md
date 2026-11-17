# Day 29 - Deep Agents

**What you will learn:** Long-running agents with planning, a virtual filesystem, sub-agents and skills - built into a forensic financial audit agent (DeepAudit).

## Before you start
- Finished [Day 00](../Day_00_Setup_uv_and_Python/00_START_HERE.md) once (your uv project, `.env` and notebook kernel are ready).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_29_Deep_Agents
  ```
- Run commands from inside this Day folder. Keys: `GOOGLE_API_KEY`/`GEMINI_API_KEY`, `SERPAPI_API_KEY`. Generated memos are saved in `reports/`.

## 📦 Step 1 - Install today's packages
Run this in the terminal (from this Day folder or the course root — uv finds your project automatically):
```bash
uv add deepagents nest-asyncio
```
| Package | What it is for |
|---|---|
| `deepagents` | LangChain's Deep Agents (planning, files, sub-agents) |
| `nest-asyncio` | run async code inside Jupyter |

> 🔎 Afterwards open `pyproject.toml` (course root) and find the new lines. We always install the **latest** versions, so your version numbers may be newer than your classmates' — that's normal.

<details>
<summary>🧯 Something went wrong? Click here</summary>

| You see... | What to do |
|---|---|
| `ModuleNotFoundError: No module named 'deepagents'` | the package is not installed — run today's `uv add` command above |
| `No solution found when resolving dependencies` | two packages need versions that don't fit together. Read the error from the bottom, then try `uv add "<package>"` without a version, or limit it: `uv add "<package><X"` (see Day 00). |
| Notebook: `No module named ...` but `uv run` works | select the `.venv (Python 3.12)` kernel from the course folder |
</details>

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 0 | 🐍 **Python basics for today** — the Python used in this day, explained very simply (no API key needed) | open 00_python_basics.ipynb |
| 1 | Overview notebook | open 01_Deep_Agents_Overview.ipynb  (and deep_agents_guide.html) |
| 2 | Read Deep_Agents/deepaudit/README.md | - |
| 3 | Terminal 1 - MCP database server | `uv run python Deep_Agents/deepaudit/mcp_server.py` |
| 4 | Terminal 2 - dashboard | `uv run python Deep_Agents/deepaudit/run_dashboard.py` |
| 5 | Walkthrough notebook | open Deep_Agents/deepaudit/deepaudit_agent_walkthrough.ipynb |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or `uv add jupyterlab` once and run `uv run jupyter lab`.

---
[<- Day_28_Remote_MCP_FreeCAD](../Day_28_Remote_MCP_FreeCAD/00_START_HERE.md) | [Day_30_Project_PPT_Agent ->](../Day_30_Project_PPT_Agent/00_START_HERE.md)
