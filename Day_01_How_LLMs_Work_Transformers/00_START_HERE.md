# Day 01 - How LLMs Work - The Transformer

**What you will learn:** What happens inside a Large Language Model: tokens, embeddings, self-attention, encoder/decoder blocks, training and how the next word is sampled.

## Before you start
- Finished [Day 00](../Day_00_Setup_uv_and_Python/00_START_HERE.md) once (your uv project, `.env` and notebook kernel are ready).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_01_How_LLMs_Work_Transformers
  ```
- No code and no API keys today - just understand the ideas.

## 📦 Step 1 - Install today's packages
✅ **Nothing new to install today** — everything you need was installed on earlier days.

Check what you have so far with `uv tree --depth 1`.

<details>
<summary>🧯 Something went wrong? Click here</summary>

| You see... | What to do |
|---|---|
| `ModuleNotFoundError: No module named ...` | a package from an earlier day is missing — check that day's 📦 step, or run `uv sync` |
| `No solution found when resolving dependencies` | two packages need versions that don't fit together. Read the error from the bottom, then try `uv add "<package>"` without a version, or limit it: `uv add "<package><X"` (see Day 00). |
| Notebook: `No module named ...` but `uv run` works | select the `.venv (Python 3.12)` kernel from the course folder |
</details>

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 0 | 🐍 **Python basics for today** — the Python used in this day, explained very simply (no API key needed) | open 00_python_basics.ipynb |
| 1 | Open `visualizers/01_transformer_encoder_visualizer.html` in your browser | double-click the file |
| 2 | Continue with visualizers 02 -> 06 in order (FFNN, decoder, training, inference, sampling) | double-click each file |
| 3 | Read `articles/01_Unpacking_Self_Attention.md` | any Markdown viewer / VS Code preview |
| 4 | Read `articles/02_Visualizing_Attention_in_Python.md` | any Markdown viewer |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or `uv add jupyterlab` once and run `uv run jupyter lab`.

---
[<- Day_00_Setup_uv_and_Python](../Day_00_Setup_uv_and_Python/00_START_HERE.md) | [Day_02_BERT_GPT_T5_Model_Families ->](../Day_02_BERT_GPT_T5_Model_Families/00_START_HERE.md)
