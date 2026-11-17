# Generative AI


## 1. How setup works in this course (install as you learn)

There is **no "install everything" step**. Instead you build your own Python project, one day at a time:

1. **Day 00** (once, ~15 minutes): install `uv`, create your project with `uv init`, add your first packages and your `.env` file.
   👉 Start here: [`Day_00_Setup_uv_and_Python/00_START_HERE.md`](Day_00_Setup_uv_and_Python/00_START_HERE.md)
2. **Every day after that** begins with **📦 Step 1 – Install today's packages** in its `00_START_HERE.md`, for example:
   ```bash
   uv add langchain-chroma faiss-cpu       # Day 07
   ```
   You see exactly which library each lesson needs and why. Installs always use the **latest** versions.
3. If an install or import fails, every day has a **🧯 Something went wrong?** box with the real error messages and their fixes.
4. **Days 34, 36 and 37 get their own small environment** inside their Day folder. With the latest versions, DeepEval and Google ADK
   need library versions that clash with LangChain's, so (like real teams) we keep those apps separate. Each of those days explains why.

**🪟 Windows, 🍎 macOS and 🐧 Linux are all supported.** Windows users: use PowerShell and run `setx PYTHONUTF8 1` once (Day 00 explains why).
Extra system tools for a few days (Poppler/Tesseract for Days 08 & 33, Docker Desktop for Days 16, 25, 32, 33, Node.js for Day 27) - install commands for every OS are in Day 00.

> 👩‍🏫 **Teachers:** `instructor/` contains the tested `pyproject.toml` + `uv.lock` of every environment (main, Day 34, Day 36, Day 37) plus an all-in-one backup.
> See [`instructor/README.md`](instructor/README.md) for how to repair a broken student environment.

## 2. How to run a lesson

Every Day folder has a **`00_START_HERE.md`** that lists the lessons in order and the exact command for each one.

🐍 **New to Python?** Every Day folder also has **`00_python_basics.ipynb`** — start with it! It teaches only the Python used in that day (variables → lists → functions → dicts → classes → async → …) in very small steps, with comments, practice exercises and solutions. It needs no API key and no internet.

```bash
cd Day_03_LLMs_ChatModels_and_Embeddings      # always run from INSIDE the day folder
uv run python 1_llm.py                         # Python scripts
uv run streamlit run 6_prompt_ui.py            # Streamlit apps (Day 04 example)
```

**Notebooks (`.ipynb`):** open them in VS Code and select the kernel `.venv (Python 3.12)` from this course folder,
or start Jupyter with `uv run jupyter lab` from the course root.

**HTML visualizers:** just double-click the `.html` file to open it in your browser.

## 3. Course map

### Module 0 - Setup

| Day | Topic | You will learn |
|---|---|---|
| [00](Day_00_Setup_uv_and_Python/00_START_HERE.md) | **Setup: Python, uv and Your Project** | Install uv, create your project with `uv init`, install packages with `uv add`, and understand `pyproject.toml`, `uv.lock` and `.venv`. |

### Module 1 - How LLMs work

| Day | Topic | You will learn |
|---|---|---|
| [01](Day_01_How_LLMs_Work_Transformers/00_START_HERE.md) | **How LLMs Work - The Transformer** | What happens inside a Large Language Model: tokens, embeddings, self-attention, encoder/decoder blocks, training and how the next word is sampled. |
| [02](Day_02_BERT_GPT_T5_Model_Families/00_START_HERE.md) | **BERT vs GPT vs T5 - Model Families** | The three transformer families: encoder-only (BERT), decoder-only (GPT) and encoder-decoder (T5), and when to use each. |

### Module 2 - LangChain basics

| Day | Topic | You will learn |
|---|---|---|
| [03](Day_03_LLMs_ChatModels_and_Embeddings/00_START_HERE.md) | **Talking to LLMs, Chat Models & Embeddings** | Call an LLM from Python, control creativity with temperature, use OpenAI / Google / Hugging Face chat models, create embeddings and measure document similarity. |
| [04](Day_04_Prompts_and_Chatbots/00_START_HERE.md) | **Prompts, Messages & Your First Chatbot** | Prompt templates, chat prompt templates, message types, message placeholders (chat history) and a simple chatbot with a Streamlit UI. |
| [05](Day_05_Structured_Output_and_Parsers/00_START_HERE.md) | **Structured Output & Output Parsers** | Make the LLM return clean data (dicts / JSON / Pydantic objects) instead of free text. |
| [06](Day_06_LangChain_Chains/00_START_HERE.md) | **LangChain Chains (LCEL)** | Connect prompts, models and parsers with the `|` operator: simple, sequential, parallel and conditional (branching) chains. |

### Module 3 - RAG

| Day | Topic | You will learn |
|---|---|---|
| [07](Day_07_RAG_Fundamentals/00_START_HERE.md) | **RAG Fundamentals - Retrieval Augmented Generation** | Give an LLM your own documents: load -> split -> embed -> store in a vector DB (Chroma) -> retrieve -> answer. |
| [08](Day_08_RAG_Chunking_Strategies/00_START_HERE.md) | **RAG Chunking Strategies & Multi-modal RAG** | How you split documents changes answer quality: recursive, semantic and agentic (LLM-driven) chunking, plus RAG over PDFs with images and tables. |
| [09](Day_09_RAG_Advanced_Retrieval/00_START_HERE.md) | **Advanced Retrieval** | Better retrieval: similarity / MMR / threshold search, multi-query, reciprocal rank fusion, hybrid (BM25 + vector) search and re-ranking. |

### Module 4 - Agents & LangGraph

| Day | Topic | You will learn |
|---|---|---|
| [10](Day_10_Agents_From_Scratch_ReAct/00_START_HERE.md) | **Build an AI Agent From Scratch (ReAct)** | What an agent really is - a loop of Thought -> Action -> Observation - written in plain Python with no framework. |
| [11](Day_11_LangGraph_Basics_Workflows/00_START_HERE.md) | **LangGraph Basics - Workflows as Graphs** | State, nodes, edges and conditional edges. Build simple LLM workflows, a sentiment-based review-reply flow, a RAG graph and an iterative post generator. |
| [12](Day_12_LangGraph_Memory_and_Persistence/00_START_HERE.md) | **LangGraph Memory & Persistence** | Checkpointers: make a chatbot remember the conversation (in memory and in SQLite), inspect/replay intermediate states. |
| [13](Day_13_LangGraph_Tools_and_Human_in_the_Loop/00_START_HERE.md) | **Tools & Human-in-the-Loop** | Let the LLM call tools (search, calculator, stock price) with ToolNode, then pause the graph for human approval (interrupt / resume). |
| [14](Day_14_LangGraph_MapReduce_and_MultiAgent/00_START_HERE.md) | **Map-Reduce & Your First Multi-Agent System** | Process many documents in parallel with Send() (map-reduce over financial PDFs) and build a research agent + chart agent team. |
| [15](Day_15_Advanced_RAG_with_LangGraph/00_START_HERE.md) | **Advanced RAG with LangGraph (Self-RAG / Corrective RAG)** | Agentic RAG: grade retrieved documents, rewrite queries, fall back to web search and check answers for hallucination. |
| [16](Day_16_Short_and_Long_Term_Memory/00_START_HERE.md) | **Short-Term & Long-Term Memory** | Trim / summarise chat history (short-term) and store facts about the user across sessions (long-term) in memory and in Postgres. |
| [17](Day_17_Project_WhatsApp_Agent/00_START_HERE.md) | **Project - WhatsApp AI Agent** | Connect a LangGraph agent to WhatsApp using Twilio, with SQLite chat memory and MongoDB long-term memory. |
| [18](Day_18_Planning_and_Deep_Research_Agents/00_START_HERE.md) | **Planning & Deep-Research Agents** | Agents that plan first, research in parallel and write long structured reports / blog posts (with images). |

### Module 5 - Multi-agent systems (LangChain v1)

| Day | Topic | You will learn |
|---|---|---|
| [19](Day_19_LangChain_Agents_RAG_SQL_Middleware/00_START_HERE.md) | **LangChain v1 Agents - RAG Agent, SQL Agent & Middleware** | `create_agent` from LangChain v1: a RAG agent, and a SQL agent protected by human-approval and PII-redaction middleware. |
| [20](Day_20_Multi_Agent_Subagents_Pattern/00_START_HERE.md) | **Multi-Agent Pattern 1 - Supervisor & Sub-agents** | A supervisor agent that delegates work to specialist sub-agents (travel planner, personal assistant, deep research). |
| [21](Day_21_Multi_Agent_Handoffs_and_Swarm/00_START_HERE.md) | **Multi-Agent Pattern 2 - Handoffs & Swarm** | Agents that hand the conversation over to each other (mortgage underwriting) and a fully connected support swarm. |
| [22](Day_22_MapReduce_and_Router_Agents/00_START_HERE.md) | **Multi-Agent Pattern 3 - Map-Reduce & Router** | Fan-out work to parallel agents and merge the results (Send API), and route questions to the right knowledge source. |
| [23](Day_23_Project_Trip_Planner_Multi_Agent/00_START_HERE.md) | **Project - Multi-Agent Trip Planner** | A full app: hotel + flight sub-agents, human approval before booking, SQLite persistence, FastAPI backend with web UI. |
| [24](Day_24_Project_Fashion_Brand_Agent/00_START_HERE.md) | **Project - Fashion Brand Shopping Agent** | A shopping assistant agent that queries a MySQL product catalogue, with a FastAPI backend and HTML frontend. |

### Module 6 - MCP (Model Context Protocol)

| Day | Topic | You will learn |
|---|---|---|
| [25](Day_25_MCP_Fundamentals_and_Servers/00_START_HERE.md) | **MCP Fundamentals - Model Context Protocol** | What MCP is, build MCP servers (filesystem, email copilot, health monitor) and an MCP client with a Streamlit chat UI. |
| [26](Day_26_MCP_ML_Model_Server_Salary_Prediction/00_START_HERE.md) | **MCP - Serve a Machine-Learning Model** | Wrap a scikit-learn salary model (with SHAP explanations) as MCP tools and call them from a LangChain agent. |
| [27](Day_27_MCP_with_LangChain_Agents/00_START_HERE.md) | **MCP + LangChain Agents** | Connect an agent to several MCP servers at once (AWS documentation + browser automation) and give it a chat UI. |
| [28](Day_28_Remote_MCP_FreeCAD/00_START_HERE.md) | **Remote MCP - Control FreeCAD with AI** | RPC vs REST, XML-RPC basics, then a remote MCP server that drives the FreeCAD 3D-CAD app from Claude Desktop. |

### Module 7 - Advanced agent projects

| Day | Topic | You will learn |
|---|---|---|
| [29](Day_29_Deep_Agents/00_START_HERE.md) | **Deep Agents** | Long-running agents with planning, a virtual filesystem, sub-agents and skills - built into a forensic financial audit agent (DeepAudit). |
| [30](Day_30_Project_PPT_Agent/00_START_HERE.md) | **Project - PowerPoint Generation Agent** | An agent that plans a slide deck, generates images with Gemini, asks for your approval and builds a real .pptx file. |
| [31](Day_31_Project_Voice_Agent/00_START_HERE.md) | **Project - Real-Time Voice Agent** | Speech-to-text -> agent -> text-to-speech, streamed over WebSockets with async Python. |

### Module 8 - Production, evaluation & fine-tuning

| Day | Topic | You will learn |
|---|---|---|
| [32](Day_32_Production_HITL_LinkedIn_Agent/00_START_HERE.md) | **Production - Human-in-the-Loop LinkedIn Agent** | A production-style LangGraph app: draft -> human review -> revise -> publish, with FastAPI, SQLite checkpoints, tests, Docker and CI/CD. |
| [33](Day_33_Production_RAG_Pipeline/00_START_HERE.md) | **Production - Multi-modal Financial RAG Pipeline** | PDF pages -> images -> Gemini embeddings -> Qdrant, with a file watcher, an S3 worker, a FastAPI service, Docker and AWS CI/CD. |
| [34](Day_34_RAG_Evaluation_DeepEval/00_START_HERE.md) | **Evaluating RAG with DeepEval** | Golden datasets, retriever / generator / pipeline metrics, LLM-as-judge, safety, cost & latency evaluation and regression gates. |
| [35](Day_35_Fine_Tuning_LLMs/00_START_HERE.md) | **Fine-Tuning an LLM (Gemma + QLoRA)** | Build a dataset, fine-tune Gemma 2B with LoRA/QLoRA, and serve it (FastAPI / vLLM). |

### Module 9 - Google ADK & cloud deployment

| Day | Topic | You will learn |
|---|---|---|
| [36](Day_36_Google_ADK_Agents/00_START_HERE.md) | **Google Agent Development Kit (ADK)** | Build agents with Google ADK: a simple tool bot, a Vertex AI RAG agent, a multi-agent podcast generator and a software-testing agent. |
| [37](Day_37_Deploy_ADK_to_Google_Cloud/00_START_HERE.md) | **Deploy ADK Agents to Google Cloud** | Deploy the Day 36 agents to Vertex AI Agent Engine and Cloud Run, then call them from an API server and a web UI. |
| [38](Day_38_Cloud_Deployment_Options_AWS/00_START_HERE.md) | **Cloud Deployment Options (AWS & others)** | Where to host GenAI apps: EC2, ECS, Lambda, App Runner, SageMaker, Bedrock - compared with other clouds. |

## 4. Folder layout

```
GenAI_Course/
├── README.md              <- you are here
├── pyproject.toml         <- created by YOU on Day 00, grows every day with `uv add`
├── .python-version        <- created on Day 00 (Python 3.12)
├── instructor/            <- teacher's reference: tested pyproject.toml + uv.lock for every environment
├── .env.example           <- copy to .env and add your keys
├── Day_00_... Day_38_...  <- one folder per day, each with 00_START_HERE.md
├── shared_data/
│   └── financial_pdfs/    <- JPM / EY annual reports (stored once, used by Days 14, 15, 29, 33, 34)
└── Extras/                <- leftover images that no lesson uses
```
