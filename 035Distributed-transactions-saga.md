# The Transactional Outbox Pattern

## 1. The Dual-Write Problem
```text
Application ---> Write to Database (Postgres)  [SUCCESS]
            ---> Publish Event to Broker (Kafka) [NETWORK TIMEOUT / CRASH]
```
- If the app crashes between DB commit and message publish, the event is lost forever.
- If we publish first, the DB write might fail, leading to phantom events downstream.

## 2. Transactional Outbox Solution
```text
[ Application ]
      |
      |-- Single Atomic DB Transaction
      |-------------------------------------> [ Orders Table ]
      |-------------------------------------> [ Outbox Table ]
                                                    |
                                      (Debezium CDC / Polling Publisher)
                                                    |
                                                    v
                                             [ Kafka Topic ]
```
1. Write business entity and outbox message row inside the **same local database transaction**.
2. A separate relay process (CDC via Debezium or tailing WAL) reads unpublished outbox rows and produces them to Kafka.
3. Guarantees **At-Least-Once Delivery** without distributed two-phase commit overhead.
