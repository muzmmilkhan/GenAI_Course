# Day 29 - Deep Agents

**What you will learn:** Long-running agents with planning, a virtual filesystem, sub-agents and skills - built into a forensic financial audit agent (DeepAudit).

## Before you start
- Do the one-time setup in the [course README](../README.md) (`uv sync` + `.env`).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_29_Deep_Agents
  ```
- Run commands from inside this Day folder. Keys: `GOOGLE_API_KEY`/`GEMINI_API_KEY`, `SERPAPI_API_KEY`. Generated memos are saved in `reports/`.

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 1 | Overview notebook | open 01_Deep_Agents_Overview.ipynb  (and deep_agents_guide.html) |
| 2 | Read Deep_Agents/deepaudit/README.md | - |
| 3 | Terminal 1 - MCP database server | `uv run python Deep_Agents/deepaudit/mcp_server.py` |
| 4 | Terminal 2 - dashboard | `uv run python Deep_Agents/deepaudit/run_dashboard.py` |
| 5 | Walkthrough notebook | open Deep_Agents/deepaudit/deepaudit_agent_walkthrough.ipynb |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or run `uv run jupyter lab` from the course root.

---
[<- Day_28_Remote_MCP_FreeCAD](../Day_28_Remote_MCP_FreeCAD/00_START_HERE.md) | [Day_30_Project_PPT_Agent ->](../Day_30_Project_PPT_Agent/00_START_HERE.md)
