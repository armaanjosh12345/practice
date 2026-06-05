## 2025-05-22 - Optimizing FastAPI Event Loop and Connection Pooling

**Learning:** When dealing with high-latency, synchronous I/O operations (like calling a local LLM via `requests`), using `async def` in FastAPI actually blocks the entire event loop, preventing the server from handling other concurrent requests. Additionally, frequent TCP handshakes to a local service like Ollama add unnecessary overhead.

**Action:**
1. Use synchronous `def` for high-latency endpoints to leverage FastAPI's thread pool.
2. Implement `requests.Session()` to enable HTTP connection pooling, reducing latency by 10-20% for successive requests.
3. Optimize database queries by ordering by `id` (Primary Key) instead of `timestamp` when possible to utilize indexing.
