# Day 17 - Project - WhatsApp AI Agent

**What you will learn:** Connect a LangGraph agent to WhatsApp using Twilio, with SQLite chat memory and MongoDB long-term memory.

## Before you start
- Finished [Day 00](../Day_00_Setup_uv_and_Python/00_START_HERE.md) once (your uv project, `.env` and notebook kernel are ready).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_17_Project_WhatsApp_Agent
  ```
- Keys: `OPENAI_API_KEY`, `GOOGLE_API_KEY`, `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `MONGODB_URI`.

## 📦 Step 1 - Install today's packages
Run this in the terminal (from this Day folder or the course root — uv finds your project automatically):
```bash
uv add fastapi "uvicorn[standard]" python-multipart twilio langgraph-store-mongodb
```
| Package | What it is for |
|---|---|
| `fastapi` | build web APIs |
| `uvicorn[standard]` | the web server that runs FastAPI apps |
| `python-multipart` | lets FastAPI read form data (Twilio sends forms) |
| `twilio` | send and receive WhatsApp messages |
| `langgraph-store-mongodb` | long-term memory stored in MongoDB |

> 🔎 Afterwards open `pyproject.toml` (course root) and find the new lines. We always install the **latest** versions, so your version numbers may be newer than your classmates' — that's normal.

<details>
<summary>🧯 Something went wrong? Click here</summary>

| You see... | What to do |
|---|---|
| `ModuleNotFoundError: No module named 'fastapi'` | the package is not installed — run today's `uv add` command above |
| `No solution found when resolving dependencies` | two packages need versions that don't fit together. Read the error from the bottom, then try `uv add "<package>"` without a version, or limit it: `uv add "<package><X"` (see Day 00). |
| Notebook: `No module named ...` but `uv run` works | select the `.venv (Python 3.12)` kernel from the course folder |
| `Form data requires "python-multipart"` | Run `uv add python-multipart` — FastAPI needs it to read Twilio's form data. |
</details>

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 0 | 🐍 **Python basics for today** — the Python used in this day, explained very simply (no API key needed) | open 00_python_basics.ipynb |
| 1 | Prototype in a notebook | open 01_whatsapp_agent.ipynb |
| 2 | Read WhatsApp_Agent_App/README.md | - |
| 3 | Run the server | `cd WhatsApp_Agent_App; uv run uvicorn main:app --port 8000` |
| 4 | Expose it to Twilio | `ngrok http 8000` |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or `uv add jupyterlab` once and run `uv run jupyter lab`.

---
[<- Day_16_Short_and_Long_Term_Memory](../Day_16_Short_and_Long_Term_Memory/00_START_HERE.md) | [Day_18_Planning_and_Deep_Research_Agents ->](../Day_18_Planning_and_Deep_Research_Agents/00_START_HERE.md)
