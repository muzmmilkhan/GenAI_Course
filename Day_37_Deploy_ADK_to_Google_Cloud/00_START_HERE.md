# Day 37 - Deploy ADK Agents to Google Cloud

**What you will learn:** Deploy the Day 36 agents to Vertex AI Agent Engine and Cloud Run, then call them from an API server and a web UI.

## Before you start
- Finished [Day 00](../Day_00_Setup_uv_and_Python/00_START_HERE.md) once (your uv project, `.env` and notebook kernel are ready).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_37_Deploy_ADK_to_Google_Cloud
  ```
- Needs a Google Cloud project + `gcloud` CLI. Keys: `GOOGLE_CLOUD_*`, `API_SECRET_KEY`.

## 📦 Step 1 - Install today's packages
### 🧪 Today you create a **separate environment**
It uses Google ADK too (same reason as Day 36). Real teams solve this by giving each app **its own environment** — so today's project lives *inside this Day folder* with its own `pyproject.toml`, `uv.lock` and `.venv`. `uv run` always uses the project of the folder you are in.

Run these commands **inside this Day folder**:
```bash
uv init --bare --python ">=3.12,<3.13"
uv python pin 3.12
uv add python-dotenv ipykernel google-adk "google-cloud-aiplatform[adk,agent-engines]" cloudpickle fastapi "uvicorn[standard]" httpx requests
```
| Package | What it is for |
|---|---|
| `google-adk` | the `adk deploy` command |
| `google-cloud-aiplatform[adk,agent-engines]` | talk to Vertex AI Agent Engine |
| `cloudpickle` | package your agent so it can be uploaded to Agent Engine |
| `fastapi / uvicorn / httpx` | the API server that sits in front of Cloud Run |

> 📓 For notebooks today choose the kernel **`.venv` from this Day folder** (not the course root one).
>
> 🔎 Afterwards open `pyproject.toml` (in this Day folder) and find the new lines. We always install the **latest** versions, so your version numbers may be newer than your classmates' — that's normal.

<details>
<summary>🧯 Something went wrong? Click here</summary>

| You see... | What to do |
|---|---|
| `ModuleNotFoundError: No module named 'google.adk'` | the package is not installed — run today's `uv add` command above |
| `ModuleNotFoundError` although you installed it on an earlier day | today uses its **own** environment - install it here too (it's already in today's command), and run everything from inside this Day folder |
| `No solution found when resolving dependencies` | two packages need versions that don't fit together. Read the error from the bottom, then try `uv add "<package>"` without a version, or limit it: `uv add "<package><X"` (see Day 00). |
| Notebook: `No module named ...` but `uv run` works | select the `.venv` kernel **from this Day folder** |
</details>

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 0 | 🐍 **Python basics for today** — the Python used in this day, explained very simply (no API key needed) | open 00_python_basics.ipynb |
| 1 | Read CLOUD_RUN_vs_AGENT_ENGINE.md | - |
| 2 | Follow deployment_materials/GCP_ADK_Deployment_Guide.md | - |
| 3 | Test Agent Engine deployment | `uv run python test_deployed_agent.py` |
| 4 | Test Cloud Run deployment | `uv run python test_deployed_agent_cloud_run.py` |
| 5 | Backend for Cloud Run | `cd backend_cloud_run; uv run uvicorn api_server_cloud_run:app --port 8000` |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or `uv add jupyterlab` once and run `uv run jupyter lab`.

---
[<- Day_36_Google_ADK_Agents](../Day_36_Google_ADK_Agents/00_START_HERE.md) | [Day_38_Cloud_Deployment_Options_AWS ->](../Day_38_Cloud_Deployment_Options_AWS/00_START_HERE.md)
