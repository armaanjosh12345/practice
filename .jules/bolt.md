## 2025-05-22 - FastAPI Concurrency Optimization
**Learning:** In FastAPI, using `async def` for endpoints that perform blocking synchronous I/O (like `requests` calls or standard `sqlite3` operations) blocks the main event loop, severely limiting concurrency.
**Action:** Use standard `def` for I/O-bound endpoints to allow FastAPI to automatically delegate the work to an internal thread pool, maintaining responsiveness for other concurrent requests.
