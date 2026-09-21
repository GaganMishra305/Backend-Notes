# Realtime Backend Systems

## 1. Protocol Comparison
| Feature | Short Polling | Long Polling | SSE (Server-Sent Events) | WebSockets |
| :--- | :--- | :--- | :--- | :--- |
| **Transport** | Repeated HTTP GET | Suspended HTTP GET | Persistent HTTP stream | Full-duplex TCP framing |
| **Direction** | Client -> Server | Client -> Server | Server -> Client | Bidirectional |
| **Overhead** | High (headers every req) | Moderate (headers on reconn) | Low (single HTTP stream) | Minimal (2-byte framing header) |
| **Reconnection** | Native | Manual in client | Native (browser handles it) | Handled by application layer |
| **Use Cases** | Simple dashboard check | Legacy chat fallback | Stock tickers, notifications | Collaborative editing, gaming |

## 2. Horizontal Scaling With Redis Pub/Sub Backplane
- WebSocket connections are stateful; clients stay connected to specific server instances.
- When User A (on Server 1) sends a message to User B (connected to Server 2):
  1. Server 1 publishes the event to Redis channel `user:user_B_id`.
  2. All server instances subscribe to user channels or cluster channels.
  3. Server 2 receives the Redis pub/sub event and pushes it over the local WebSocket to User B.

```text
Client A (Server 1) ---> HTTP/WS ---> Server 1
                                         |
                                   Redis Pub/Sub
                                         |
Client B (Server 2) <--- HTTP/WS <--- Server 2
```

## 3. Heartbeats and Connection Health
- Keepalive ping/pong frames every 30–60s prevent intermediate NAT routers and load balancers from killing idle TCP sockets.
- Handle zombie connections by setting strict read deadlines.
