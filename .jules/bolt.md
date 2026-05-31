## 2025-05-23 - Backend Request Path Optimization
**Learning:**
1. Using `async def` in FastAPI for endpoints that perform blocking I/O (like LLM calls via `requests`) blocks the main event loop. FastAPI's behavior of running synchronous `def` endpoints in an internal thread pool is the correct way to handle these cases.
2. HTTP connection pooling with `requests.Session` provides a significant latency reduction for local service communication (Ollama).
3. **Thread Safety Anti-pattern**: Sharing a single `sqlite3` connection object across threads in a FastAPI thread pool is unsafe for concurrent writes and can lead to database corruption or locking issues. Reverting to open-on-demand connections is safer unless a proper connection pool (like SQLAlchemy's) is used.
4. Sorting by `id DESC` in SQLite is faster than `timestamp DESC` because `id` is the primary key and indexed by default.

**Action:**
- Prefer synchronous `def` for long-running LLM processing in FastAPI.
- Always use `requests.Session()` for repeated API calls to the same host.
- Avoid sharing raw `sqlite3` connections across threads; use connection pooling if persistent connections are required.
- Use primary keys for sorting whenever possible.
