# HTTP Status Codes Quick Reference
## 2xx Success
- `200 OK`: Standard successful response.
- `201 Created`: Resource successfully created (includes `Location` header).
- `204 No Content`: Request succeeded but no response body returned (e.g. DELETE).

## 4xx Client Errors
- `400 Bad Request`: Malformed syntax or request validation failure.
- `401 Unauthorized`: Authentication required or token invalid.
- `403 Forbidden`: Authenticated, but lacks necessary role/permission.
- `404 Not Found`: Target resource does not exist.
- `409 Conflict`: Request conflicts with current server state (e.g. duplicate key).
- `422 Unprocessable Entity`: Semantic validation failure.
- `429 Too Many Requests`: Rate limit exceeded.

## 5xx Server Errors
- `500 Internal Server Error`: Unhandled application exception.
- `502 Bad Gateway`: Upstream reverse proxy received invalid response.
- `503 Service Unavailable`: Server overloaded or undergoing maintenance.
- `504 Gateway Timeout`: Upstream proxy timed out waiting for service.
