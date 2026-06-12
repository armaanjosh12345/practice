## 2025-05-22 - Backend Concurrency Bottleneck
**Learning:** FastAPI endpoints defined with `async def` run on the main event loop. If they call synchronous blocking functions (like `requests` or SQLite without an async driver), they block the entire application.
**Action:** Use standard `def` for synchronous/blocking endpoints in FastAPI. This offloads the work to a thread pool, allowing the event loop to remain responsive for other requests.

## 2025-05-22 - SQLite Sorting Performance
**Learning:** Sorting by `DATETIME` columns in SQLite is significantly slower than sorting by an `INTEGER PRIMARY KEY` due to internal representation and indexing efficiency.
**Action:** Use `ORDER BY id` instead of `ORDER BY timestamp` for chronological sorting when `id` is an autoincrementing primary key.
