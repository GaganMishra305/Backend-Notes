# Caching
Keeping a subset of some data depending on the {frequency of usage, probability of usage, ...} in a location which is faster to access.
* Very important in high-performance applications.
* CDNs are a caching mechanism that is used by global companies for sending media/static-files across the web with ease and speed.
    - CDNs optimize their working by using ml-predictions to pre-fill the CDN data

## 1. Levels of Caching-
### i. Network-caching
1. **CDNs**: content is stored and served using edge-compute (server closest to the client), thus minimizing the latency and compute.
    * POP (point of presence) [collection of a number of edge servers]: the client sends the request to  the nearest POP
    * TTL : uses TTL for avoidind serving old-content
2. **DNS**:the dns-query is sent to a recursive-resolver which is provided by the ISP. The recursive-resolver[goes deep and deep till it resolves the domain] checks in-
    * Local-cache
    * Root-servers (refs for top-level domain; .com, .co. in)
    * TLD (top-level-domain)
    * Authoritative name-server
    ```
    local-cache(DHS) ->  browser(DNS cache) -> Resolver(ISP)
    ```
---
### ii. Hardware-caching
![hardware-cache](/public/hardware-cache.png)
* redis etc. below are in-memory(RAM) based caches; caching done thru software is just abstracted hardware based caching
---
### iii. Software-caching
* Redis, memcache, elasticache  ---> they're in-memory, key-value based, no-sql databases
* They use the RAM-and provide FAST-caching
* **Caching Strategies**:
    1. Lazy caching: we dont proactively cache; we cache when the client requests
    2. Write through caching: every time there is a change in the db(POST, PUT, PATCH) we cache it; (+it provides updated data) (-write request has more overhead)
* **Eviction**: these are strategies to remove extra data from cached
    1. _No-eviction_: we dont evict any data; we handle the error [dumb ik]
    2. _LRU_: we evict the least-recently used cache
    3. _LFU_: we evict the least-frequently used
    4. _TTL_: which key has the lowest ttl

* **Some example use cases of caching in backend:**
    + DB-queries
    + User-profile data
    + session-info
    + api-caching from external resource
    + rate-limiting mechanisms [middleware]
    + MOSTLY READ-HEAVY AND WRITE-LOW OPERATIONS