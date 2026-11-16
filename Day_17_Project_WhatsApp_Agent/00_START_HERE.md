# Day 17 - Project - WhatsApp AI Agent

**What you will learn:** Connect a LangGraph agent to WhatsApp using Twilio, with SQLite chat memory and MongoDB long-term memory.

## Before you start
- Do the one-time setup in the [course README](../README.md) (`uv sync` + `.env`).
- Open a terminal **inside this folder**:
  ```bash
  cd Day_17_Project_WhatsApp_Agent
  ```
- Keys: `OPENAI_API_KEY`, `GOOGLE_API_KEY`, `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `MONGODB_URI`. `embedding_setup.py` links to the Day 15 copy.

## Lessons (do them in this order)
| # | Lesson | How to run |
|---|--------|------------|
| 1 | Prototype in a notebook | open 01_whatsapp_agent.ipynb |
| 2 | Read WhatsApp_Agent_App/README.md | - |
| 3 | Run the server | `cd WhatsApp_Agent_App && uv run uvicorn main:app --port 8000` |
| 4 | Expose it to Twilio | `ngrok http 8000` |

> `.ipynb` files are Jupyter notebooks. Open them in VS Code (choose the `.venv` kernel from the course root) or run `uv run jupyter lab` from the course root.

---
[<- Day_16_Short_and_Long_Term_Memory](../Day_16_Short_and_Long_Term_Memory/00_START_HERE.md) | [Day_18_Planning_and_Deep_Research_Agents ->](../Day_18_Planning_and_Deep_Research_Agents/00_START_HERE.md)
