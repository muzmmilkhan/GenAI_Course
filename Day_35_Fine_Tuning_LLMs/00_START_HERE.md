# Day 35 - Fine-Tuning an LLM (Gemma + QLoRA)

**What you will learn:** Build a dataset, fine-tune Gemma 2B with LoRA/QLoRA, and serve it (FastAPI / vLLM).

## Before you start
- Do the one-time setup in the [course README](../README.md) (`uv sync` + `.env`).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_35_Fine_Tuning_LLMs
  ```
- Needs an NVIDIA GPU (free Colab T4 works) and a Hugging Face token with Gemma access.

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 1 | Visual explanation | open gemma_finetune_hindi_visualization.html |
| 2 | Build the dataset | `uv run python generate_dataset.py` |
| 3 | Fine-tune (GPU needed) | open gemma_hindi_finetune.ipynb in Google Colab, or: uv sync --group finetune && uv run python train.py |
| 4 | Serve with vLLM | open vllm_gemma_serve.ipynb in Colab |
| 5 | Serve with FastAPI | `uv run python app.py` |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or run `uv run jupyter lab` from the course root.

---
[<- Day_34_RAG_Evaluation_DeepEval](../Day_34_RAG_Evaluation_DeepEval/00_START_HERE.md) | [Day_36_Google_ADK_Agents ->](../Day_36_Google_ADK_Agents/00_START_HERE.md)
