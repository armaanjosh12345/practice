# Bolt's Performance Journal

## 2025-05-22 - Ollama Connection Pooling & Async vs Sync FastAPI
**Learning:** Using `requests.Session` for local API calls to Ollama reduces overhead by ~10-20% due to TCP connection reuse. Defining FastAPI endpoints as `def` instead of `async def` for blocking I/O (like LLM requests) prevents the event loop from being blocked, allowing the framework to manage threading efficiently.

**Action:** Always use sessions for repeated HTTP calls and prefer `def` for blocking logic in FastAPI.
