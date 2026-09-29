# Linux Server Performance and Automated Monitoring Suite

A production-style Linux operations and observability suite designed to automate L1 system health triage, audit file descriptor allocations, and monitor node telemetry via Prometheus and Grafana.

## Architecture & Features
- **L1 Health Automation**: Python and Bash scripts scheduled to audit CPU, memory, disk, and socket/file-descriptor allocations.
- **OS Resource Limits**: Configured file descriptor limits from 1,024 to 65,535 via Docker container configs to avoid socket starvation.
- **Observability Stack**: Prometheus metrics collection with Node Exporter and Grafana dashboard visualization.
- **Log Hygiene**: Automated shell routines for log retention and storage reclamation.

## Project Structure
```free
.
+-- configs/
¦   +-- prometheus.yml
+-- scripts/
¦   +-- health_check.py
?   +-- log_cleanup.sh
+-- docker-compose.yml
+-- README.md
p``

## Quick Start
1. Start the stack:
   ```bash
   docker compose up -d
   ```
2. Access Prometheus at `http://localhost:9090`
3. Access Grafana at `http://localhost:3000` (Default: `admin`/`admin`)
4. Run manual L1 health triage:
   ```bash
   python3 scripts/health_check.py
   ```

