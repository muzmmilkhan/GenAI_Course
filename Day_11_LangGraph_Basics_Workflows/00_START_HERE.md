# Day 11 - LangGraph Basics - Workflows as Graphs

**What you will learn:** State, nodes, edges and conditional edges. Build simple LLM workflows, a sentiment-based review-reply flow, a RAG graph and an iterative post generator.

## Before you start
- Finished [Day 00](../Day_00_Setup_uv_and_Python/00_START_HERE.md) once (your uv project, `.env` and notebook kernel are ready).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_11_LangGraph_Basics_Workflows
  ```
- Keys: `OPENAI_API_KEY`, `GOOGLE_API_KEY`.

## 📦 Step 1 - Install today's packages
Run this in the terminal (from this Day folder or the course root — uv finds your project automatically):
```bash
uv add langgraph prompt-inspector-ux
```
| Package | What it is for |
|---|---|
| `langgraph` | build agents and workflows as graphs |
| `prompt-inspector-ux` | inspect the prompts sent to the LLM |

> 🔎 Afterwards open `pyproject.toml` (course root) and find the new lines. We always install the **latest** versions, so your version numbers may be newer than your classmates' — that's normal.

<details>
<summary>🧯 Something went wrong? Click here</summary>

| You see... | What to do |
|---|---|
| `ModuleNotFoundError: No module named 'langgraph'` | the package is not installed — run today's `uv add` command above |
| `No solution found when resolving dependencies` | two packages need versions that don't fit together. Read the error from the bottom, then try `uv add "<package>"` without a version, or limit it: `uv add "<package><X"` (see Day 00). |
| Notebook: `No module named ...` but `uv run` works | select the `.venv (Python 3.12)` kernel from the course folder |
</details>

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 0 | 🐍 **Python basics for today** — the Python used in this day, explained very simply (no API key needed) | open 00_python_basics.ipynb |
| 1 | Read LANGGRAPH_EXPLAINED_FOR_STUDENTS.md | - |
| 2 | Simple LLM workflow | open 01_simple_llm_workflow.ipynb |
| 3 | Sentiment -> reply workflow | open 02_sentiment_review_reply_workflow.ipynb |
| 4 | Simple RAG agent | open 03_simple_rag_agent.ipynb |
| 5 | X (Twitter) post generator with evaluator loop | open 04_X_post_generator_workflow.ipynb |
| 6 | Mini project: review reply web app | `cd Amazon_Review_Reply_App; uv run streamlit run app.py` |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or `uv add jupyterlab` once and run `uv run jupyter lab`.

---
[<- Day_10_Agents_From_Scratch_ReAct](../Day_10_Agents_From_Scratch_ReAct/00_START_HERE.md) | [Day_12_LangGraph_Memory_and_Persistence ->](../Day_12_LangGraph_Memory_and_Persistence/00_START_HERE.md)
