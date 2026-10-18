# Circuit Breakers And System Resilience Patterns

## 1. Cascading Failures
- If downstream dependency Service B slows down or times out, upstream Service A exhausts thread pool and connection buffers waiting for replies.
- Soon Service A crashes, affecting its upstream callers, bringing down the entire system.

## 2. Circuit Breaker State Machine
```text
         +-------------------+
         |                   |
         v                   | (Success rate reaches threshold)
    [ CLOSED ]               |
         |                   |
         | (Error threshold  |
         |  exceeded)        |
         v                   |
     [ OPEN ] ------------> [ HALF-OPEN ]
        |       (Probe TTL     ^
        |        expires)      |
        +----------------------+
```
- **Closed**: Requests pass through normally. Track failure rate.
- **Open**: Short-circuits immediately; returns fallback or error without calling downstream dependency.
- **Half-Open**: Allows limited probe requests through to test if dependency has recovered.

## 3. Bulkhead Pattern & Load Shedding
- **Bulkhead**: Isolate resources (thread pools, connection pools) per downstream service so exhaustion in one integration cannot starve others.
- **Load Shedding**: When queue latency exceeds threshold, immediately reject lower-priority traffic (429/503) to preserve throughput for critical user flows.
