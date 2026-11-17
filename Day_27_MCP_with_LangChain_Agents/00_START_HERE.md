# Day 27 - MCP + LangChain Agents

**What you will learn:** Connect an agent to several MCP servers at once (AWS documentation + browser automation) and give it a chat UI.

## Before you start
- Finished [Day 00](../Day_00_Setup_uv_and_Python/00_START_HERE.md) once (your uv project, `.env` and notebook kernel are ready).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_27_MCP_with_LangChain_Agents
  ```
- Keys: `GOOGLE_API_KEY`. Needs `uvx` (comes with uv) and Node.js `npx` for the MCP servers.

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
| `uvx` / `npx` not found | `uvx` comes with uv. `npx` comes with Node.js (macOS: `brew install node` · Windows: `winget install OpenJS.NodeJS.LTS`), then reopen the terminal. |
</details>

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 0 | 🐍 **Python basics for today** — the Python used in this day, explained very simply (no API key needed) | open 00_python_basics.ipynb |
| 1 | Architecture | open aws_browser_mcp_visualization.html |
| 2 | Notebook | open 01_aws_docs_and_browser_mcp_agent.ipynb |
| 3 | Chat UI backend | `cd mcp_agent_ui/backend; uv run uvicorn main:app --reload --port 8000` |
| 4 | Chat UI frontend | open mcp_agent_ui/frontend/index.html |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or `uv add jupyterlab` once and run `uv run jupyter lab`.

---
[<- Day_26_MCP_ML_Model_Server_Salary_Prediction](../Day_26_MCP_ML_Model_Server_Salary_Prediction/00_START_HERE.md) | [Day_28_Remote_MCP_FreeCAD ->](../Day_28_Remote_MCP_FreeCAD/00_START_HERE.md)
