# Modular Monolith vs Microservices Architecture

## 1. The Real Cost of Microservices
- Distributed system overhead: network latency, network failure modes, serializing/deserializing payloads.
- Distributed transactions and eventual consistency complexities.
- Operational burden: service discovery, distributed tracing, independent CI/CD pipelines, security perimeters.

## 2. What Is A Modular Monolith?
- Single deployable artifact with strictly enforced internal module boundaries.
- Modules communicate via in-memory interface contracts rather than network calls.
- Independent database schemas or namespaces per module within a single managed database.

## 3. When To Split Into Microservices
1. **Independent Scaling Dimensions**: One component requires 100x CPU/memory resources (e.g. video transcode worker vs CRUD API).
2. **Organizational Scale (Conway's Law)**: Multiple large engineering teams stepping on each other's release cycles.
3. **Different Technology Requirements**: Polyglot requirements (e.g. Python machine learning pipeline integrated with Go API).
