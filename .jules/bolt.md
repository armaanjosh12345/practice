## 2025-05-15 - Optimize SQLite history retrieval
**Learning:** Sorting by an `INTEGER PRIMARY KEY` in SQLite is significantly more efficient than sorting by a `DATETIME` column, even when both are conceptually sequential. In this codebase, the `id` in `conversation_history` is an autoincrementing primary key, making it a perfect proxy for time-based sorting.
**Action:** Always prefer `ORDER BY id` over `ORDER BY timestamp` when retrieving recent records from SQLite tables where `id` is a primary key and corresponds to insertion order.
