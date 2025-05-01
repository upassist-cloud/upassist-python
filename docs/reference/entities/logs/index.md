# Logs

The Logs module allows you to collect and send log entries to the Upassist Cloud API.

## Features

- Send log entries in batches
- Structured log data with timestamps
- Custom metadata support
- Type-safe log entries with Pydantic

## Examples

### Basic Usage

Send log entries to Upassist Cloud

```python
from upassist.entities.logs import Logs, LogItemSchema
from datetime import datetime

logs = Logs()
log_entries = [
    LogItemSchema(
        dt=datetime.utcnow(),
        host="server1",
        message="Application started",
        file="app.py",
        data={"version": "1.0.0"}
    ),
    LogItemSchema(
        dt=datetime.utcnow(),
        host="server1",
        message="Database connection established",
        file="db.py",
        data={"connection_id": "123"}
    )
]
response = logs.collect(log_entries)
```

### Advanced Usage

Send logs with custom configuration

```python
from upassist.entities.logs import Logs, LogItemSchema
from datetime import datetime
from upassist import AsyncAPIClient

# Create logs instance with custom API key
logs = Logs(api_key="your-api-key")

# Use async client for high-performance logging
logs = Logs(api_client_cls=AsyncAPIClient)

# Send logs with custom metadata
log_entries = [
    LogItemSchema(
        dt=datetime.utcnow(),
        host="prod-server-1",
        message="High CPU usage detected",
        file="monitor.py",
        data={
            "cpu_usage": 95.5,
            "memory_usage": 80.2,
            "process_count": 150,
            "environment": "production"
        }
    )
]
response = logs.collect(log_entries)
```

## API Reference

::: upassist.entities.logs

---

For more information and to get started with monitoring your applications, visit [Upassist Cloud](https://upassist.cloud/)