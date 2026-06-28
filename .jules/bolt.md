## 2025-05-15 - SQLite Primary Key Indexing for History Retrieval
**Learning:** Sorting by an `INTEGER PRIMARY KEY` in SQLite is significantly more efficient than sorting by a `DATETIME` column. In the `conversation_history` table, switching from `ORDER BY timestamp DESC` to `ORDER BY id DESC` resulted in a ~47x speedup for 10,000 records.
**Action:** Always prefer sorting by primary key when it correlates with the desired chronological order (like auto-increment IDs for history/logs).
