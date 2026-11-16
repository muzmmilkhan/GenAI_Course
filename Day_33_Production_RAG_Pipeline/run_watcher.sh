#!/bin/bash

# Get directory of this script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$DIR"


# Run the watcher script using the virtual environment python
echo "Starting watcher service using virtual environment..."
# Uses the course-wide uv environment (run `uv sync` once in the course root)
exec uv run python -u watcher.py
