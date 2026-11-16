# Day 34 - Evaluating RAG with DeepEval

**What you will learn:** Golden datasets, retriever / generator / pipeline metrics, LLM-as-judge, safety, cost & latency evaluation and regression gates.

## Before you start
- Do the one-time setup in the [course README](../README.md) (`uv sync` + `.env`).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_34_RAG_Evaluation_DeepEval
  ```
- Keys: `GOOGLE_API_KEY`, `GROQ_API_KEY`, `OPENAI_API_KEY` (judge). Needs Qdrant from Day 33 (`QDRANT_URL`).

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 1 | Read README.md (complete step-by-step guide) | - |
| 2 | Ask the RAG bot | `uv run python main.py query "What was JPMorgan's net income in 2023?"` |
| 3 | DeepEval intro | `uv run python resources/deepeval_intro.py` |
| 4 | Run evaluations | `uv run python main.py eval --help` |
| 5 | Interview prep | open resources/Production_RAG_Test_Question_Bank.html |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or run `uv run jupyter lab` from the course root.

---
[<- Day_33_Production_RAG_Pipeline](../Day_33_Production_RAG_Pipeline/00_START_HERE.md) | [Day_35_Fine_Tuning_LLMs ->](../Day_35_Fine_Tuning_LLMs/00_START_HERE.md)
