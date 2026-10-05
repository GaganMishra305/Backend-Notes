# JWT vs Server-Side Sessions Comparison
- **JWT (Stateless)**:
  - Stored on client (HttpOnly cookie or Auth header).
  - Scalable horizontally without shared session store.
  - *Drawback*: Cannot be easily revoked before expiration without maintaining a token blocklist in Redis.
- **Server-Side Sessions (Stateful)**:
  - Server maintains session in Redis/Postgres; client holds session ID cookie.
  - Instant revocation on logout or password change.
  - Requires centralized fast session store.
