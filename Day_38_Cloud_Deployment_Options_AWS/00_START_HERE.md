# Day 38 - Cloud Deployment Options (AWS & others)

**What you will learn:** Where to host GenAI apps: EC2, ECS, Lambda, App Runner, SageMaker, Bedrock - compared with other clouds.

## Before you start
- Finished [Day 00](../Day_00_Setup_uv_and_Python/00_START_HERE.md) once (your uv project, `.env` and notebook kernel are ready).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_38_Cloud_Deployment_Options_AWS
  ```
- No API keys needed.

## 📦 Step 1 - Install today's packages
Run this in the terminal (from this Day folder or the course root — uv finds your project automatically):
```bash
uv add matplotlib python-docx
```
| Package | What it is for |
|---|---|
| `matplotlib` | draw charts (used to make the diagrams in the Word guide) |
| `python-docx` | create Word documents from Python |

> 🔎 Afterwards open `pyproject.toml` (course root) and find the new lines. We always install the **latest** versions, so your version numbers may be newer than your classmates' — that's normal.

<details>
<summary>🧯 Something went wrong? Click here</summary>

| You see... | What to do |
|---|---|
| `ModuleNotFoundError: No module named 'matplotlib'` | the package is not installed — run today's `uv add` command above |
| `No solution found when resolving dependencies` | two packages need versions that don't fit together. Read the error from the bottom, then try `uv add "<package>"` without a version, or limit it: `uv add "<package><X"` (see Day 00). |
| Notebook: `No module named ...` but `uv run` works | select the `.venv (Python 3.12)` kernel from the course folder |
</details>

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 0 | 🐍 **Python basics for today** — the Python used in this day, explained very simply (no API key needed) | open 00_python_basics.ipynb |
| 1 | Open cloud_services_comparison.html | double-click |
| 2 | Read AWS_Deployment_Options_Guide.docx | Word / Pages / Google Docs |
| 3 | (Optional) regenerate the document | `uv run python generate_aws_doc.py` |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or `uv add jupyterlab` once and run `uv run jupyter lab`.

---
[<- Day_37_Deploy_ADK_to_Google_Cloud](../Day_37_Deploy_ADK_to_Google_Cloud/00_START_HERE.md) | [Course home](../README.md)
