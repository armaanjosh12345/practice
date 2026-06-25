## 2025-05-15 - SQLite Primary Key Sorting Optimization
**Learning:** Sorting by an INTEGER PRIMARY KEY (id) in SQLite is significantly faster (~40x-500x) than sorting by a DATETIME column, especially as the dataset grows. Since AUTOINCREMENT IDs generally reflect insertion order, they can be used as a high-performance proxy for chronological sorting.
**Action:** Always prefer ORDER BY id DESC/ASC over ORDER BY timestamp_column for large tables where ID preserves order.

## 2025-05-15 - Redundant System and Import Overhead
**Learning:** Frequent calls to platform.system() or inline imports (like import re) inside hot methods add unnecessary micro-latency. While small, these add up in high-frequency request environments like a FastAPI chat loop.
**Action:** Move imports to module level and cache static system information in module-level constants.
