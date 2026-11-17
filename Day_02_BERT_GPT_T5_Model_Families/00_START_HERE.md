# Day 02 - BERT vs GPT vs T5 - Model Families

**What you will learn:** The three transformer families: encoder-only (BERT), decoder-only (GPT) and encoder-decoder (T5), and when to use each.

## Before you start
- Finished [Day 00](../Day_00_Setup_uv_and_Python/00_START_HERE.md) once (your uv project, `.env` and notebook kernel are ready).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_02_BERT_GPT_T5_Model_Families
  ```
- No code and no API keys today.

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
| 1 | Open `01_bert_visualizer.html` | double-click |
| 2 | Open `02_gpt_visualizer.html` | double-click |
| 3 | Open `03_t5_visualizer.html` | double-click |
| 4 | Compare them in `04_bert_gpt_t5_comparison.html` | double-click |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or `uv add jupyterlab` once and run `uv run jupyter lab`.

---
[<- Day_01_How_LLMs_Work_Transformers](../Day_01_How_LLMs_Work_Transformers/00_START_HERE.md) | [Day_03_LLMs_ChatModels_and_Embeddings ->](../Day_03_LLMs_ChatModels_and_Embeddings/00_START_HERE.md)
