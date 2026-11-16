# Day 05 - Structured Output & Output Parsers

**What you will learn:** Make the LLM return clean data (dicts / JSON / Pydantic objects) instead of free text.

## Before you start
- Do the one-time setup in the [course README](../README.md) (`uv sync` + `.env`).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_05_Structured_Output_and_Parsers
  ```
- Keys: `OPENAI_API_KEY`, `HUGGINGFACEHUB_API_TOKEN` (for the open-model examples).

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 1 | TypedDict basics | `cd part1_structured_output && uv run python 1_typeddict_demo.py` |
| 2 | with_structured_output + TypedDict | `uv run python 2_with_structured_output_typeddict.py` |
| 3 | Pydantic basics | `uv run python 3_pydantic_demo.py` |
| 4 | with_structured_output + Pydantic | `uv run python 4_with_structured_output_pydantic.py` |
| 5 | with_structured_output + JSON schema | `uv run python 5_with_structured_output_json.py` |
| 6 | Structured output with an open model | `uv run python 6_with_structured_output_llama.py` |
| 7 | StrOutputParser | `cd ../part2_output_parsers && uv run python 1_stroutputparser.py` |
| 8 | StrOutputParser in a chain | `uv run python 2_stroutputparser_chain.py` |
| 9 | JsonOutputParser | `uv run python 3_jsonoutputparser.py` |
| 10 | PydanticOutputParser | `uv run python 4_pydanticoutputparser.py` |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or run `uv run jupyter lab` from the course root.

---
[<- Day_04_Prompts_and_Chatbots](../Day_04_Prompts_and_Chatbots/00_START_HERE.md) | [Day_06_LangChain_Chains ->](../Day_06_LangChain_Chains/00_START_HERE.md)
