# Day 35 - Fine-Tuning an LLM (Gemma + QLoRA)

**What you will learn:** Build a dataset, fine-tune Gemma 2B with LoRA/QLoRA, and serve it (FastAPI / vLLM).

## Before you start
- Finished [Day 00](../Day_00_Setup_uv_and_Python/00_START_HERE.md) once (your uv project, `.env` and notebook kernel are ready).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_35_Fine_Tuning_LLMs
  ```
- Needs an NVIDIA GPU (free Colab T4 works) and a Hugging Face token with Gemma access.

## 📦 Step 1 - Install today's packages
Run this in the terminal (from this Day folder or the course root — uv finds your project automatically):
```bash
uv add --group finetune peft trl accelerate datasets "bitsandbytes; sys_platform == 'linux'"
```
| Package | What it is for |
|---|---|
| `peft` | LoRA / QLoRA — train a small adapter instead of the whole model |
| `trl` | Hugging Face trainer for chat models (SFTTrainer) |
| `accelerate` | run training on GPUs efficiently |
| `datasets` | load and process training datasets |
| `bitsandbytes` | 4-bit model loading (Linux + NVIDIA GPU only — that's what `; sys_platform == 'linux'` means) |

> 🔎 Afterwards open `pyproject.toml` (course root) and find the new lines. We always install the **latest** versions, so your version numbers may be newer than your classmates' — that's normal.

<details>
<summary>🧯 Something went wrong? Click here</summary>

| You see... | What to do |
|---|---|
| `ModuleNotFoundError: No module named 'peft'` | the package is not installed — run today's `uv add` command above |
| `No solution found when resolving dependencies` | two packages need versions that don't fit together. Read the error from the bottom, then try `uv add "<package>"` without a version, or limit it: `uv add "<package><X"` (see Day 00). |
| Notebook: `No module named ...` but `uv run` works | select the `.venv (Python 3.12)` kernel from the course folder |
| `bitsandbytes` / CUDA errors on a Mac | Fine-tuning needs an NVIDIA GPU. Open the notebook in Google Colab (free T4 GPU) and run the `!pip install` cell there. |
</details>

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 0 | 🐍 **Python basics for today** — the Python used in this day, explained very simply (no API key needed) | open 00_python_basics.ipynb |
| 1 | Visual explanation | open gemma_finetune_hindi_visualization.html |
| 2 | Build the dataset | `uv run python generate_dataset.py` |
| 3 | Fine-tune (GPU needed) | open gemma_hindi_finetune.ipynb in Google Colab, or: uv sync --group finetune; uv run python train.py |
| 4 | Serve with vLLM | open vllm_gemma_serve.ipynb in Colab |
| 5 | Serve with FastAPI | `uv run python app.py` |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or `uv add jupyterlab` once and run `uv run jupyter lab`.

---
[<- Day_34_RAG_Evaluation_DeepEval](../Day_34_RAG_Evaluation_DeepEval/00_START_HERE.md) | [Day_36_Google_ADK_Agents ->](../Day_36_Google_ADK_Agents/00_START_HERE.md)
