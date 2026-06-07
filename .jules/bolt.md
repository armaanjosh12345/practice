## 2025-05-22 - LLM Request & Event Loop Optimization
**Learning:** In FastAPI, using `async def` for endpoints that perform blocking synchronous I/O (like `requests` calls to an LLM) blocks the main event loop, killing concurrency. Additionally, repeated HTTP calls without a session incur significant handshake overhead.
**Action:** Use `def` for blocking synchronous endpoints to leverage FastAPI's thread pool, and always use `requests.Session()` for connection pooling to local or remote services.

## 2025-05-22 - Primary Key Indexing for History
**Learning:** Sorting by `timestamp` in SQLite can become a bottleneck as tables grow if not indexed. Sorting by the auto-incrementing Primary Key (`id`) is usually equivalent for chronological history and much faster as it's indexed by default.
**Action:** Prefer `ORDER BY id` over `ORDER BY timestamp` for chronological retrieval when possible.
