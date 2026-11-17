# Day 05 - Structured Output & Output Parsers

**What you will learn:** Make the LLM return clean data (dicts / JSON / Pydantic objects) instead of free text.

## Before you start
- Finished [Day 00](../Day_00_Setup_uv_and_Python/00_START_HERE.md) once (your uv project, `.env` and notebook kernel are ready).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_05_Structured_Output_and_Parsers
  ```
- Keys: `OPENAI_API_KEY`, `HUGGINGFACEHUB_API_TOKEN` (for the open-model examples).

## 📦 Step 1 - Install today's packages
Run this in the terminal (from this Day folder or the course root — uv finds your project automatically):
```bash
uv add "pydantic[email]"
```
| Package | What it is for |
|---|---|
| `pydantic[email]` | data validation; `[email]` is an *extra* that adds email checking |

> 🔎 Afterwards open `pyproject.toml` (course root) and find the new lines. We always install the **latest** versions, so your version numbers may be newer than your classmates' — that's normal.

<details>
<summary>🧯 Something went wrong? Click here</summary>

| You see... | What to do |
|---|---|
| `ModuleNotFoundError: No module named 'email_validator'` | the package is not installed — run today's `uv add` command above |
| `No solution found when resolving dependencies` | two packages need versions that don't fit together. Read the error from the bottom, then try `uv add "<package>"` without a version, or limit it: `uv add "<package><X"` (see Day 00). |
| Notebook: `No module named ...` but `uv run` works | select the `.venv (Python 3.12)` kernel from the course folder |
</details>

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 0 | 🐍 **Python basics for today** — the Python used in this day, explained very simply (no API key needed) | open 00_python_basics.ipynb |
| 1 | TypedDict basics | `cd part1_structured_output; uv run python 1_typeddict_demo.py` |
| 2 | with_structured_output + TypedDict | `uv run python 2_with_structured_output_typeddict.py` |
| 3 | Pydantic basics | `uv run python 3_pydantic_demo.py` |
| 4 | with_structured_output + Pydantic | `uv run python 4_with_structured_output_pydantic.py` |
| 5 | with_structured_output + JSON schema | `uv run python 5_with_structured_output_json.py` |
| 6 | Structured output with an open model | `uv run python 6_with_structured_output_llama.py` |
| 7 | StrOutputParser | `cd ../part2_output_parsers; uv run python 1_stroutputparser.py` |
| 8 | StrOutputParser in a chain | `uv run python 2_stroutputparser_chain.py` |
| 9 | JsonOutputParser | `uv run python 3_jsonoutputparser.py` |
| 10 | PydanticOutputParser | `uv run python 4_pydanticoutputparser.py` |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or `uv add jupyterlab` once and run `uv run jupyter lab`.

---
[<- Day_04_Prompts_and_Chatbots](../Day_04_Prompts_and_Chatbots/00_START_HERE.md) | [Day_06_LangChain_Chains ->](../Day_06_LangChain_Chains/00_START_HERE.md)
