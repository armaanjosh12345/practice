## 2025-05-22 - FastAPI Concurrency and SQLite Indexing

**Learning:** Using `async def` for endpoints that perform blocking I/O (SQLite, Requests, System stats) stalls the FastAPI event loop, as these operations are not natively asynchronous in the current implementation. Switching to `def` allows FastAPI to delegate these tasks to its internal thread pool, significantly improving throughput and responsiveness under concurrent load. Additionally, sorting by an `INTEGER PRIMARY KEY` (which acts as a `ROWID` alias) in SQLite is much more efficient than sorting by a `DATETIME` column, as it leverages the primary B-tree index directly.

**Action:** For any endpoint performing blocking I/O without `await`, prefer `def` over `async def`. When fetching the latest records in SQLite, use `ORDER BY id DESC` instead of `ORDER BY timestamp DESC` when the ID is an auto-incrementing primary key.
