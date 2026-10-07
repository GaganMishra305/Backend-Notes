# Message Brokers: Apache Kafka vs RabbitMQ

## 1. Architectural Model
- **RabbitMQ (Smart Broker, Dumb Consumer)**:
  - AMQP standard; routing via exchanges (direct, topic, fanout, headers) into queues.
  - Messages deleted from queue once acknowledged by consumers.
  - Excellent for fine-grained routing, task queuing, RPCs.
- **Kafka (Dumb Broker, Smart Consumer)**:
  - Distributed append-only commit log partitioned across brokers.
  - Messages retained based on time/size policy, independent of consumer state.
  - Consumers track their own read progress via offsets (`__consumer_offsets`).
  - High sequential throughput (millions msg/sec), event sourcing, stream processing.

## 2. Consumer Groups & Partitioning In Kafka
```text
Topic: orders (3 Partitions)
Partition 0 ---------> Consumer 1 (Consumer Group A)
Partition 1 ---------> Consumer 2 (Consumer Group A)
Partition 2 ---------> Consumer 3 (Consumer Group A)
```
- A partition is consumed by exactly one consumer within a consumer group at any time.
- Scaling concurrency is bounded by partition count.
