## 2026-06-21 - SQLite Primary Key Sorting
**Learning:** Sorting by an `INTEGER PRIMARY KEY` (id) in SQLite is significantly more efficient (~10x for 10k rows, ~500x for 100k rows) than sorting by a `DATETIME` column (timestamp), as the PK is already indexed and optimized for numerical sorting.
**Action:** Always prefer `ORDER BY id DESC` for chronological ordering in SQLite when an `AUTOINCREMENT` primary key is available.

## 2026-06-21 - SQLite Indexing for Stats
**Learning:** Queries that aggregate data with filters (e.g., `SELECT AVG(pnl) FROM trade_log WHERE status="CLOSED"`) are bottlenecked by full table scans without indexes on the filtered columns.
**Action:** Proactively add indexes to columns used in `WHERE` clauses for statistical queries.
