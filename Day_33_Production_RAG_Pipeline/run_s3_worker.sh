#!/bin/bash

# Get directory of this script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$DIR"


echo "Starting S3 Ingestion Worker in unbuffered mode..."
# Uses the course-wide uv environment (run `uv sync` once in the course root)
exec uv run python -u src/embedding_service/s3_worker.py
