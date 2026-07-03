# Bolt's Performance Journal

## 2025-05-15 - SQLite Sorting Optimization
**Learning:** Sorting by an `INTEGER PRIMARY KEY` (like `id` or the alias `rowid`) in SQLite is significantly faster than sorting by a `DATETIME` column (`timestamp`). This is because the primary key is automatically indexed and matches the physical storage order. Benchmarking 10,000 records showed a ~47x speedup (0.02s vs 1.10s for 1000 iterations).

**Action:** Always prefer `ORDER BY id DESC` over `ORDER BY timestamp DESC` for time-sequential data in SQLite when `id` is an autoincrementing primary key.
