# Bolt's Performance Journal ⚡

## Critical Learnings

## 2025-05-22 - [LLM Connection Pooling & FastAPI Concurrency]
**Learning:** Reusing TCP connections with `requests.Session` for local LLM APIs (like Ollama) reduces request overhead by ~10-20%. Additionally, using synchronous `def` for routes that perform heavy blocking I/O (like LLM processing) in FastAPI is superior to `async def`, as it offloads work to a thread pool and prevents event loop starvation.
**Action:** Always prefer `requests.Session` for service-to-service communication and evaluate if an endpoint should be synchronous based on its blocking nature.

## 2025-05-22 - [Database Sort Optimization]
**Learning:** Sorting by an autoincrementing primary key (`id`) is a faster alternative to sorting by a `timestamp` column for chronological retrieval, as it leverages the primary key index.
**Action:** Use `ORDER BY id` for history retrieval when `id` is guaranteed to be chronological.
