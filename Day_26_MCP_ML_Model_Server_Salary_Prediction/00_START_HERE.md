# Day 26 - MCP - Serve a Machine-Learning Model

**What you will learn:** Wrap a scikit-learn salary model (with SHAP explanations) as MCP tools and call them from a LangChain agent.

## Before you start
- Do the one-time setup in the [course README](../README.md) (`uv sync` + `.env`).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_26_MCP_ML_Model_Server_Salary_Prediction
  ```
- Keys: `GOOGLE_API_KEY` for the agent notebook.

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 1 | Train the model (creates salary_model.pkl) | `uv run python train_model.py` |
| 2 | Explain predictions | `uv run python explain_model.py` |
| 3 | Run the MCP server | `uv run fastmcp dev salary_mcp_server.py` |
| 4 | Use it from an agent | open salary_prediction_mcp_agent.ipynb |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or run `uv run jupyter lab` from the course root.

---
[<- Day_25_MCP_Fundamentals_and_Servers](../Day_25_MCP_Fundamentals_and_Servers/00_START_HERE.md) | [Day_27_MCP_with_LangChain_Agents ->](../Day_27_MCP_with_LangChain_Agents/00_START_HERE.md)
