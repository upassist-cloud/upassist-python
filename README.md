# Upassist Python SDK & CLI

Official Python client library and CLI for the [Upassist](https://upassist.cloud) Monitoring, Uptime, Cron Heartbeats, Error Tracking & Observability Platform.

[![PyPI version](https://img.shields.io/pypi/v/upassist.svg)](https://pypi.org/project/upassist/)
[![Python versions](https://img.shields.io/pypi/pyversions/upassist.svg)](https://pypi.org/project/upassist/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

- **Complete API Coverage**: 100% of platform resources (Monitors, Heartbeats, Incidents, Maintenance, Error Apps, Status Pages, Dashboards, Members, API Keys, Logs, Metrics).
- **Synchronous & Asynchronous**: First-class `Upassist` (sync) and `AsyncUpassist` (asyncio) clients with automatic connection pooling and retry transports.
- **Ergonomic Facades**: High-level, pythonic interfaces (`client.monitors`, `client.heartbeats`, etc.) with built-in pagination iterators (`.iter()`).
- **High-Throughput Ingest**: Zero-latency helpers for cron heartbeats, structured log streaming, and metric collection.
- **Bundled CLI**: Full-featured `upassist` command-line tool for bash scripts, crontab, and CI/CD pipelines.

---

## Table of Contents

- [Installation](#installation)
- [Authentication](#authentication)
- [CLI Quickstart](#cli-quickstart)
- [Practical Python Examples](#practical-python-examples)
  - [1. Uptime Monitoring & Health Checks](#1-uptime-monitoring--health-checks)
  - [2. Cron Job & Background Worker Monitoring (Heartbeats)](#2-cron-job--background-worker-monitoring-heartbeats)
  - [3. CI/CD Deployment: Alert Silencing via Maintenance Windows](#3-cicd-deployment-alert-silencing-via-maintenance-windows)
  - [4. Automated Incident Management](#4-automated-incident-management)
  - [5. Sentry-Compatible Error Apps & Issue Tracking](#5-sentry-compatible-error-apps--issue-tracking)
  - [6. High-Throughput Log & Metric Ingestion](#6-high-throughput-log--metric-ingestion)
  - [7. Team Members & API Key Provisioning](#7-team-members--api-key-provisioning)
  - [8. Async / Asyncio Usage (FastAPI, Starlette, Quart)](#8-async--asyncio-usage-fastapi-starlette-quart)
- [Error Handling](#error-handling)
- [License](#license)

---

## Installation

```bash
pip install upassist
# or with uv
uv add upassist
# or with poetry
poetry add upassist
```

---

## Authentication

Obtain your Project API Key from your [Upassist Dashboard](https://upassist.cloud) (*Settings -> API Keys*).

Pass your API key directly or export `UPASSIST_API_KEY`:

```bash
export UPASSIST_API_KEY="up_live_your_secret_api_key_here"
```

```python
from upassist import Upassist

# If UPASSIST_API_KEY is exported, api_key argument is optional:
client = Upassist(api_key="up_live_your_secret_api_key_here")
```

---

## CLI Quickstart

The package installs the `upassist` executable:

```bash
export UPASSIST_API_KEY="up_live_your_secret_api_key_here"

# 1. Verify credentials and project quota
upassist whoami

# 2. List monitors and check their status
upassist monitors list
upassist monitors get --id 12345

# 3. Ping cron heartbeats in crontab or bash
upassist heartbeats ping my-backup-job --status up --duration-ms 420 --msg "Backup successful"

# 4. View and acknowledge incidents
upassist incidents list
upassist incidents ack --id 98765

# 5. Create a deploy-time maintenance window
upassist maintenance create --name "v2.4.0 Deploy" --start "2026-11-21T21:00:00Z" --end "2026-11-21T21:30:00Z"
```

---

## Practical Python Examples

### 1. Uptime Monitoring & Health Checks

Manage website and API endpoint monitors programmatically:

```python
from upassist import Upassist

client = Upassist()

# 1. Create a new HTTP uptime monitor
new_monitor = client.monitors.create({
    "name": "Production Payment Gateway",
    "url": "https://api.example.com/health",
    "monitor_type": "status",
    "interval": 60,           # Check every 60 seconds
    "timeout": 10,            # 10s timeout
    "expected_status_code": 200,
    "send_email": True,
    "call": False,
})
print(f"Created monitor ID: {new_monitor.id}")

# 2. Iterate through all monitors across pages
for monitor in client.monitors.iter(per_page=50):
    print(f"[{monitor.status.upper()}] {monitor.name} -> {monitor.url}")

# 3. Temporarily pause checks during maintenance
client.monitors.pause(new_monitor.id)

# 4. Resume checks
client.monitors.unpause(new_monitor.id)
```

---

### 2. Cron Job & Background Worker Monitoring (Heartbeats)

Never let a silent background task failure go unnoticed. Monitor Celery tasks, Kubernetes CronJobs, and system crontabs:

```python
import time
from upassist import Upassist

client = Upassist()

def run_nightly_billing():
    heartbeat_slug = "nightly-billing-cron"
    start_time = time.time()
    
    try:
        # Perform your business logic...
        print("Billing processing...")
        time.sleep(1.5)
        
        # Report success with duration
        duration_ms = int((time.time() - start_time) * 1000)
        client.heartbeats.ping(
            token=heartbeat_slug,
            status="up",
            duration_ms=duration_ms,
            message="Processed 14,205 invoices without error",
        )
    except Exception as exc:
        # Report failure immediately to trigger on-call alerts
        duration_ms = int((time.time() - start_time) * 1000)
        client.heartbeats.ping(
            token=heartbeat_slug,
            status="down",
            duration_ms=duration_ms,
            message=f"Job crashed: {exc}",
        )
        raise

run_nightly_billing()
```

#### Reusable Context Manager / Decorator:

```python
import contextlib
import time
from upassist import Upassist

client = Upassist()

@contextlib.contextmanager
def monitor_cron(token: str):
    start = time.time()
    try:
        yield
        duration = int((time.time() - start) * 1000)
        client.heartbeats.ping(token=token, status="up", duration_ms=duration)
    except Exception as exc:
        duration = int((time.time() - start) * 1000)
        client.heartbeats.ping(token=token, status="down", duration_ms=duration, message=str(exc))
        raise

# Usage:
with monitor_cron("database-sync-worker"):
    # Critical work here
    pass
```

---

### 3. CI/CD Deployment: Alert Silencing via Maintenance Windows

Integrate into deploy scripts (Fabric, Ansible, GitHub Actions, GitLab CI) to silence alerts while services restart:

```python
from datetime import datetime, timezone, timedelta
from upassist import Upassist

client = Upassist()

# 1. Schedule a 15-minute maintenance window starting right now
now = datetime.now(timezone.utc)
window_start = now.isoformat()
window_end = (now + timedelta(minutes=15)).isoformat()

window = client.maintenance.create({
    "name": "Production Release v3.12.0",
    "description": "Database migrations and rolling service restart",
    "started_at": window_start,
    "finished_at": window_end,
    "timezone": "UTC",
    "resources": [
        # Silence all monitors or specific ones:
        {"public_name": "API Service", "object_id": "101", "resource_type": "monitor"},
        {"public_name": "Web Frontend", "object_id": "102", "resource_type": "monitor"},
    ],
})

print(f"Maintenance window #{window.id} active until {window_end}")

# 2. Deploy your code here...

# 3. If finished earlier, complete/delete window immediately:
client.maintenance.delete(window.id)
print("Maintenance window ended, alerting resumed.")
```

---

### 4. Automated Incident Management

Inspect active outages and programmatically acknowledge or resolve them:

```python
from upassist import Upassist

client = Upassist()

# Fetch open incidents
incidents = client.incidents.list(page=1, per_page=20)
for incident in incidents.items:
    print(f"Incident #{incident.id}: {incident.cause} (State: {incident.state})")
    
    # Acknowledge incident to stop escalation escalation alerts
    if incident.state == "started":
        client.incidents.ack(incident.id)
        print(f" -> Acknowledged #{incident.id}")

    # Auto-resolve incident after automated remediation
    # client.incidents.resolve(incident.id)
```

---

### 5. Sentry-Compatible Error Apps & Issue Tracking

Upassist includes a built-in Sentry-compatible error collection and crash reporting service. You can audit, query, and resolve error issues:

```python
from upassist import Upassist

client = Upassist()

# 1. List error tracking apps
apps = client.error_apps.list()
for app in apps:
    print(f"App: {app.name} | Sentry DSN: {app.sentry_dsn}")

# 2. Inspect active issues for an app
if apps:
    app_id = apps[0].id
    issues = client.error_apps.issues.list(app_id=app_id)
    for issue in issues.items:
        print(f"Issue: {issue.title} (Seen {issue.events_count} times)")
        
        # Resolve issue after deploying fix:
        client.error_apps.issues.resolve(app_id=app_id, issue_id=issue.id)
```

---

### 6. High-Throughput Log & Metric Ingestion

Push structured logs and custom metrics directly to Upassist telemetry ingestion servers:

```python
from datetime import datetime, timezone
from upassist import Upassist

client = Upassist()

# Ingest structured application logs
client.logs.collect(
    service="checkout-service",
    logs=[
        {
            "level": "INFO",
            "message": "Payment intent succeeded",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "context": {
                "customer_id": "cust_9921",
                "amount": 149.99,
                "currency": "USD",
            },
        },
    ],
)

# Ingest custom timeseries metrics
client.metrics.collect(
    metrics=[
        {
            "name": "cart_checkout_seconds",
            "value": 1.24,
            "type": "gauge",
            "labels": {"region": "us-east-1", "env": "prod"},
        },
        {
            "name": "active_websocket_connections",
            "value": 450,
            "type": "gauge",
        },
    ]
)
```

---

### 7. Team Members & API Key Provisioning

Automate user onboarding and machine-to-machine API key rotation:

```python
from upassist import Upassist

client = Upassist()

# 1. List current project team members
members = client.members.list()
for m in members:
    print(f"Member: {m.email} (Role: {m.role})")

# 2. Invite a new team member
client.invitations.create({
    "email": "devops@company.com",
    "role": "admin",
})

# 3. Create a scoped API key for CI/CD runners
key = client.api_keys.create({
    "name": "GitHub Actions Deployment Key",
    "scopes": [
        "monitor:read",
        "maintenance:write",
        "heartbeat:write",
    ],
})
print(f"Generated Key: {key.token}")
```

---

### 8. Async / Asyncio Usage (FastAPI, Starlette, Quart)

Use `AsyncUpassist` with `async/await` for high-concurrency applications:

```python
import asyncio
from upassist import AsyncUpassist

async def main():
    async with AsyncUpassist(api_key="up_live_secret") as client:
        # Run queries concurrently
        monitors_task = client.monitors.list()
        heartbeats_task = client.heartbeats.list()
        incidents_task = client.incidents.list()
        
        monitors, heartbeats, incidents = await asyncio.gather(
            monitors_task, heartbeats_task, incidents_task
        )
        
        print(f"Monitors: {len(monitors.items)}")
        print(f"Heartbeats: {len(heartbeats.items)}")
        print(f"Incidents: {len(incidents.items)}")

if __name__ == "__main__":
    asyncio.run(main())
```

---

## Error Handling

All management API failures raise `APIError` with structured code, human-readable message, and request ID for debugging:

```python
from upassist import Upassist, APIError

client = Upassist()

try:
    client.monitors.get(monitor_id="non-existent-id")
except APIError as err:
    print(f"Code: {err.code}")             # e.g., 'not_found'
    print(f"Message: {err.message}")       # e.g., 'Monitor with id ... was not found'
    print(f"Request ID: {err.request_id}") # e.g., 'req_01hqb7...'
```

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
