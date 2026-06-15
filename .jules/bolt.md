## 2026-06-15 - Backend Concurrency and Connection Pooling
**Learning:** FastAPI endpoints defined with `async def` that perform blocking I/O (like `requests` or SQLite without an async driver) will block the entire event loop. Moving to `def` allows FastAPI to utilize its internal thread pool. Additionally, `requests.Session()` provides a measurable speedup for repeated LLM API calls via connection pooling.
**Action:** Always prefer `def` for endpoints with blocking I/O in FastAPI. Use `requests.Session()` for persistent connections to local or remote APIs.

## 2026-06-15 - SQLite Primary Key Sorting
**Learning:** Sorting by `INTEGER PRIMARY KEY` in SQLite is faster than sorting by a `DATETIME` column because the primary key is indexed and often stores data in that physical order.
**Action:** Use `ORDER BY id DESC` instead of `ORDER BY timestamp DESC` for recent history lookups when id is an autoincrementing primary key.
