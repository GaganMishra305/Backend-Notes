# gRPC And Protocol Buffers In Production

## 1. Performance Advantages Over REST/JSON
- **Binary Wire Format**: Protobuf encodes fields as tagged varints and length-delimited bytes; substantially smaller payload than text JSON.
- **HTTP/2 Multiplexing**: Multiple bidirectional streams over a single TCP connection, eliminating head-of-line blocking.
- **Header Compression (HPACK)**: Drastically reduces header transmission overhead across internal microservice meshes.

## 2. Four RPC Communication Patterns
1. **Unary RPC**: Single request $\to$ single response (standard client-server).
2. **Server Streaming**: Single request $\to$ stream of responses (e.g. event feed).
3. **Client Streaming**: Stream of requests $\to$ single response (e.g. file chunk upload).
4. **Bidirectional Streaming**: Streams of requests and responses interleaved independently.

## 3. Schema Evolution Guidelines
- Never change numeric field tags in `.proto`.
- Field names can change; tags cannot.
- Use `reserved` keyword when deprecating fields to prevent accidental tag reuse.
