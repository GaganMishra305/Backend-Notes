# Rate Limiting And Throttling Algorithms

## 1. Algorithm Comparison
1. **Token Bucket**:
   - Tokens added at constant rate up to bucket capacity $B$.
   - Allows bursts of up to $B$ requests while enforcing long-term average rate.
2. **Leaky Bucket**:
   - Requests enter queue and are processed at constant outflow rate.
   - Smooths out bursts into steady traffic.
3. **Fixed Window Counter**:
   - Increments counter per discrete time window (e.g., minute).
   - *Flaw*: Burst of $2 \times$ limit at window boundary.
4. **Sliding Window Log**:
   - Stores sorted set of timestamps.
   - Exact precision, but high memory footprint ($O(N)$ stored timestamps per user).
5. **Sliding Window Counter**:
   - Approximates rate: `count = current_window + previous_window * (1 - overlap_fraction)`.
   - Low memory ($O(1)$) and high accuracy.

## 2. Redis Lua Script Implementation (Atomic Sliding Window)
```lua
local key = KEYS[1]
local now = tonumber(ARGV[1])
local window = tonumber(ARGV[2])
local limit = tonumber(ARGV[3])

-- Clear expired entries
redis.call('ZREMRANGEBYSCORE', key, 0, now - window)

local count = redis.call('ZCARD', key)
if count < limit then
    redis.call('ZADD', key, now, now)
    redis.call('EXPIRE', key, math.ceil(window / 1000))
    return 1 -- Allowed
else
    return 0 -- Rejected (429 Too Many Requests)
end
```
