# Day 25 - MCP Fundamentals - Model Context Protocol

**What you will learn:** What MCP is, build MCP servers (filesystem, email copilot, health monitor) and an MCP client with a Streamlit chat UI.

## Before you start
- Finished [Day 00](../Day_00_Setup_uv_and_Python/00_START_HERE.md) once (your uv project, `.env` and notebook kernel are ready).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_25_MCP_Fundamentals_and_Servers
  ```
- Keys: one of `OPENAI_API_KEY` / `ANTHROPIC_API_KEY` / `GROQ_API_KEY`. Health monitor needs Docker (Postgres + Redis).

## 📦 Step 1 - Install today's packages
Run this in the terminal (from this Day folder or the course root — uv finds your project automatically):
```bash
uv add "mcp<2" fastmcp openai anthropic pyyaml httpx
uv add google-auth-oauthlib sqlmodel asyncpg greenlet "python-jose[cryptography]" bcrypt redis
```
| Package | What it is for |
|---|---|
| `mcp<2` | the official Model Context Protocol SDK. ⚠️ We ask for **below version 2** on purpose: mcp 2.0 renamed `FastMCP` and `langchain-mcp-adapters` (Day 26) does not support it yet. This is how you say *latest, but not 2.x* |
| `fastmcp` | the easy way to build MCP servers and clients |
| `openai` | OpenAI's official SDK |
| `anthropic` | Anthropic's official SDK (Claude) |
| `pyyaml` | read YAML config files |
| `httpx` | modern HTTP client (sync and async) |
| `google-auth-oauthlib` | Gmail login for the email copilot |
| `sqlmodel` | SQL databases with Pydantic-style models (health monitor) |
| `asyncpg` | async PostgreSQL driver |
| `greenlet` | needed by SQLAlchemy's async mode |
| `python-jose[cryptography]` | create and check login tokens (JWT) |
| `bcrypt` | hash passwords safely |
| `redis` | talk to Redis (live vitals) |

> 🔎 Afterwards open `pyproject.toml` (course root) and find the new lines. We always install the **latest** versions, so your version numbers may be newer than your classmates' — that's normal.

<details>
<summary>🧯 Something went wrong? Click here</summary>

| You see... | What to do |
|---|---|
| `ModuleNotFoundError: No module named 'mcp'` | the package is not installed — run today's `uv add` command above |
| `No solution found when resolving dependencies` | two packages need versions that don't fit together. Read the error from the bottom, then try `uv add "<package>"` without a version, or limit it: `uv add "<package><X"` (see Day 00). |
| Notebook: `No module named ...` but `uv run` works | select the `.venv (Python 3.12)` kernel from the course folder |
| `ImportError ... mcp.server.fastmcp` or `RequestContext` | You have mcp 2.x. Run `uv add "mcp<2"` (see the ⚠️ note above). |
| `.sh` script won't run on Windows | Use Git Bash, or follow `health-monitor/docs/START_EVERYTHING.md` step by step in PowerShell. |
</details>

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 0 | 🐍 **Python basics for today** — the Python used in this day, explained very simply (no API key needed) | open 00_python_basics.ipynb |
| 1 | Architecture | open "MCP architecture.html" and resource.html |
| 2 | Filesystem server in MCP Inspector | `uv run fastmcp dev filesystem-server/server.py` |
| 3 | Email copilot server | `uv run fastmcp dev email-copilot/server.py` |
| 4 | Client chat UI (connects to all servers) | `cd mcp-client; uv run streamlit run app.py` |
| 5 | Health monitor (bigger project) | read health-monitor/README.md |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or `uv add jupyterlab` once and run `uv run jupyter lab`.

---
[<- Day_24_Project_Fashion_Brand_Agent](../Day_24_Project_Fashion_Brand_Agent/00_START_HERE.md) | [Day_26_MCP_ML_Model_Server_Salary_Prediction ->](../Day_26_MCP_ML_Model_Server_Salary_Prediction/00_START_HERE.md)
