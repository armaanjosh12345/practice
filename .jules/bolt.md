## 2025-05-15 - SQLite Sorting Optimization
**Learning:** Sorting by an `INTEGER PRIMARY KEY` in SQLite is significantly more efficient than sorting by a non-indexed `DATETIME` column. Benchmarks showed a ~98% reduction in query time for a 10k row table.
**Action:** Always prefer `ORDER BY primary_key` for fetching recent records if the primary key is auto-incrementing and correlates with time.

## 2025-05-15 - FastAPI Concurrency and Blocking I/O
**Learning:** Using `async def` for FastAPI endpoints that perform blocking I/O (like SQLite queries, `psutil` calls, or synchronous `requests`) blocks the entire event loop, preventing true concurrency.
**Action:** Use standard `def` for endpoints with blocking I/O to allow FastAPI to handle them in its internal thread pool.

## 2025-05-15 - Connection Pooling for Local LLM
**Learning:** Repeatedly opening and closing TCP connections for high-frequency requests to a local LLM API (like Ollama) adds unnecessary overhead.
**Action:** Use `requests.Session()` to leverage connection pooling and reduce request latency.
