## 2025-05-15 - SQLite History Retrieval Optimization

**Learning:** Sorting by a non-indexed `DATETIME` column in SQLite becomes a significant bottleneck as the table grows. In the `conversation_history` table, sorting by `timestamp DESC` for 10,000 records was ~50x slower than sorting by the `INTEGER PRIMARY KEY` (`id`).

**Action:** Always prefer sorting by the auto-incrementing primary key (`id`) instead of a `timestamp` column for chronological retrieval in SQLite, as it leverages the default index and provides the same ordering for sequential inserts.
