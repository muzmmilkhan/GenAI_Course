# Day 14 - Map-Reduce & Your First Multi-Agent System

**What you will learn:** Process many documents in parallel with Send() (map-reduce over financial PDFs) and build a research agent + chart agent team.

## Before you start
- Do the one-time setup in the [course README](../README.md) (`uv sync` + `.env`).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_14_LangGraph_MapReduce_and_MultiAgent
  ```
- Keys: `OPENAI_API_KEY`, `GOOGLE_API_KEY`. `chart.html` and `xray_graph.png` are sample outputs of notebook 02.

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 1 | Map-reduce over PDFs in shared_data/financial_pdfs | open 01_map_reduce.ipynb |
| 2 | Multi-agent: researcher + Plotly chart generator | open 02_multiagent_research_and_chart.ipynb |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or run `uv run jupyter lab` from the course root.

---
[<- Day_13_LangGraph_Tools_and_Human_in_the_Loop](../Day_13_LangGraph_Tools_and_Human_in_the_Loop/00_START_HERE.md) | [Day_15_Advanced_RAG_with_LangGraph ->](../Day_15_Advanced_RAG_with_LangGraph/00_START_HERE.md)
