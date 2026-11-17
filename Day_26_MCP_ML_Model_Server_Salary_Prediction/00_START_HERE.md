# Day 26 - MCP - Serve a Machine-Learning Model

**What you will learn:** Wrap a scikit-learn salary model (with SHAP explanations) as MCP tools and call them from a LangChain agent.

## Before you start
- Finished [Day 00](../Day_00_Setup_uv_and_Python/00_START_HERE.md) once (your uv project, `.env` and notebook kernel are ready).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_26_MCP_ML_Model_Server_Salary_Prediction
  ```
- Keys: `GOOGLE_API_KEY` for the agent notebook.

## 📦 Step 1 - Install today's packages
Run this in the terminal (from this Day folder or the course root — uv finds your project automatically):
```bash
uv add pandas shap langchain-mcp-adapters
```
| Package | What it is for |
|---|---|
| `pandas` | tables of data (DataFrames) |
| `shap` | explain why the model made a prediction |
| `langchain-mcp-adapters` | turn MCP tools into LangChain tools |

> 🔎 Afterwards open `pyproject.toml` (course root) and find the new lines. We always install the **latest** versions, so your version numbers may be newer than your classmates' — that's normal.

<details>
<summary>🧯 Something went wrong? Click here</summary>

| You see... | What to do |
|---|---|
| `ModuleNotFoundError: No module named 'pandas'` | the package is not installed — run today's `uv add` command above |
| `No solution found when resolving dependencies` | two packages need versions that don't fit together. Read the error from the bottom, then try `uv add "<package>"` without a version, or limit it: `uv add "<package><X"` (see Day 00). |
| Notebook: `No module named ...` but `uv run` works | select the `.venv (Python 3.12)` kernel from the course folder |
</details>

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 0 | 🐍 **Python basics for today** — the Python used in this day, explained very simply (no API key needed) | open 00_python_basics.ipynb |
| 1 | Train the model (creates salary_model.pkl) | `uv run python train_model.py` |
| 2 | Explain predictions | `uv run python explain_model.py` |
| 3 | Run the MCP server | `uv run fastmcp dev salary_mcp_server.py` |
| 4 | Use it from an agent | open salary_prediction_mcp_agent.ipynb |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or `uv add jupyterlab` once and run `uv run jupyter lab`.

---
[<- Day_25_MCP_Fundamentals_and_Servers](../Day_25_MCP_Fundamentals_and_Servers/00_START_HERE.md) | [Day_27_MCP_with_LangChain_Agents ->](../Day_27_MCP_with_LangChain_Agents/00_START_HERE.md)
