## 2025-05-22 - Optimizing FastAPI Concurrency for Blocking I/O

**Learning:** In FastAPI, defining a route with `async def` while performing blocking synchronous operations (like `requests` or `sqlite3` without an async driver) blocks the main event loop. This serializes all requests, making the application feel slow and unresponsive under load. Using a standard `def` allows FastAPI to delegate the work to an internal thread pool, enabling concurrent request processing.

**Action:** Always use `def` for route handlers that perform blocking synchronous I/O. Reserve `async def` for handlers that exclusively use `await` with asynchronous libraries.
