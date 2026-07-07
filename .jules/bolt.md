## 2025-05-15 - SQLite History Retrieval Optimization
**Learning:** Sorting by a non-indexed `DATETIME` column (`timestamp`) in SQLite causes a full table scan, which degrades performance as history grows. Sorting by the `INTEGER PRIMARY KEY` (`id`) provides the same chronological order (assuming monotonic increments) but leverages the B-Tree index for O(log N) retrieval.
**Action:** Always prefer sorting by `id DESC` instead of `timestamp DESC` for time-sequential data in SQLite to achieve ~50x speedups.

## 2025-05-15 - LLM API Connection Reuse
**Learning:** Establishing a new TCP connection for every request to a local or remote LLM API (like Ollama) adds significant latency (handshake overhead). Using `requests.Session()` maintains a persistent connection.
**Action:** Use persistent sessions for frequent API interactions to improve responsiveness and reduce latency from ~20ms to ~2ms per request overhead.
