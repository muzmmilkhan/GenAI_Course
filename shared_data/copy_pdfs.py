"""Copy the course's financial PDFs into a folder (works on Windows, macOS and Linux).

Usage (from a Day folder):
    uv run python ../shared_data/copy_pdfs.py data
"""
import shutil
import sys
from pathlib import Path

source = Path(__file__).resolve().parent / "financial_pdfs"
target = Path(sys.argv[1] if len(sys.argv) > 1 else "data")
target.mkdir(parents=True, exist_ok=True)

for pdf in sorted(source.glob("*.pdf")):
    shutil.copy2(pdf, target / pdf.name)
    print(f"📄 copied {pdf.name} -> {target / pdf.name}")
print("✅ done")
