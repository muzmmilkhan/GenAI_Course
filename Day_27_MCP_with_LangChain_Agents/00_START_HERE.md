# Day 27 - MCP + LangChain Agents

**What you will learn:** Connect an agent to several MCP servers at once (AWS documentation + browser automation) and give it a chat UI.

## Before you start
- Do the one-time setup in the [course README](../README.md) (`uv sync` + `.env`).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_27_MCP_with_LangChain_Agents
  ```
- Keys: `GOOGLE_API_KEY`. Needs `uvx` (comes with uv) and Node.js `npx` for the MCP servers.

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 1 | Architecture | open aws_browser_mcp_visualization.html |
| 2 | Notebook | open 01_aws_docs_and_browser_mcp_agent.ipynb |
| 3 | Chat UI backend | `cd mcp_agent_ui/backend && uv run uvicorn main:app --reload --port 8000` |
| 4 | Chat UI frontend | open mcp_agent_ui/frontend/index.html |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or run `uv run jupyter lab` from the course root.

---
[<- Day_26_MCP_ML_Model_Server_Salary_Prediction](../Day_26_MCP_ML_Model_Server_Salary_Prediction/00_START_HERE.md) | [Day_28_Remote_MCP_FreeCAD ->](../Day_28_Remote_MCP_FreeCAD/00_START_HERE.md)
