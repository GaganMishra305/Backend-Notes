# Backend Engineering Interview Q&A
### Q1: What happens under the hood when a database transaction commits?
1. Changes are written to the Write-Ahead Log (WAL) and fsync'd to disk.
2. In-memory buffer pool pages are marked dirty.
3. Locks held by transaction are released.
4. Client receives commit acknowledgement. Background thread later flushes dirty pages to data files (checkpointing).
