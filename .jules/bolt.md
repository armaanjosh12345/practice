## 2025-05-21 - SQLite Primary Key Sorting & FastAPI Concurrency

**Learning:** In SQLite, sorting by an `INTEGER PRIMARY KEY` (which is often an alias for `rowid`) is significantly faster than sorting by a `DATETIME` column because the table is physically stored as a B-tree keyed by `rowid`. Additionally, using `async def` in FastAPI for endpoints that perform synchronous blocking I/O (like `requests` calls) blocks the main event loop, starving other requests.

**Action:**
1. Use `ORDER BY id DESC` (if `id` is the `INTEGER PRIMARY KEY`) instead of `ORDER BY timestamp DESC` when chronological order is maintained by insertion.
2. Define FastAPI route handlers as synchronous `def` instead of `async def` when they perform blocking I/O, allowing FastAPI to manage them via its internal thread pool.
3. Utilize `requests.Session()` to enable HTTP connection pooling and reduce handshake latency for consecutive requests to the same host (e.g., local LLM APIs).
>>>>>>> REPLACE
