# Day 32 - Production - Human-in-the-Loop LinkedIn Agent

**What you will learn:** A production-style LangGraph app: draft -> human review -> revise -> publish, with FastAPI, SQLite checkpoints, tests, Docker and CI/CD.

## Before you start
- Do the one-time setup in the [course README](../README.md) (`uv sync` + `.env`).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_32_Production_HITL_LinkedIn_Agent
  ```
- Keys: see README.md (Gemini/OpenAI + LinkedIn). `docker/` keeps this project's own lock file for the Docker image.

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 1 | Read README.md, ARCHITECTURE.md, open architecture_visualization.html | - |
| 2 | Run the app | `uv run python main.py` |
| 3 | Run the tests | `uv run pytest` |
| 4 | Docker | `docker compose up --build   (read DEPLOYMENT.md)` |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or run `uv run jupyter lab` from the course root.

---
[<- Day_31_Project_Voice_Agent](../Day_31_Project_Voice_Agent/00_START_HERE.md) | [Day_33_Production_RAG_Pipeline ->](../Day_33_Production_RAG_Pipeline/00_START_HERE.md)
