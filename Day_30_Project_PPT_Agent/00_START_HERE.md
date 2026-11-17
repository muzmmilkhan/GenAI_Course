# Day 30 - Project - PowerPoint Generation Agent

**What you will learn:** An agent that plans a slide deck, generates images with Gemini, asks for your approval and builds a real .pptx file.

## Before you start
- Finished [Day 00](../Day_00_Setup_uv_and_Python/00_START_HERE.md) once (your uv project, `.env` and notebook kernel are ready).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_30_Project_PPT_Agent
  ```
- Keys: `GOOGLE_API_KEY`.

## 📦 Step 1 - Install today's packages
Run this in the terminal (from this Day folder or the course root — uv finds your project automatically):
```bash
uv add python-pptx
```
| Package | What it is for |
|---|---|
| `python-pptx` | create PowerPoint files from Python |

> 🔎 Afterwards open `pyproject.toml` (course root) and find the new lines. We always install the **latest** versions, so your version numbers may be newer than your classmates' — that's normal.

<details>
<summary>🧯 Something went wrong? Click here</summary>

| You see... | What to do |
|---|---|
| `ModuleNotFoundError: No module named 'pptx'` | the package is not installed — run today's `uv add` command above |
| `No solution found when resolving dependencies` | two packages need versions that don't fit together. Read the error from the bottom, then try `uv add "<package>"` without a version, or limit it: `uv add "<package><X"` (see Day 00). |
| Notebook: `No module named ...` but `uv run` works | select the `.venv (Python 3.12)` kernel from the course folder |
</details>

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 0 | 🐍 **Python basics for today** — the Python used in this day, explained very simply (no API key needed) | open 00_python_basics.ipynb |
| 1 | Architecture | open ppt_agent_visualization.html and pptx_code_explainer_visualization.html |
| 2 | Run the agent | open ppt_agent.ipynb |
| 3 | Look at the generated decks (*.pptx) | - |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or `uv add jupyterlab` once and run `uv run jupyter lab`.

---
[<- Day_29_Deep_Agents](../Day_29_Deep_Agents/00_START_HERE.md) | [Day_31_Project_Voice_Agent ->](../Day_31_Project_Voice_Agent/00_START_HERE.md)
