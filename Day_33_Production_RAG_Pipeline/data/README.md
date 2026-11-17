# data/ - the PDF inbox 📥

Put the PDF files you want the RAG system to read in this folder.
To use the course's financial reports, run this **from this Day folder** (works on Windows, macOS and Linux):

```bash
uv run python ../shared_data/copy_pdfs.py data
```
The watcher notices new PDFs here and indexes them automatically.
