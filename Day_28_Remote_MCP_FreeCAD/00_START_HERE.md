# Day 28 - Remote MCP - Control FreeCAD with AI

**What you will learn:** RPC vs REST, XML-RPC basics, then a remote MCP server that drives the FreeCAD 3D-CAD app from Claude Desktop.

## Before you start
- Finished [Day 00](../Day_00_Setup_uv_and_Python/00_START_HERE.md) once (your uv project, `.env` and notebook kernel are ready).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_28_Remote_MCP_FreeCAD
  ```
- Needs FreeCAD installed. Optional: `uv sync --group freecad` for local Qt testing.

## 📦 Step 1 - Install today's packages
Run this in the terminal (from this Day folder or the course root — uv finds your project automatically):
```bash
uv add --group freecad pyside6
```
| Package | What it is for |
|---|---|
| `pyside6` | Qt for Python (optional, only for testing the FreeCAD bridge locally) |

> 🔎 Afterwards open `pyproject.toml` (course root) and find the new lines. We always install the **latest** versions, so your version numbers may be newer than your classmates' — that's normal.

<details>
<summary>🧯 Something went wrong? Click here</summary>

| You see... | What to do |
|---|---|
| `ModuleNotFoundError: No module named 'PySide6'` | the package is not installed — run today's `uv add` command above |
| `No solution found when resolving dependencies` | two packages need versions that don't fit together. Read the error from the bottom, then try `uv add "<package>"` without a version, or limit it: `uv add "<package><X"` (see Day 00). |
| Notebook: `No module named ...` but `uv run` works | select the `.venv (Python 3.12)` kernel from the course folder |
| `ModuleNotFoundError: No module named 'FreeCAD'` | Normal outside FreeCAD — those files run *inside* the FreeCAD app (see README.md). |
</details>

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 0 | 🐍 **Python basics for today** — the Python used in this day, explained very simply (no API key needed) | open 00_python_basics.ipynb |
| 1 | RPC basics | `uv run python xmlrpc_demo/demo_server.py   (then in a 2nd terminal) uv run python xmlrpc_demo/demo_client.py` |
| 2 | Read Resources/*.md and open Resources/dataflow_visualization.html | - |
| 3 | Follow README.md to connect FreeCAD | - |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or `uv add jupyterlab` once and run `uv run jupyter lab`.

---
[<- Day_27_MCP_with_LangChain_Agents](../Day_27_MCP_with_LangChain_Agents/00_START_HERE.md) | [Day_29_Deep_Agents ->](../Day_29_Deep_Agents/00_START_HERE.md)
