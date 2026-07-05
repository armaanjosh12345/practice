# Bolt's Performance Journal

## 2025-05-15 - SQLite Primary Key Sorting Speedup
**Learning:** In SQLite, sorting by an `INTEGER PRIMARY KEY` (like `id`) is significantly faster than sorting by a `DATETIME` column, even if they logically represent the same order. This is because the primary key is used as the underlying rowid and is already indexed/stored in that physical order.
**Action:** Always prefer `ORDER BY id DESC` over `ORDER BY timestamp DESC` for time-sequential data retrieval when an auto-incrementing ID is present. Measured a ~50x speedup for 10,000 records.
