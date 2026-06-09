# Bolt's Performance Journal - Quantum Sandbox

## 2025-05-22 - LLM Connection Pooling and FastAPI Concurrency
**Learning:** The backend uses `requests.post` inside an `async def` FastAPI endpoint. This blocks the event loop. Moving to `def` allows FastAPI to use a thread pool. Additionally, `requests.Session` enables TCP connection pooling, reducing overhead for repeated LLM calls.
**Action:** Always use `requests.Session` for internal service communication and avoid `async def` for blocking I/O in FastAPI.

## Baseline Performance
- `pytest tests/test_logic.py`: ~0.20s (logic only, mocked LLM)
- `pytest` full suite: ~0.53s
- Request overhead (mocked): TBD
