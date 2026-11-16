# Day 28 - Remote MCP - Control FreeCAD with AI

**What you will learn:** RPC vs REST, XML-RPC basics, then a remote MCP server that drives the FreeCAD 3D-CAD app from Claude Desktop.

## Before you start
- Do the one-time setup in the [course README](../README.md) (`uv sync` + `.env`).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_28_Remote_MCP_FreeCAD
  ```
- Needs FreeCAD installed. Optional: `uv sync --group freecad` for local Qt testing.

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 1 | RPC basics | `uv run python xmlrpc_demo/demo_server.py   (then in a 2nd terminal) uv run python xmlrpc_demo/demo_client.py` |
| 2 | Read Resources/*.md and open Resources/dataflow_visualization.html | - |
| 3 | Follow README.md to connect FreeCAD | - |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or run `uv run jupyter lab` from the course root.

---
[<- Day_27_MCP_with_LangChain_Agents](../Day_27_MCP_with_LangChain_Agents/00_START_HERE.md) | [Day_29_Deep_Agents ->](../Day_29_Deep_Agents/00_START_HERE.md)
