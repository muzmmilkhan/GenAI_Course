# Day 36 - Google Agent Development Kit (ADK)

**What you will learn:** Build agents with Google ADK: a simple tool bot, a Vertex AI RAG agent, a multi-agent podcast generator and a software-testing agent.

## Before you start
- Finished [Day 00](../Day_00_Setup_uv_and_Python/00_START_HERE.md) once (your uv project, `.env` and notebook kernel are ready).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_36_Google_ADK_Agents
  ```
- Run from inside this folder. Keys: `GOOGLE_API_KEY` (rag_agent also needs a Google Cloud project).

## 📦 Step 1 - Install today's packages
### 🧪 Today you create a **separate environment**
The newest **Google ADK** needs `google-genai<3`, but the newest `langchain-google-genai` (used since Day 03) needs `google-genai>=3.2`. Both can't be true in one environment. Real teams solve this by giving each app **its own environment** — so today's project lives *inside this Day folder* with its own `pyproject.toml`, `uv.lock` and `.venv`. `uv run` always uses the project of the folder you are in.

Run these commands **inside this Day folder**:
```bash
uv init --bare --python ">=3.12,<3.13"
uv python pin 3.12
uv add python-dotenv ipykernel google-adk "google-cloud-aiplatform[adk,agent-engines]" beautifulsoup4 python-docx edge-tts pypdf requests
uv add --dev pytest
```
| Package | What it is for |
|---|---|
| `google-adk` | Google's Agent Development Kit |
| `google-cloud-aiplatform[adk,agent-engines]` | Vertex AI (RAG Engine, Agent Engine) |
| `beautifulsoup4` | read web pages (HTML) |
| `python-docx` | read and write Word documents |
| `edge-tts` | free text-to-speech for the podcast agent |
| `pytest` | run the agent tests |

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
| `google.auth.exceptions.DefaultCredentialsError` | The RAG agent needs Google Cloud: run `gcloud auth application-default login`. |
</details>

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 0 | 🐍 **Python basics for today** — the Python used in this day, explained very simply (no API key needed) | open 00_python_basics.ipynb |
| 1 | Read Materials/*.md | - |
| 2 | Open the ADK web UI and pick an agent | `uv run adk web` |
| 3 | Test the podcast agent | `uv run python test_podcast_agent.py` |
| 4 | Test the software-testing agent | `uv run python test_software_testing_agent.py` |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or `uv add jupyterlab` once and run `uv run jupyter lab`.

---
[<- Day_35_Fine_Tuning_LLMs](../Day_35_Fine_Tuning_LLMs/00_START_HERE.md) | [Day_37_Deploy_ADK_to_Google_Cloud ->](../Day_37_Deploy_ADK_to_Google_Cloud/00_START_HERE.md)
