# Testing And Code Quality In Production Backends

## 1. The Testing Pyramid
```text
        /  E2E  \         Slowest, most brittle, highest operational cost
       / Integration \     Tests interaction with DB, Redis, Message Queues
      /     Unit     \    Fastest, isolated business logic, high coverage
```

## 2. Test Doubles: Mocks vs Stubs vs Fakes
- **Dummy**: Objects passed around but never actually used (e.g. filling parameter lists).
- **Stub**: Provides predetermined canned answers to calls during the test.
- **Spy**: A stub that also records information about how it was called (e.g. number of invocations).
- **Mock**: Objects pre-programmed with expectations which form a specification of the calls they are expected to receive.
- **Fake**: Working implementation, but with a shortcut unsuitable for production (e.g., in-memory SQLite / fake repository).

## 3. Integration Testing with Testcontainers
- Running real lightweight Docker containers (PostgreSQL, Redis, RabbitMQ) dynamically during test lifecycle.
- Eliminates divergence between in-memory mock behavior and actual SQL dialect/locking semantics.

```go
// Example pattern: spin up ephemeral Postgres container
postgresContainer, err := postgres.RunContainer(ctx,
    testcontainers.WithImage("postgres:16-alpine"),
    postgres.WithDatabase("testdb"),
)
```
