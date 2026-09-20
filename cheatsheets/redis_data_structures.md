# Redis Data Structures Cheat Sheet
- **Strings**: Caching, counters (`INCR`), bitfields.
- **Lists**: Producer-consumer queues (`LPUSH`, `RPOP`, `BRPOP`).
- **Sets**: Unique tags, mutual friends (`SINTER`, `SUNION`).
- **Sorted Sets (ZSet)**: Leaderboards, sliding window rate limits (`ZADD`, `ZRANGEBYSCORE`).
- **Hashes**: Object representations (`HSET`, `HGETALL`).
- **Streams**: Append-only event streams with consumer groups (`XADD`, `XREADGROUP`).
- **HyperLogLog**: Approximate cardinality counting in 12KB (`PFADD`, `PFCOUNT`).
