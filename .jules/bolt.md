## 2025-05-14 - FastAPI Concurrency Optimization

**Learning:** Using `async def` for FastAPI endpoints that perform synchronous, blocking I/O (like local LLM requests via `requests`, system stat gathering with `psutil`, or SQLite operations) blocks the main event loop. This prevents the server from handling other concurrent requests efficiently.

**Action:** Define path operations as synchronous `def` instead of `async def` when they involve blocking I/O. FastAPI will automatically run these in a thread pool, maintaining the responsiveness of the event loop for other tasks.
