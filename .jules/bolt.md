## 2026-06-04 - Connection Pooling and Threading Optimizations

**Learning:** Reusing TCP connections with `requests.Session` in the backend provides a measured performance improvement in request overhead when communicating with local services like Ollama. Additionally, switching blocking LLM calls from `async def` to `def` in FastAPI allows for better concurrency by utilizing the worker thread pool.

**Action:** Always use `requests.Session()` for repeated API calls to the same host. For long-running synchronous tasks in FastAPI, prefer `def` over `async def` to avoid blocking the main event loop.
