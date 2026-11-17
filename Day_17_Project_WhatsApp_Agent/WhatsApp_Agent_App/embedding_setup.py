"""Embedding model used by the WhatsApp agent's long-term memory."""
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv(override=True)


def get_gemini_embedding_model():
    """Return Google's Gemini embedding model (needs GOOGLE_API_KEY in .env)."""
    return GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
