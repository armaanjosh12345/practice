## 2025-05-22 - [Optimized LLM Loop and System Info]
**Learning:** In a local AI agent architecture, the communication overhead with the LLM (Ollama) and frequent system stat polling can introduce cumulative latency. Using `requests.Session()` for connection pooling and caching static platform info (OS, version) provides a measurable reduction in response time and CPU overhead.
**Action:** Always prefer persistent sessions for frequent local API calls and cache immutable system metadata during initialization.
