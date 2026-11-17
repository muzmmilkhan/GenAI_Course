# Day 03 - Talking to LLMs, Chat Models & Embeddings

**What you will learn:** Call an LLM from Python, control creativity with temperature, use OpenAI / Google / Hugging Face chat models, create embeddings and measure document similarity.

## Before you start
- Finished [Day 00](../Day_00_Setup_uv_and_Python/00_START_HERE.md) once (your uv project, `.env` and notebook kernel are ready).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_03_LLMs_ChatModels_and_Embeddings
  ```
- Keys: `OPENAI_API_KEY`, `GOOGLE_API_KEY`, `HUGGINGFACEHUB_API_TOKEN`.

## 📦 Step 1 - Install today's packages
Run this in the terminal (from this Day folder or the course root — uv finds your project automatically):
```bash
uv add langchain langchain-openai langchain-google-genai langchain-huggingface sentence-transformers scikit-learn pillow
```
| Package | What it is for |
|---|---|
| `langchain` | the main LangChain framework |
| `langchain-openai` | talk to OpenAI models (GPT) |
| `langchain-google-genai` | talk to Google Gemini models |
| `langchain-huggingface` | use Hugging Face models (online API and local) |
| `sentence-transformers` | run embedding models on your own computer (also installs PyTorch — big download!) |
| `scikit-learn` | machine-learning helpers; we use its cosine similarity |
| `pillow` | open and work with images |

> 🔎 Afterwards open `pyproject.toml` (course root) and find the new lines. We always install the **latest** versions, so your version numbers may be newer than your classmates' — that's normal.

<details>
<summary>🧯 Something went wrong? Click here</summary>

| You see... | What to do |
|---|---|
| `ModuleNotFoundError: No module named 'langchain'` | the package is not installed — run today's `uv add` command above |
| `No solution found when resolving dependencies` | two packages need versions that don't fit together. Read the error from the bottom, then try `uv add "<package>"` without a version, or limit it: `uv add "<package><X"` (see Day 00). |
| Notebook: `No module named ...` but `uv run` works | select the `.venv (Python 3.12)` kernel from the course folder |
| Download is very slow / takes minutes | Normal! `sentence-transformers` installs PyTorch (~1 GB). Let it finish once — it is cached afterwards. |
</details>

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 0 | 🐍 **Python basics for today** — the Python used in this day, explained very simply (no API key needed) | open 00_python_basics.ipynb |
| 1 | Your first LLM call | `uv run python 1_llm.py` |
| 2 | Temperature | `uv run python 2_temperature.py` |
| 3 | Google Gemini chat model | `uv run python 3_chatmodel_google.py` |
| 4 | Hugging Face API model | `uv run python 4_chatmodel_hf_api.py` |
| 5 | Run a model locally (downloads weights) | `uv run python 5_chatmodel_hf_local.py` |
| 6 | Local embeddings | `uv run python 6_embedding_hf_local.py` |
| 7 | Document similarity with embeddings | `uv run python 7_document_similarity.py` |
| 8 | Extra embedding test | `uv run python 8_test_embedding.py` |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or `uv add jupyterlab` once and run `uv run jupyter lab`.

---
[<- Day_02_BERT_GPT_T5_Model_Families](../Day_02_BERT_GPT_T5_Model_Families/00_START_HERE.md) | [Day_04_Prompts_and_Chatbots ->](../Day_04_Prompts_and_Chatbots/00_START_HERE.md)
