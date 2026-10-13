# Zero-Downtime Deployment Strategies
- **Rolling Update**: Replaces old instances with new instances incrementally (Kubernetes default).
- **Blue/Green Deployment**: Two identical environments. Switch router/DNS from Blue to Green instantly. Instant rollback by switching back.
- **Canary Deployment**: Route 5% of traffic to new version. Monitor error rate / latency SLIs before rolling out to 100%.
