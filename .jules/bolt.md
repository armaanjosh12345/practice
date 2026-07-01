## 2025-05-15 - SQLite Primary Key Sorting Optimization
**Learning:** Sorting by `INTEGER PRIMARY KEY` in SQLite is significantly faster (up to 50x in this case) than sorting by a `DATETIME` column, because the PK is automatically indexed and serves as the physical storage order (rowid alias).
**Action:** Always prefer sorting by `id DESC` for time-sequential logs or history tables in SQLite instead of a `timestamp` column.
