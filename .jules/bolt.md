# Bolt's Performance Journal ⚡

## 2025-05-22 - FastAPI Event Loop Blocking and Connection Overhead
**Learning:** In a FastAPI application using an LLM (like Ollama), defining the endpoint as `async def` while calling a synchronous, high-latency LLM library (like `requests`) blocks the entire event loop. This prevents the server from handling concurrent requests, such as real-time system monitoring or heartbeat checks. Additionally, creating a new HTTP connection for every LLM request adds significant TCP handshake overhead.

**Action:** Define high-latency endpoints as standard `def` to let FastAPI delegate them to its thread pool, and use `requests.Session()` for connection pooling to minimize request overhead.
