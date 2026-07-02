# Bolt's Performance Journal

## 2026-07-02 - SQLite Primary Key Sorting Speedup
**Learning:** Sorting by an `INTEGER PRIMARY KEY` (like `id`) in SQLite is significantly more efficient than sorting by a `DATETIME` column (like `timestamp`). My benchmarks on 10,000 records showed a ~47x speedup (~1.1s vs ~0.02s for 1000 iterations). This is because the primary key is already indexed and often defines the physical order of rows.
**Action:** Always prefer `ORDER BY id DESC` (or similar primary key) over `ORDER BY timestamp DESC` for time-sequential data in SQLite when possible.
