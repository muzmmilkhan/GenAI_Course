# Day 18 - Planning & Deep-Research Agents

**What you will learn:** Agents that plan first, research in parallel and write long structured reports / blog posts (with images).

## Before you start
- Finished [Day 00](../Day_00_Setup_uv_and_Python/00_START_HERE.md) once (your uv project, `.env` and notebook kernel are ready).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_18_Planning_and_Deep_Research_Agents
  ```
- Keys: `OPENAI_API_KEY`, `GOOGLE_API_KEY`, `TAVILY_API_KEY`/`SERPAPI_API_KEY`. `sample_outputs/` shows a generated report.

## 📦 Step 1 - Install today's packages
✅ **Nothing new to install today** — everything you need was installed on earlier days.

Check what you have so far with `uv tree --depth 1`.

<details>
<summary>🧯 Something went wrong? Click here</summary>

| You see... | What to do |
|---|---|
| `ModuleNotFoundError: No module named ...` | a package from an earlier day is missing — check that day's 📦 step, or run `uv sync` |
| `No solution found when resolving dependencies` | two packages need versions that don't fit together. Read the error from the bottom, then try `uv add "<package>"` without a version, or limit it: `uv add "<package><X"` (see Day 00). |
| Notebook: `No module named ...` but `uv run` works | select the `.venv (Python 3.12)` kernel from the course folder |
</details>

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 0 | 🐍 **Python basics for today** — the Python used in this day, explained very simply (no API key needed) | open 00_python_basics.ipynb |
| 1 | Planning agent -> structured report | open 01_planning_agent_deep_research_report.ipynb |
| 2 | Blog research & writing agent | open 02_blog_research_writing_agent.ipynb |
| 3 | Same agent + image generation | open 03_blog_research_writing_agent_with_image.ipynb |
| 4 | Architecture | open blog_agent_architecture_visualization.html |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or `uv add jupyterlab` once and run `uv run jupyter lab`.

---
[<- Day_17_Project_WhatsApp_Agent](../Day_17_Project_WhatsApp_Agent/00_START_HERE.md) | [Day_19_LangChain_Agents_RAG_SQL_Middleware ->](../Day_19_LangChain_Agents_RAG_SQL_Middleware/00_START_HERE.md)
