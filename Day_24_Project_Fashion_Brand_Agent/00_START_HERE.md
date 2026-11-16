# Day 24 - Project - Fashion Brand Shopping Agent

**What you will learn:** A shopping assistant agent that queries a MySQL product catalogue, with a FastAPI backend and HTML frontend.

## Before you start
- Do the one-time setup in the [course README](../README.md) (`uv sync` + `.env`).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_24_Project_Fashion_Brand_Agent
  ```
- Keys: `GROQ_API_KEY` + MySQL settings (`MYSQL_*`) in `.env`. Needs a running MySQL server.

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 1 | Create the database | `cd backend && uv run python setup_fashion_db.py` |
| 2 | Start the API | `uv run python main.py` |
| 3 | Open the UI | open ../frontend/index.html |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or run `uv run jupyter lab` from the course root.

---
[<- Day_23_Project_Trip_Planner_Multi_Agent](../Day_23_Project_Trip_Planner_Multi_Agent/00_START_HERE.md) | [Day_25_MCP_Fundamentals_and_Servers ->](../Day_25_MCP_Fundamentals_and_Servers/00_START_HERE.md)
