# Day 25 - MCP Fundamentals - Model Context Protocol

**What you will learn:** What MCP is, build MCP servers (filesystem, email copilot, health monitor) and an MCP client with a Streamlit chat UI.

## Before you start
- Do the one-time setup in the [course README](../README.md) (`uv sync` + `.env`).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_25_MCP_Fundamentals_and_Servers
  ```
- Keys: one of `OPENAI_API_KEY` / `ANTHROPIC_API_KEY` / `GROQ_API_KEY`. Health monitor needs Docker (Postgres + Redis).

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 1 | Architecture | open "MCP architecture.html" and resource.html |
| 2 | Filesystem server in MCP Inspector | `uv run fastmcp dev filesystem-server/server.py` |
| 3 | Email copilot server | `uv run fastmcp dev email-copilot/server.py` |
| 4 | Client chat UI (connects to all servers) | `cd mcp-client && uv run streamlit run app.py` |
| 5 | Health monitor (bigger project) | read health-monitor/README.md |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or run `uv run jupyter lab` from the course root.

---
[<- Day_24_Project_Fashion_Brand_Agent](../Day_24_Project_Fashion_Brand_Agent/00_START_HERE.md) | [Day_26_MCP_ML_Model_Server_Salary_Prediction ->](../Day_26_MCP_ML_Model_Server_Salary_Prediction/00_START_HERE.md)
