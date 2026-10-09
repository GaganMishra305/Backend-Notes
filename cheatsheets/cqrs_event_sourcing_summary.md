# CQRS and Event Sourcing Summary
- **CQRS (Command Query Responsibility Segregation)**:
  - Write Model (Command): Validates domain invariants, writes to DB.
  - Read Model (Query): Denormalized projections optimized for specific view queries (Elasticsearch/MongoDB/Postgres views).
- **Event Sourcing**:
  - State is not stored directly; state is reconstructed by replaying immutable domain events.
  - Built-in audit log and time-travel debugging.
