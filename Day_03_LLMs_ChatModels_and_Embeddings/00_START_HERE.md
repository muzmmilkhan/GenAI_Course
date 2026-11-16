# Day 03 - Talking to LLMs, Chat Models & Embeddings

**What you will learn:** Call an LLM from Python, control creativity with temperature, use OpenAI / Google / Hugging Face chat models, create embeddings and measure document similarity.

## Before you start
- Do the one-time setup in the [course README](../README.md) (`uv sync` + `.env`).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_03_LLMs_ChatModels_and_Embeddings
  ```
- Keys: `OPENAI_API_KEY`, `GOOGLE_API_KEY`, `HUGGINGFACEHUB_API_TOKEN`.

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 1 | Your first LLM call | `uv run python 1_llm.py` |
| 2 | Temperature | `uv run python 2_temperature.py` |
| 3 | Google Gemini chat model | `uv run python 3_chatmodel_google.py` |
| 4 | Hugging Face API model | `uv run python 4_chatmodel_hf_api.py` |
| 5 | Run a model locally (downloads weights) | `uv run python 5_chatmodel_hf_local.py` |
| 6 | Local embeddings | `uv run python 6_embedding_hf_local.py` |
| 7 | Document similarity with embeddings | `uv run python 7_document_similarity.py` |
| 8 | Extra embedding test | `uv run python 8_test_embedding.py` |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or run `uv run jupyter lab` from the course root.

---
[<- Day_02_BERT_GPT_T5_Model_Families](../Day_02_BERT_GPT_T5_Model_Families/00_START_HERE.md) | [Day_04_Prompts_and_Chatbots ->](../Day_04_Prompts_and_Chatbots/00_START_HERE.md)
