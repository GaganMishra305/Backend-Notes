# Distributed Caching Patterns And Pitfalls

## 1. Caching Strategies
- **Cache-Aside (Lazy Loading)**:
  - App reads from cache; if miss, reads from DB and writes to cache.
  - Good for read-heavy workloads; cache only stores requested data.
- **Write-Through**:
  - App writes to cache; cache writes synchronously to DB.
  - Higher write latency, but ensures cache freshness.
- **Write-Behind (Write-Back)**:
  - App writes to cache; cache acknowledges immediately and batches asynchronous DB writes.
  - High performance; risk of data loss on cache instance failure.

## 2. Common Production Pitfalls
- **Cache Stampede (Thundering Herd)**:
  - Key expires; thousands of concurrent requests simultaneously hit DB to recompute.
  - *Fix*: Mutex locking with single-flight pattern, or probabilistic early expiration (XFetch algorithm).
- **Cache Penetration**:
  - Continuous requests for keys that do not exist in DB, bypassing cache.
  - *Fix*: Cache negative/null results with short TTL, or use Bloom Filters before cache query.
- **Cache Avalanche**:
  - Thousands of keys configured with identical TTL expire at the exact same second.
  - *Fix*: Add random jitter to key expiration times (`TTL = base_ttl + rand(0, 300)`).
