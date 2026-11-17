# Day 31 - Project - Real-Time Voice Agent

**What you will learn:** Speech-to-text -> agent -> text-to-speech, streamed over WebSockets with async Python.

## Before you start
- Finished [Day 00](../Day_00_Setup_uv_and_Python/00_START_HERE.md) once (your uv project, `.env` and notebook kernel are ready).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_31_Project_Voice_Agent
  ```
- Keys: `ASSEMBLYAI_API_KEY`, `CARTESIA_API_KEY`, `SENSENOVA_API_KEY` (or `OPENAI_API_KEY`).

## 📦 Step 1 - Install today's packages
Run this in the terminal (from this Day folder or the course root — uv finds your project automatically):
```bash
uv add assemblyai cartesia
```
| Package | What it is for |
|---|---|
| `assemblyai` | speech-to-text |
| `cartesia` | text-to-speech |

> 🔎 Afterwards open `pyproject.toml` (course root) and find the new lines. We always install the **latest** versions, so your version numbers may be newer than your classmates' — that's normal.

<details>
<summary>🧯 Something went wrong? Click here</summary>

| You see... | What to do |
|---|---|
| `ModuleNotFoundError: No module named 'assemblyai'` | the package is not installed — run today's `uv add` command above |
| `No solution found when resolving dependencies` | two packages need versions that don't fit together. Read the error from the bottom, then try `uv add "<package>"` without a version, or limit it: `uv add "<package><X"` (see Day 00). |
| Notebook: `No module named ...` but `uv run` works | select the `.venv (Python 3.12)` kernel from the course folder |
</details>

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 0 | 🐍 **Python basics for today** — the Python used in this day, explained very simply (no API key needed) | open 00_python_basics.ipynb |
| 1 | Streaming & async explained | open streaming_and_agent_async_explained.ipynb and WEBSOCKET_EXPLAINED.md |
| 2 | Read README.md | - |
| 3 | Start the server -> http://127.0.0.1:8000 | `uv run python server.py` |
| 4 | End-to-end test | `uv run python test_end_to_end.py` |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or `uv add jupyterlab` once and run `uv run jupyter lab`.

---
[<- Day_30_Project_PPT_Agent](../Day_30_Project_PPT_Agent/00_START_HERE.md) | [Day_32_Production_HITL_LinkedIn_Agent ->](../Day_32_Production_HITL_LinkedIn_Agent/00_START_HERE.md)
