# DevOps Essentials For Backend Engineers

## 1. Multi-Stage Dockerfile Optimization
- Minimize image footprint to reduce attack surface and build/push latency.
- Separate compilation environment from lean runtime environment.

```dockerfile
# Build Stage
FROM golang:1.22-alpine AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-s -w" -o server ./cmd/server

# Production Runtime Stage
FROM alpine:3.19
RUN apk --no-cache add ca-certificates tzdata
WORKDIR /app
COPY --from=builder /app/server .
USER 10001:10001
EXPOSE 8080
ENTRYPOINT ["./server"]
```

## 2. CI/CD Pipeline Stages
1. **Static Analysis**: Linting (`golangci-lint`, `eslint`), security scan (`trivy`).
2. **Automated Testing**: Unit tests, integration tests against isolated services.
3. **Container Build & Attestation**: Multi-arch build, sign container with Cosign.
4. **Deploy**: Push updated image tag to GitOps repository.
