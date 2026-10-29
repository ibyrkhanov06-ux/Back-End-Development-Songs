#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")/.."
PYTHON="${PYTHON:-python3.9}"
"$PYTHON" --version
"$PYTHON" -m venv backend-songs-venv
source backend-songs-venv/bin/activate
python -m pip install --upgrade pip wheel
python -m pip install -r requirements.txt
python -m pip check
echo "Environment setup completed successfully: backend-songs-venv"
