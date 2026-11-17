# Day 34 - Evaluating RAG with DeepEval

**What you will learn:** Golden datasets, retriever / generator / pipeline metrics, LLM-as-judge, safety, cost & latency evaluation and regression gates.

## Before you start
- Finished [Day 00](../Day_00_Setup_uv_and_Python/00_START_HERE.md) once (your uv project, `.env` and notebook kernel are ready).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_34_RAG_Evaluation_DeepEval
  ```
- Keys: `GOOGLE_API_KEY`, `GROQ_API_KEY`, `OPENAI_API_KEY` (judge). Needs Qdrant from Day 33 (`QDRANT_URL`).

## 📦 Step 1 - Install today's packages
### 🧪 Today you create a **separate environment**
The newest **DeepEval** needs `click<8.4`, but the newest `huggingface-hub` (used since Day 03) needs `click>=8.4.2`. Both can't be true in one environment. Real teams solve this by giving each app **its own environment** — so today's project lives *inside this Day folder* with its own `pyproject.toml`, `uv.lock` and `.venv`. `uv run` always uses the project of the folder you are in.

Run these commands **inside this Day folder**:
```bash
uv init --bare --python ">=3.12,<3.13"
uv python pin 3.12
uv add python-dotenv ipykernel deepeval langchain-openai langchain-google-genai langchain-groq langchain-text-splitters qdrant-client sentence-transformers streamlit fastapi "uvicorn[standard]" python-multipart boto3 pdf2image pypdf pillow groq google-genai openai langsmith
```
| Package | What it is for |
|---|---|
| `deepeval` | evaluate LLM apps with metrics and LLM judges |
| `everything else` | the RAG app being evaluated (you know these packages from earlier days) |

> 📓 For notebooks today choose the kernel **`.venv` from this Day folder** (not the course root one).
>
> 🔎 Afterwards open `pyproject.toml` (in this Day folder) and find the new lines. We always install the **latest** versions, so your version numbers may be newer than your classmates' — that's normal.

<details>
<summary>🧯 Something went wrong? Click here</summary>

| You see... | What to do |
|---|---|
| `ModuleNotFoundError: No module named 'deepeval'` | the package is not installed — run today's `uv add` command above |
| `ModuleNotFoundError` although you installed it on an earlier day | today uses its **own** environment - install it here too (it's already in today's command), and run everything from inside this Day folder |
| `No solution found when resolving dependencies` | two packages need versions that don't fit together. Read the error from the bottom, then try `uv add "<package>"` without a version, or limit it: `uv add "<package><X"` (see Day 00). |
| Notebook: `No module named ...` but `uv run` works | select the `.venv` kernel **from this Day folder** |
| `No PDF files found in .../data` | Copy the PDFs into the inbox: `uv run python ../shared_data/copy_pdfs.py data`. |
| `connection refused` on port 6333 | Start Qdrant first (see Day 33): `docker compose up -d qdrant` in the Day 33 folder. |
</details>

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 0 | 🐍 **Python basics for today** — the Python used in this day, explained very simply (no API key needed) | open 00_python_basics.ipynb |
| 1 | Read README.md (complete step-by-step guide) | - |
| 1b | Copy the course PDFs into the `data/` inbox | `uv run python ../shared_data/copy_pdfs.py data` |
| 2 | Ask the RAG bot | `uv run python main.py query "What was JPMorgan's net income in 2023?"` |
| 3 | DeepEval intro | `uv run python resources/deepeval_intro.py` |
| 4 | Run evaluations | `uv run python main.py eval --help` |
| 5 | Interview prep | open resources/Production_RAG_Test_Question_Bank.html |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or `uv add jupyterlab` once and run `uv run jupyter lab`.

---
[<- Day_33_Production_RAG_Pipeline](../Day_33_Production_RAG_Pipeline/00_START_HERE.md) | [Day_35_Fine_Tuning_LLMs ->](../Day_35_Fine_Tuning_LLMs/00_START_HERE.md)
