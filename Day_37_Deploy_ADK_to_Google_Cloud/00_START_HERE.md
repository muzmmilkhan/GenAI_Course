# Day 37 - Deploy ADK Agents to Google Cloud

**What you will learn:** Deploy the Day 36 agents to Vertex AI Agent Engine and Cloud Run, then call them from an API server and a web UI.

## Before you start
- Do the one-time setup in the [course README](../README.md) (`uv sync` + `.env`).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_37_Deploy_ADK_to_Google_Cloud
  ```
- Needs a Google Cloud project + `gcloud` CLI. Keys: `GOOGLE_CLOUD_*`, `API_SECRET_KEY`.

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 1 | Read CLOUD_RUN_vs_AGENT_ENGINE.md | - |
| 2 | Follow deployment_materials/GCP_ADK_Deployment_Guide.md | - |
| 3 | Test Agent Engine deployment | `uv run python test_deployed_agent.py` |
| 4 | Test Cloud Run deployment | `uv run python test_deployed_agent_cloud_run.py` |
| 5 | Backend for Cloud Run | `cd backend_cloud_run && uv run uvicorn api_server_cloud_run:app --port 8000` |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or run `uv run jupyter lab` from the course root.

---
[<- Day_36_Google_ADK_Agents](../Day_36_Google_ADK_Agents/00_START_HERE.md) | [Day_38_Cloud_Deployment_Options_AWS ->](../Day_38_Cloud_Deployment_Options_AWS/00_START_HERE.md)
