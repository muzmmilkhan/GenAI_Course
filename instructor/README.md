# 👩‍🏫 Instructor reference environments

Students build their environment themselves (Day 00 + the **📦 Install today's packages** step of every day).
These folders contain the **tested result** of following the course from Day 00 to Day 38, so you can help a student whose setup is broken.

| Folder | Used for | Same as what a student gets after... |
|---|---|---|
| `main/` | Days 00-33, 35, 38 (course root project) | doing every 📦 step in the course root |
| `day34_rag_evaluation/` | Day 34 (its own environment) | Day 34's 📦 step inside `Day_34_RAG_Evaluation_DeepEval/` |
| `day36_google_adk/` | Day 36 (its own environment) | Day 36's 📦 step inside `Day_36_Google_ADK_Agents/` |
| `day37_adk_deploy/` | Day 37 (its own environment) | Day 37's 📦 step inside `Day_37_Deploy_ADK_to_Google_Cloud/` |
| `all_in_one/` | everything in **one** environment (older but compatible versions) | - (handy for you to run any day quickly) |

### Why are Days 34, 36 and 37 separate?
With the **latest** versions, some packages cannot live in the same environment:
- newest **Google ADK** needs `google-genai<3`, newest `langchain-google-genai` needs `google-genai>=3.2`
- newest **DeepEval** needs `click<8.4`, newest `huggingface-hub` needs `click>=8.4.2`

### Fix a broken student environment
```bash
# compare first (great learning moment):
diff pyproject.toml instructor/main/pyproject.toml
# last resort - replace and rebuild (course root):
cp instructor/main/pyproject.toml instructor/main/uv.lock instructor/main/.python-version .
uv sync --all-groups
```
For a separate-environment day, copy that folder's 3 files into the Day folder and run `uv sync` there.

### Tested
- Every day's `uv add` run in order on a fresh project, then **every import statement** of that day's lessons and notebooks executed: all 39 days pass.
- Every locked package checked for **Windows** (Python 3.12, x86-64): all have Windows wheels, except `google-search-results` and `langdetect`, which are pure Python and install everywhere.
- Versions are the latest at the time of testing. `mcp` is limited to `<2` on purpose (see Day 25).
