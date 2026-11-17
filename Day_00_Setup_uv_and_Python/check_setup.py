"""Day 00 - check that your setup works.

Run it from the COURSE ROOT folder:
    uv run python Day_00_Setup_uv_and_Python/check_setup.py
"""
import os
import sys
from pathlib import Path

print("🐍 Python version :", sys.version.split()[0])
print("📁 Python location:", sys.executable)

in_project_venv = ".venv" in Path(sys.executable).parts
print("✅ Using the project's .venv" if in_project_venv else "⚠️  Not using the project's .venv - run this with `uv run ...`")

if sys.platform == "win32":                 # only on Windows
    if sys.flags.utf8_mode:
        print("✅ Python UTF-8 mode is ON")
    else:
        print("⚠️  Python UTF-8 mode is OFF -> run:  setx PYTHONUTF8 1   (then reopen the terminal and VS Code)")

try:
    from dotenv import load_dotenv          # installed with: uv add python-dotenv
except ModuleNotFoundError:
    print("❌ python-dotenv is missing -> run:  uv add python-dotenv")
    sys.exit(1)

found = load_dotenv()                       # looks for a .env file in this folder and the folders above it
print("✅ .env file found" if found else "⚠️  No .env file yet -> run:  cp .env.example .env")

print("\n🔑 API keys (only the first 4 characters are shown):")
for key in ["OPENAI_API_KEY", "GOOGLE_API_KEY", "GROQ_API_KEY"]:
    value = os.getenv(key)
    print(f"   {key:<16} {value[:4] + '...' if value else '— not set yet (that is OK for today)'}")

print("\n🎉 Setup check finished.")
