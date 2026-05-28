## 2025-05-22 - [Connection Pooling for LLM Requests]
**Learning:** Reusing TCP connections with `requests.Session` significantly reduces latency when making frequent requests to a local service like Ollama. In a local benchmark server, this resulted in a ~20% reduction in request overhead.
**Action:** Always use `requests.Session` for persistent backend-to-backend or backend-to-LLM communications.
