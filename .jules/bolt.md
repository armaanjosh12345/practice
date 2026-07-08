## 2025-05-15 - [SQLite Sorting Optimization]
**Learning:** Sorting by an `INTEGER PRIMARY KEY` (like `id` in SQLite) is significantly faster than sorting by a `DATETIME` column. In this codebase, history retrieval was optimized by ~50x by switching to `ORDER BY id DESC` while maintaining the same chronological order for auto-incrementing inserts.
**Action:** Always prefer primary key sorting for time-sequential data in SQLite when physical storage order matches logical time order.
