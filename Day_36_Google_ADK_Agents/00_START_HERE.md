# Day 36 - Google Agent Development Kit (ADK)

**What you will learn:** Build agents with Google ADK: a simple tool bot, a Vertex AI RAG agent, a multi-agent podcast generator and a software-testing agent.

## Before you start
- Do the one-time setup in the [course README](../README.md) (`uv sync` + `.env`).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_36_Google_ADK_Agents
  ```
- Run from inside this folder. Keys: `GOOGLE_API_KEY` (rag_agent also needs a Google Cloud project).

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 1 | Read Materials/*.md | - |
| 2 | Open the ADK web UI and pick an agent | `uv run adk web` |
| 3 | Test the podcast agent | `uv run python test_podcast_agent.py` |
| 4 | Test the software-testing agent | `uv run python test_software_testing_agent.py` |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or run `uv run jupyter lab` from the course root.

---
[<- Day_35_Fine_Tuning_LLMs](../Day_35_Fine_Tuning_LLMs/00_START_HERE.md) | [Day_37_Deploy_ADK_to_Google_Cloud ->](../Day_37_Deploy_ADK_to_Google_Cloud/00_START_HERE.md)
