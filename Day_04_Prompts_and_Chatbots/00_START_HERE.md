# Day 04 - Prompts, Messages & Your First Chatbot

**What you will learn:** Prompt templates, chat prompt templates, message types, message placeholders (chat history) and a simple chatbot with a Streamlit UI.

## Before you start
- Finished [Day 00](../Day_00_Setup_uv_and_Python/00_START_HERE.md) once (your uv project, `.env` and notebook kernel are ready).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_04_Prompts_and_Chatbots
  ```
- Keys: `OPENAI_API_KEY`.

## 📦 Step 1 - Install today's packages
Run this in the terminal (from this Day folder or the course root — uv finds your project automatically):
```bash
uv add streamlit
```
| Package | What it is for |
|---|---|
| `streamlit` | build a web UI in pure Python |

> 🔎 Afterwards open `pyproject.toml` (course root) and find the new lines. We always install the **latest** versions, so your version numbers may be newer than your classmates' — that's normal.

<details>
<summary>🧯 Something went wrong? Click here</summary>

| You see... | What to do |
|---|---|
| `ModuleNotFoundError: No module named 'streamlit'` | the package is not installed — run today's `uv add` command above |
| `No solution found when resolving dependencies` | two packages need versions that don't fit together. Read the error from the bottom, then try `uv add "<package>"` without a version, or limit it: `uv add "<package><X"` (see Day 00). |
| Notebook: `No module named ...` but `uv run` works | select the `.venv (Python 3.12)` kernel from the course folder |
</details>

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 0 | 🐍 **Python basics for today** — the Python used in this day, explained very simply (no API key needed) | open 00_python_basics.ipynb |
| 1 | Chat prompt template | `uv run python 1_chat_prompt_template.py` |
| 2 | Message placeholder + chat history | `uv run python 2_message_placeholder.py` |
| 3 | System / Human / AI messages | `uv run python 3_messages.py` |
| 4 | Prompt template | `uv run python 4_prompt_template.py` |
| 5 | Save a reusable template to template.json | `uv run python 5_prompt_generator.py` |
| 6 | Prompt UI (opens in browser) | `uv run streamlit run 6_prompt_ui.py` |
| 7 | Terminal chatbot with memory | `uv run python 7_chatbot.py` |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or `uv add jupyterlab` once and run `uv run jupyter lab`.

---
[<- Day_03_LLMs_ChatModels_and_Embeddings](../Day_03_LLMs_ChatModels_and_Embeddings/00_START_HERE.md) | [Day_05_Structured_Output_and_Parsers ->](../Day_05_Structured_Output_and_Parsers/00_START_HERE.md)
