# Day 33 - Production - Multi-modal Financial RAG Pipeline

**What you will learn:** PDF pages -> images -> Gemini embeddings -> Qdrant, with a file watcher, an S3 worker, a FastAPI service, Docker and AWS CI/CD.

## Before you start
- Finished [Day 00](../Day_00_Setup_uv_and_Python/00_START_HERE.md) once (your uv project, `.env` and notebook kernel are ready).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_33_Production_RAG_Pipeline
  ```
- Keys: `GOOGLE_API_KEY`, `GROQ_API_KEY`; AWS keys only for S3 / deployment. `data/` is the PDF inbox - step 2 fills it from `shared_data/financial_pdfs`.

## 📦 Step 1 - Install today's packages
Run this in the terminal (from this Day folder or the course root — uv finds your project automatically):
```bash
uv add qdrant-client pdf2image boto3 groq
```
| Package | What it is for |
|---|---|
| `qdrant-client` | the Qdrant vector database |
| `pdf2image` | turn PDF pages into images (needs poppler) |
| `boto3` | Amazon Web Services SDK (S3) |
| `groq` | Groq's official SDK |

> 🔎 Afterwards open `pyproject.toml` (course root) and find the new lines. We always install the **latest** versions, so your version numbers may be newer than your classmates' — that's normal.

<details>
<summary>🧯 Something went wrong? Click here</summary>

| You see... | What to do |
|---|---|
| `ModuleNotFoundError: No module named 'qdrant_client'` | the package is not installed — run today's `uv add` command above |
| `No solution found when resolving dependencies` | two packages need versions that don't fit together. Read the error from the bottom, then try `uv add "<package>"` without a version, or limit it: `uv add "<package><X"` (see Day 00). |
| Notebook: `No module named ...` but `uv run` works | select the `.venv (Python 3.12)` kernel from the course folder |
| `connection refused` on port 6333 | Qdrant is not running: `docker compose up -d qdrant` (needs Docker Desktop). |
| The web UI can't reach the API | Type `http://localhost:8080` into the API URL box at the top of the page (the default address is the original author's server). |
| `No PDF files found` | The `data/` inbox is empty: `uv run python ../shared_data/copy_pdfs.py data`. |
</details>

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 0 | 🐍 **Python basics for today** — the Python used in this day, explained very simply (no API key needed) | open 00_python_basics.ipynb |
| 1 | Start Qdrant (Docker) | `docker compose up -d qdrant` |
| 2 | Copy the course PDFs into the `data/` inbox | `uv run python ../shared_data/copy_pdfs.py data` |
| 3 | Index the PDFs (leave it running - it watches `data/` for new files) | `uv run python -u watcher.py` |
| 4 | Start the API (2nd terminal) | `uv run uvicorn src.generation_service.app:app --port 8080` |
| 5 | Serve the web UI (3rd terminal), open http://localhost:8081 and type `http://localhost:8080` in the API URL box | `uv run python -m http.server 8081 --directory UI` |
| 6 | Full stack with Docker | `docker compose up --build` |

> 🍎🐧 On macOS/Linux the scripts `start_qdrant.sh`, `run_watcher.sh` and `run_ui.sh` do steps 1, 3 and 5 for you.

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or `uv add jupyterlab` once and run `uv run jupyter lab`.

---
[<- Day_32_Production_HITL_LinkedIn_Agent](../Day_32_Production_HITL_LinkedIn_Agent/00_START_HERE.md) | [Day_34_RAG_Evaluation_DeepEval ->](../Day_34_RAG_Evaluation_DeepEval/00_START_HERE.md)
