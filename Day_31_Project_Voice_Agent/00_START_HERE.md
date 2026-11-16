# Day 31 - Project - Real-Time Voice Agent

**What you will learn:** Speech-to-text -> agent -> text-to-speech, streamed over WebSockets with async Python.

## Before you start
- Do the one-time setup in the [course README](../README.md) (`uv sync` + `.env`).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_31_Project_Voice_Agent
  ```
- Keys: `ASSEMBLYAI_API_KEY`, `CARTESIA_API_KEY`, `SENSENOVA_API_KEY` (or `OPENAI_API_KEY`).

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 1 | Streaming & async explained | open streaming_and_agent_async_explained.ipynb and WEBSOCKET_EXPLAINED.md |
| 2 | Read README.md | - |
| 3 | Start the server -> http://127.0.0.1:8000 | `uv run python server.py` |
| 4 | End-to-end test | `uv run python test_end_to_end.py` |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or run `uv run jupyter lab` from the course root.

---
[<- Day_30_Project_PPT_Agent](../Day_30_Project_PPT_Agent/00_START_HERE.md) | [Day_32_Production_HITL_LinkedIn_Agent ->](../Day_32_Production_HITL_LinkedIn_Agent/00_START_HERE.md)
