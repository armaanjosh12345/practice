## 2025-05-15 - [SQLite Sorting Optimization]
**Learning:** Sorting by an `INTEGER PRIMARY KEY` (like `id` in SQLite) is significantly faster (~10x) than sorting by a `DATETIME` column, as it leverages the underlying B-tree structure of the `ROWID`.
**Action:** Always prefer sorting by `id` for sequential logs (like conversation history or trades) when the insertion order matches the chronological order.
