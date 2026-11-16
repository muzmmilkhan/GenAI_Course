# Day 12 - LangGraph Memory & Persistence

**What you will learn:** Checkpointers: make a chatbot remember the conversation (in memory and in SQLite), inspect/replay intermediate states.

## Before you start
- Do the one-time setup in the [course README](../README.md) (`uv sync` + `.env`).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_12_LangGraph_Memory_and_Persistence
  ```
- Keys: `OPENAI_API_KEY`.

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 1 | Chatbot with InMemorySaver | open 01_chatbot_with_inmemory_saver.ipynb |
| 2 | SqliteSaver | `uv run python 02_sqlite_saver.py` |
| 3 | Persistence & time travel | open 03_persistence.ipynb |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or run `uv run jupyter lab` from the course root.

---
[<- Day_11_LangGraph_Basics_Workflows](../Day_11_LangGraph_Basics_Workflows/00_START_HERE.md) | [Day_13_LangGraph_Tools_and_Human_in_the_Loop ->](../Day_13_LangGraph_Tools_and_Human_in_the_Loop/00_START_HERE.md)
