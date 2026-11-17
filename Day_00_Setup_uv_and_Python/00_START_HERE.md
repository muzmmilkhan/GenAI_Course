# Day 00 - Setup: Python, uv and Your Project

**What you will learn:** what `uv` is, how to create a Python project, how to install packages with `uv add`, and what the files `pyproject.toml`, `uv.lock`, `.python-version` and `.venv` are for.

> 💡 **How this course works:** we do **not** install everything at once. Every day starts with an
> **"📦 Install today's packages"** step, so you learn what each library is for — and how to fix it when an install goes wrong.

---

## Step 1 - Install uv
`uv` is a very fast tool that installs Python, creates virtual environments and manages packages (it replaces `pip`, `venv` and `pyenv`).

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
Close and reopen the terminal, then check:
```bash
uv --version
```

### 🪟 Windows users - 3 extra things (do them once)
1. **Use PowerShell** (the default terminal in VS Code and Windows Terminal). All commands in this course work there.
2. **Turn on Python's UTF-8 mode**, otherwise files with emojis or Hindi text fail with `UnicodeDecodeError`:
   ```powershell
   setx PYTHONUTF8 1
   ```
   Then **close and reopen** the terminal **and VS Code**.
3. **Paths:** Windows writes `Day_07\docs`, macOS/Linux write `Day_07/docs`. Python accepts `/` on every system, so all the code in this course uses `/`.

| Tool (needed on) | macOS | Windows | Linux |
|---|---|---|---|
| Docker Desktop (Days 16, 25, 32, 33) | [docker.com](https://www.docker.com/products/docker-desktop/) | [docker.com](https://www.docker.com/products/docker-desktop/) | `sudo apt install docker.io docker-compose-v2` |
| Poppler + Tesseract (Days 08, 33) | `brew install poppler tesseract libmagic` | `winget install oschwartz10612.Poppler` and `winget install UB-Mannheim.TesseractOCR`, then restart the terminal | `sudo apt install poppler-utils tesseract-ocr libmagic1` |
| Node.js (Day 27) | `brew install node` | `winget install OpenJS.NodeJS.LTS` | `sudo apt install nodejs npm` |
| Git (optional) | `xcode-select --install` | `winget install Git.Git` | `sudo apt install git` |

## Step 2 - Open the course folder
All `uv` commands in this course are run from the **course root folder** (the folder that contains `README.md` and all the `Day_XX` folders):
```bash
cd path/to/GenAI_Course
```

## Step 3 - Create your project
```bash
uv init --bare --python ">=3.12,<3.13"
uv python pin 3.12
```
| Command | What it does |
|---|---|
| `uv init --bare` | creates **`pyproject.toml`** - the file that lists your project's packages (it is empty for now) |
| `--python ">=3.12,<3.13"` | says the project runs on **Python 3.12** (3.12 or newer, but older than 3.13). Keep the quotes! |
| `uv python pin 3.12` | creates **`.python-version`** so uv always uses Python 3.12 (it downloads it if you don't have it) |

Open `pyproject.toml` in your editor and find the line `requires-python = ">=3.12, <3.13"`.

> ❓ **Why not just `--python 3.12`?** That writes `requires-python = ">=3.12"`, which means *"3.12 **and every future Python**"*.
> uv then only picks package versions that promise to work on all of them. Some new releases (for example Google ADK and deepeval)
> list a maximum Python version, so uv would quietly install **very old** versions instead (we saw Google ADK 1.1 instead of 2.x!).
> Telling uv the exact range lets it choose the real latest versions.
>
> ❓ **Why 3.12 and not the newest Python?** Big AI libraries (PyTorch, unstructured, ...) usually need some months to support a new Python version. 3.12 works with everything in this course.

## Step 4 - Install your first packages
```bash
uv add python-dotenv ipykernel
```
| Package | Why we need it |
|---|---|
| `python-dotenv` | reads your API keys from the `.env` file |
| `ipykernel` | lets VS Code / Jupyter run notebooks with this project's Python |

Now look at what changed:
| File / folder | What it is | Edit it by hand? |
|---|---|---|
| `pyproject.toml` | the list of packages **you asked for** (a new `dependencies = [...]` section appeared) | yes, but `uv add` / `uv remove` is easier |
| `uv.lock` | the **exact** version of every package (including the packages your packages need) | ❌ never - uv writes it |
| `.venv/` | the virtual environment: Python + all installed packages, only for this project | ❌ never - you can delete it and run `uv sync` to rebuild it |

## Step 5 - Add your API keys
```bash
cp .env.example .env          # Windows: copy .env.example .env
```
Open `.env` and paste the keys you have (OpenAI and/or Google Gemini are enough to start). **Never** share this file or upload it to GitHub - it is already in `.gitignore`.

## Step 6 - Check everything
```bash
uv run python Day_00_Setup_uv_and_Python/check_setup.py
```
`uv run` = *run this command using the project's `.venv`*. You never have to "activate" anything.

Then open **`hello_notebook.ipynb`** in VS Code, click **Select Kernel → Python Environments → `.venv (Python 3.12)`** and run the cells.
> Prefer Jupyter in the browser? `uv add jupyterlab` and then `uv run jupyter lab`.

---

## 🧰 uv cheat sheet
| I want to... | Command |
|---|---|
| install a package | `uv add langchain` |
| install a package with an *extra* | `uv add "unstructured[pdf]"` (quotes needed!) |
| install a specific / older version | `uv add "langchain==1.5.0"` or `uv add "rich<15"` |
| install a tool only for development | `uv add --dev pytest` |
| install an optional group | `uv add --group finetune peft` → later `uv sync --group finetune` |
| remove a package | `uv remove streamlit` |
| upgrade one package to the latest | `uv add langchain --upgrade-package langchain` |
| upgrade everything | `uv lock --upgrade; uv sync` |
| see what is installed (as a tree) | `uv tree` |
| rebuild `.venv` from `uv.lock` | `uv sync` |
| run a script / app | `uv run python file.py`, `uv run streamlit run app.py` |

## 🧯 Common errors (and how to fix them)
| You see... | It means | Fix |
|---|---|---|
| `ModuleNotFoundError: No module named 'langchain_openai'` | the package is not installed in this project | do the day's **📦 Install** step (`uv add langchain-openai`). Note: you import `langchain_openai` but install `langchain-openai` |
| `No solution found when resolving dependencies` | two packages need versions that can't both be true | read the error from the bottom: it names the package that conflicts. Usually `uv add "that-package<X"` fixes it (see the example below) |
| `error: No pyproject.toml found` | you are not in the course root folder | `cd` to the folder that contains `pyproject.toml` |
| uv installed a surprisingly **old** version (check with `uv tree --depth 1`) | `requires-python` allows future Pythons that the new release doesn't support | make sure `pyproject.toml` says `requires-python = ">=3.12, <3.13"`, then `uv lock --upgrade` |
| `KeyError` / `api_key must be set` | the API key is missing | add it to `.env` (Step 5) |
| Notebook says `No module named ...` but `uv run` works | the notebook uses a different Python | choose the `.venv` kernel (Step 6) |
| 🪟 `UnicodeDecodeError: 'charmap' codec can't decode` | Windows read a UTF-8 file with its old default encoding | `setx PYTHONUTF8 1`, then reopen the terminal and VS Code |
| 🪟 `uv : The term 'uv' is not recognized` | the terminal was opened before uv was installed | close and reopen the terminal |
| 🪟 `running scripts is disabled on this system` | PowerShell blocks scripts by default | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` |
| 🪟 `.sh` files don't run | `.sh` scripts are for macOS/Linux | each day's guide shows the same command for PowerShell; or use Git Bash |

**Example of a real conflict** (it happened while building this course):
```
Because deepeval depends on rich<15.0.0 and your project depends on rich>=15.0.0 ...
your project's requirements are unsatisfiable.
```
Read it like a sentence: *deepeval needs rich below 15, but the project asked for rich 15 or newer*. Fix: let uv choose -> `uv add rich` (no version), or `uv add "rich<15"`.

---
[Course home](../README.md) | [Day_01_How_LLMs_Work_Transformers ->](../Day_01_How_LLMs_Work_Transformers/00_START_HERE.md)
