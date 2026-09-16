# SQL Indexing Rules of Thumb
1. **Leftmost Prefix Rule**: A composite index `(A, B, C)` can serve queries on `(A)`, `(A, B)`, and `(A, B, C)`, but NOT `(B, C)` alone.
2. **Cardinality First**: Place highest cardinality (selectivity) columns first in composite index.
3. **Avoid Functions On Indexed Columns**: `WHERE YEAR(created_at) = 2026` invalidates index; use `WHERE created_at >= '2026-01-01' AND created_at < '2027-01-01'`.
4. **Covering Indexes**: Include all queried columns (`INCLUDE` or composite) to satisfy query entirely from B-Tree leaf nodes without heap lookups.
