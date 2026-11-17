# Day 08 - RAG Chunking Strategies & Multi-modal RAG

**What you will learn:** How you split documents changes answer quality: recursive, semantic and agentic (LLM-driven) chunking, plus RAG over PDFs with images and tables.

## Before you start
- Finished [Day 00](../Day_00_Setup_uv_and_Python/00_START_HERE.md) once (your uv project, `.env` and notebook kernel are ready).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_08_RAG_Chunking_Strategies
  ```
- Keys: `OPENAI_API_KEY`, `GOOGLE_API_KEY`. Notebook 8 needs the system tools Poppler and Tesseract (install commands for macOS / Windows / Linux are in the [Day 00 table](../Day_00_Setup_uv_and_Python/00_START_HERE.md)). `dbv2/` is the vector DB the notebook builds.

## 📦 Step 1 - Install today's packages
Run this in the terminal (from this Day folder or the course root — uv finds your project automatically):
```bash
uv add langchain-experimental "unstructured[pdf]"
```
| Package | What it is for |
|---|---|
| `langchain-experimental` | experimental features such as SemanticChunker |
| `unstructured[pdf]` | read PDFs including tables and images (needs poppler + tesseract, see below) |

> 🔎 Afterwards open `pyproject.toml` (course root) and find the new lines. We always install the **latest** versions, so your version numbers may be newer than your classmates' — that's normal.

<details>
<summary>🧯 Something went wrong? Click here</summary>

| You see... | What to do |
|---|---|
| `ModuleNotFoundError: No module named 'langchain_experimental'` | the package is not installed — run today's `uv add` command above |
| `No solution found when resolving dependencies` | two packages need versions that don't fit together. Read the error from the bottom, then try `uv add "<package>"` without a version, or limit it: `uv add "<package><X"` (see Day 00). |
| Notebook: `No module named ...` but `uv run` works | select the `.venv (Python 3.12)` kernel from the course folder |
| `PDFInfoNotInstalledError` or `TesseractNotFoundError` | These are system programs, not Python packages. macOS: `brew install poppler tesseract libmagic` · Windows: `winget install oschwartz10612.Poppler` and `winget install UB-Mannheim.TesseractOCR`, then reopen the terminal · Linux: `sudo apt install poppler-utils tesseract-ocr libmagic1`. |
</details>

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 0 | 🐍 **Python basics for today** — the Python used in this day, explained very simply (no API key needed) | open 00_python_basics.ipynb |
| 1 | Recursive character splitter | `uv run python 5_recursive_character_text_splitter.py` |
| 2 | Semantic chunking | `uv run python 6_semantic_chunking.py` |
| 3 | Agentic chunking | `uv run python 7_agentic_chunking.py` |
| 4 | Multi-modal RAG on docs/attention-is-all-you-need.pdf | open 8_multi_modal_rag.ipynb |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or `uv add jupyterlab` once and run `uv run jupyter lab`.

---
[<- Day_07_RAG_Fundamentals](../Day_07_RAG_Fundamentals/00_START_HERE.md) | [Day_09_RAG_Advanced_Retrieval ->](../Day_09_RAG_Advanced_Retrieval/00_START_HERE.md)
