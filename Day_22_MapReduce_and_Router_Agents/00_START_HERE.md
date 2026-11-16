# Day 22 - Multi-Agent Pattern 3 - Map-Reduce & Router

**What you will learn:** Fan-out work to parallel agents and merge the results (Send API), and route questions to the right knowledge source.

## Before you start
- Do the one-time setup in the [course README](../README.md) (`uv sync` + `.env`).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_22_MapReduce_and_Router_Agents
  ```
- Keys: `GOOGLE_API_KEY`, `OPENAI_API_KEY`. `reports/` holds benchmark reports produced by these notebooks.

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 1 | Map-reduce with parallel agents | open 01_map_reduce_parallel_agents.ipynb |
| 2 | Map-reduce with Send() | open 02_map_reduce_send_api.ipynb |
| 3 | Router knowledge base | open 03_router_knowledge_base.ipynb |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or run `uv run jupyter lab` from the course root.

---
[<- Day_21_Multi_Agent_Handoffs_and_Swarm](../Day_21_Multi_Agent_Handoffs_and_Swarm/00_START_HERE.md) | [Day_23_Project_Trip_Planner_Multi_Agent ->](../Day_23_Project_Trip_Planner_Multi_Agent/00_START_HERE.md)
