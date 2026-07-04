## 2025-05-15 - Optimize SQLite history retrieval
**Learning:** Sorting by an `INTEGER PRIMARY KEY` (like `id`) in SQLite is significantly more efficient than sorting by a `DATETIME` column (like `timestamp`). In a table with 10,000 records, `ORDER BY id DESC` was measured to be ~47x faster than `ORDER BY timestamp DESC`. This is because the primary key is already indexed and often corresponds to the physical storage order.
**Action:** Prefer sorting by `id DESC` (alias for rowid) over a `DATETIME` column for time-sequential data in SQLite to leverage the automatic primary key index.
