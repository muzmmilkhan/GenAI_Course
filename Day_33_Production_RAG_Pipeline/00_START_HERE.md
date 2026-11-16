# Day 33 - Production - Multi-modal Financial RAG Pipeline

**What you will learn:** PDF pages -> images -> Gemini embeddings -> Qdrant, with a file watcher, an S3 worker, a FastAPI service, Docker and AWS CI/CD.

## Before you start
- Do the one-time setup in the [course README](../README.md) (`uv sync` + `.env`).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_33_Production_RAG_Pipeline
  ```
- Keys: `GOOGLE_API_KEY`, `GROQ_API_KEY`; AWS keys only for S3 / deployment. `data/*.pdf` are links to `shared_data/financial_pdfs`.

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 1 | Start Qdrant (Docker) | `./start_qdrant.sh` |
| 2 | Index the PDFs in data/ | `./run_watcher.sh` |
| 3 | Start the API | `uv run uvicorn src.generation_service.app:app --port 8080` |
| 4 | Open the web UI | `./run_ui.sh` |
| 5 | Full stack with Docker | `docker compose up --build` |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or run `uv run jupyter lab` from the course root.

---
[<- Day_32_Production_HITL_LinkedIn_Agent](../Day_32_Production_HITL_LinkedIn_Agent/00_START_HERE.md) | [Day_34_RAG_Evaluation_DeepEval ->](../Day_34_RAG_Evaluation_DeepEval/00_START_HERE.md)
