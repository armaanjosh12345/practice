## 2025-05-14 - FastAPI Blocking I/O & SQLite Indexing

**Learning:** Using `async def` in FastAPI for endpoints that perform synchronous blocking I/O (like `requests` calls or `sqlite3` queries) blocks the main event loop. This prevents the server from handling concurrent requests. Also, sorting by `INTEGER PRIMARY KEY` in SQLite is faster than sorting by `DATETIME` columns.

**Action:** Use synchronous `def` for FastAPI endpoints that involve blocking I/O to leverage FastAPI's internal thread pool. Always use `id` for chronological sorting in SQLite when possible, and index frequently filtered/sorted columns like `status`.
