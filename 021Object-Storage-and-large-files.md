# Object Storage And Large File Handling

## 1. Why Not Store Files In Relational DBs?
- DBs are optimized for structured rows, indexing, and transactional ACID guarantees (WAL logs).
- Large BLOBs bloat database memory, cache pool buffers (e.g. InnoDB buffer pool), and cause heavy I/O saturation during sequential table scans.
- Backups and point-in-time recovery become significantly slower.

## 2. Object Storage Architecture (S3 / GCS / MinIO)
- **Key-Value Paradigm**: Bucket + Key (flat namespace).
- **Metadata separation**: Object payload is stored across distributed erasure-coded storage nodes; metadata is maintained in a distributed catalog.
- **Immutability**: Objects are written once and replaced, never partially modified in-place.

## 3. Direct Uploads via Presigned URLs
```text
Client                  App Server                  Object Store (S3)
  |                         |                              |
  |-- 1. Request Upload --->|                              |
  |   (file meta, auth)     |-- 2. Generate Presigned URL->| (HMAC sign)
  |                         |<-- 3. Return Presigned URL --|
  |<- 4. Presigned PUT URL -|                              |
  |                                                        |
  |---------------- 5. Direct HTTP PUT ------------------->|
  |<--------------- 6. 200 OK (ETag) ----------------------|
```
- Offloads heavy file transfer I/O from backend application servers.
- Backend verifies authorization, generates a temporary signed URL with strict TTL (e.g. 15 minutes) and HTTP headers restriction (e.g. Content-Type, Content-Length-Range).

## 4. Multipart Uploads for Large Files (>100MB)
1. **InitiateMultipartUpload**: Backend requests upload ID from S3.
2. **Chunking**: Client splits file into 5MB–50MB chunks.
3. **Parallel Upload**: Client uploads chunks concurrently with part numbers and presigned URLs.
4. **CompleteMultipartUpload**: Client sends part numbers + ETags to S3; S3 stitches parts into a single object.
5. **Fault Tolerance**: Failed parts can be retried independently without restarting the entire upload.
