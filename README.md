# Back-End-Development-Songs

Flask REST API with MongoDB persistence. Endpoints: GET /health, GET /count, GET /song, GET /song/<id>, POST /song, PUT /song/<id>, DELETE /song/<id>.

Set MONGODB_URI or MONGODB_SERVICE (default 127.0.0.1:27018), then run python -m flask run --port 5001. Seed data is imported only into an empty collection.

Verified locally against a real MongoDB 8.0 server: health and list return 200, create 201, update 201 (course API contract), delete 204.

Based on the IBM Skills Network starter template. Implementation assistance: OpenAI Codex. Songs and MongoDB were deployed to OpenShift; the deployed /health endpoint returns status OK.

## Environment Setup

This repository was created from the IBM Skills Network starter template:
https://github.com/ibm-developer-skills-network/hvlga-Back-End-Development-Songs
The starter was cloned locally and the implemented source published here.

The revised `bin/setup.sh` was successfully executed in the Cloud IDE using
the official `python:3.9.16-slim` container (Python 3.9.16). It creates the
`backend-songs-venv` virtual environment, installs requirements, and runs `pip check`.
The observed result was `No broken requirements found.` followed by
`Environment setup completed successfully: backend-songs-venv`.

```bash
bash bin/setup.sh
source backend-songs-venv/bin/activate
python --version
```

For the same isolated setup used during verification:
```bash
docker run --rm -v "$PWD:/app" -w /app python:3.9.16-slim bash bin/setup.sh
```
The setup script avoids modifying global shell configuration or starting an unrelated database.
