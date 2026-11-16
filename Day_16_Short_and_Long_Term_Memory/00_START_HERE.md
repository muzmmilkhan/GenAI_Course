# Day 16 - Short-Term & Long-Term Memory

**What you will learn:** Trim / summarise chat history (short-term) and store facts about the user across sessions (long-term) in memory and in Postgres.

## Before you start
- Do the one-time setup in the [course README](../README.md) (`uv sync` + `.env`).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_16_Short_and_Long_Term_Memory
  ```
- Keys: `OPENAI_API_KEY`, `GOOGLE_API_KEY`. Needs Docker Desktop for notebook 03 (Postgres on port 5442).

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 1 | Short-term memory (trimming, summarising) | open 01_short_term_memory.ipynb |
| 2 | Long-term memory with InMemoryStore | open 02_long_term_memory_inmemorystore.ipynb |
| 3 | Start Postgres | `docker compose up -d` |
| 4 | Long-term memory in Postgres | open 03_long_term_memory_postgres.ipynb |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or run `uv run jupyter lab` from the course root.

---
[<- Day_15_Advanced_RAG_with_LangGraph](../Day_15_Advanced_RAG_with_LangGraph/00_START_HERE.md) | [Day_17_Project_WhatsApp_Agent ->](../Day_17_Project_WhatsApp_Agent/00_START_HERE.md)
