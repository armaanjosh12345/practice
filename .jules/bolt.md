# Bolt's Performance Journal

## 2025-05-15 - SQLite History Retrieval Optimization
**Learning:** In SQLite, sorting by an `INTEGER PRIMARY KEY` (like `id`) is significantly faster than sorting by a `DATETIME` column because the table is physically stored in the order of the primary key. For a table with 10,000 records, `ORDER BY id DESC` provided a ~50x speedup compared to `ORDER BY timestamp DESC`.
**Action:** Always prefer sorting by `id` (or rowid) for time-sequential data in SQLite if the ID is autoincrementing.

## 2025-05-15 - Persistent Connection for LLM Interactions
**Learning:** Using `requests.Session()` allows for TCP and TLS connection reuse. For applications that make frequent external API calls (like to an Ollama LLM), this reduces the overhead of the handshake for every request.
**Action:** Implement `requests.Session()` at the class level for any component making repeated HTTP requests.

## 2025-05-15 - Micro-optimization: Module-level Imports
**Learning:** Inline imports (e.g., `import re` inside a function) add a small overhead for every call as Python checks the sys.modules cache.
**Action:** Keep standard library imports at the top-level of the module unless there is a strong reason (like circular dependencies) not to.
