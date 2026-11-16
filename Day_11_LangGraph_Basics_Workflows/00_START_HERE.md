# Day 11 - LangGraph Basics - Workflows as Graphs

**What you will learn:** State, nodes, edges and conditional edges. Build simple LLM workflows, a sentiment-based review-reply flow, a RAG graph and an iterative post generator.

## Before you start
- Do the one-time setup in the [course README](../README.md) (`uv sync` + `.env`).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_11_LangGraph_Basics_Workflows
  ```
- Keys: `OPENAI_API_KEY`, `GOOGLE_API_KEY`.

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 1 | Read LANGGRAPH_EXPLAINED_FOR_STUDENTS.md | - |
| 2 | Simple LLM workflow | open 01_simple_llm_workflow.ipynb |
| 3 | Sentiment -> reply workflow | open 02_sentiment_review_reply_workflow.ipynb |
| 4 | Simple RAG agent | open 03_simple_rag_agent.ipynb |
| 5 | X (Twitter) post generator with evaluator loop | open 04_X_post_generator_workflow.ipynb |
| 6 | Mini project: review reply web app | `cd Amazon_Review_Reply_App && uv run streamlit run app.py` |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or run `uv run jupyter lab` from the course root.

---
[<- Day_10_Agents_From_Scratch_ReAct](../Day_10_Agents_From_Scratch_ReAct/00_START_HERE.md) | [Day_12_LangGraph_Memory_and_Persistence ->](../Day_12_LangGraph_Memory_and_Persistence/00_START_HERE.md)
