## 2025-05-14 - [LLM Request Latency & FastAPI Blocking]
**Learning:** In FastAPI, using `async def` for endpoints that perform blocking I/O (like synchronous HTTP requests to an LLM) blocks the main event loop. Reusing TCP connections via `requests.Session` significantly reduces overhead for local API calls.
**Action:** Use `def` (instead of `async def`) for blocking endpoints to leverage FastAPI's thread pool. Always use `requests.Session` for repeated calls to the same host (e.g., Ollama).

## 2025-05-14 - [Database Sorting Performance]
**Learning:** Sorting by `timestamp` in SQLite without an index is slower than sorting by the `id` (Primary Key), which is indexed by default.
**Action:** Prefer `ORDER BY id DESC` for retrieving recent history in SQLite if `id` is an autoincrementing integer.
