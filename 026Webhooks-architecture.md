# Webhook Architecture: Delivery, Security, And Retries

## 1. Asynchronous Delivery Pipeline
- Never send HTTP webhooks synchronously in the main request thread.
- Enqueue webhook payload to a dedicated message broker (RabbitMQ/SQS).
- Dedicated worker pools execute HTTP POST requests with short timeouts (e.g. 5s).

## 2. Security: HMAC Signatures
- Protect subscribers against spoofing and tampering.
- Compute SHA-256 HMAC of raw payload body with subscriber's shared secret.
- Send signature in header `X-Signature-SHA256: t=1695982800,v1=abcdef12345...`.
- Include timestamp `t` to defend against replay attacks.

## 3. Exponential Backoff & Dead Letter Queue (DLQ)
- Subscriber endpoints can experience outages or rate limits.
- Retry with jittered exponential backoff:
  - Attempt 1: immediate
  - Attempt 2: 15 seconds
  - Attempt 3: 1 minute
  - Attempt 4: 15 minutes
  - Attempt 5: 1 hour
- After exhaustion (e.g. 5 attempts), route message to DLQ and trigger alert.
