# Idempotency In Distributed Systems

An operation is **idempotent** if applying it multiple times produces the exact same side-effects as applying it once ($f(f(x)) = f(x)$).

## 1. Why Is Idempotency Critical?
- Network timeouts do not mean failure; the request may have succeeded just before connection dropped.
- Clients retry automatically (at-least-once delivery). Without idempotency, users get charged twice or duplicate orders get placed.

## 2. Idempotency Key Architecture
```text
Client                         Backend Server                     Database / Cache
  |                                  |                                  |
  |-- POST /payments --------------->|                                  |
  |   (Idempotency-Key: uuid-123)    |-- Check key exists ------------->|
  |                                  |<- Key not found (insert lock) ---|
  |                                  |-- Process Payment Gateway        |
  |                                  |-- Store result with key -------->|
  |<- 200 OK (Payment Confirmed) ----|                                  |
  |                                  |                                  |
  |-- POST /payments (Retry) ------->|                                  |
  |   (Idempotency-Key: uuid-123)    |-- Check key exists ------------->|
  |                                  |<- Cached Response found ---------|
  |<- 200 OK (Return Cached Resp) ---|                                  |
```

## 3. Implementation Details
- Store idempotency record in transactional store with status: `PROCESSING`, `COMPLETED`, `FAILED`.
- Enforce database unique constraint on `(user_id, idempotency_key)`.
- Set expiration TTL (e.g. 24–48 hours) to prevent unbounded key accumulation.
