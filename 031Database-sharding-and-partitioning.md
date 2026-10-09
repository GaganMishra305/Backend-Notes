# Database Sharding And Horizontal Partitioning

## 1. Sharding Strategies
- **Range-Based Sharding**: Partition by numerical range or alphabetical chunks (e.g. User IDs 1–1M on Node 1, 1M–2M on Node 2).
  - *Risk*: Hotspots on latest range for monotonically increasing IDs.
- **Hash-Based Sharding**: Partition by hash of shard key: `node = hash(user_id) % N`.
  - Uniform distribution, but adding new node ($N+1$) requires rehashing all keys.
- **Consistent Hashing**: Keys and nodes mapped onto virtual ring ($0$ to $2^{32}-1$). Adding node only rebalances $K/N$ keys.

## 2. Distributed Query Challenges
- **Cross-Shard Joins**: Extreme latency overhead; require application-side joins or denormalization.
- **Distributed Transactions**: Requires 2-Phase Commit (2PC) which introduces blocking and coordinator vulnerability.
- **Global Secondary Indexes**: Must query all shards (scatter-gather) unless secondary index is separately sharded.
