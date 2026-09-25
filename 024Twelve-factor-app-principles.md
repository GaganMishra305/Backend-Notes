# The 12-Factor App Methodology

A blueprint for building modern, scalable, cloud-native backend services.

1. **Codebase**: One codebase tracked in revision control, many deploys (dev, staging, prod).
2. **Dependencies**: Explicitly declare and isolate dependencies (e.g. `go.mod`, `package.json`, virtualenvs). Never rely on implicit system-wide packages.
3. **Config**: Store configuration in the environment variables (secrets, DB credentials, ports), never checked into git.
4. **Backing services**: Treat backing services (databases, queues, caches) as attached resources accessible via URLs/credentials.
5. **Build, release, run**: Strictly separate build stage (compile assets), release stage (code + config), and run stage (execute process).
6. **Processes**: Execute the app as one or more stateless processes. Share-nothing architecture; state persists in backing services.
7. **Port binding**: Export services via port binding (e.g., app listens on `$PORT` directly rather than running inside an external injected Apache/Tomcat).
8. **Concurrency**: Scale out via the process model (horizontal pod autoscaling / multiple worker processes).
9. **Disposability**: Maximize robustness with fast startup and graceful shutdown on `SIGTERM`.
10. **Dev/prod parity**: Keep development, staging, and production as similar as possible.
11. **Logs**: Treat logs as event streams. App writes unbuffered to stdout/stderr; execution environment handles routing.
12. **Admin processes**: Run admin/management tasks (e.g. DB migrations) as one-off processes in an identical environment.
