# Back-End-Development-Songs

Flask REST API with MongoDB persistence. Endpoints: GET /health, GET /count, GET /song, GET /song/<id>, POST /song, PUT /song/<id>, DELETE /song/<id>.

Set MONGODB_URI or MONGODB_SERVICE (default 127.0.0.1:27018), then run python -m flask run --port 5001. Seed data is imported only into an empty collection.

Verified locally against a real MongoDB 8.0 server: health and list return 200, create 201, update 200, delete 204.

Based on the IBM Skills Network starter template. Implementation assistance: OpenAI Codex. Cloud deployment evidence is not yet available.
