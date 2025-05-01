# Official Upassist Cloud Python SDK

[Upassist Cloud](https://upassist.cloud/) - Monitor your applications and services with ease

## Installation

```bash
pip install upassist
```

## Configuration

Set your API key globally:

```python
import upassist

upassist.config.API_KEY = 'your-api-key'
```

## Heartbeat

The Heartbeat class provides functionality to manage and interact with heartbeat monitors.

### Basic Usage

```python
import upassist

# Create a heartbeat instance
heartbeat = upassist.Heartbeat("your-heartbeat-slug")

# Send a heartbeat event
heartbeat.event()
```

### Advanced Usage

You can also specify API credentials and version when creating a heartbeat instance:

```python
heartbeat = upassist.Heartbeat(
    heartbeat_slug="your-heartbeat-slug",
    api_key="your-api-key",  # Optional, defaults to upassist.config.API_KEY
    api_version="v1",        # Optional, defaults to upassist.config.API_VERSION
)
```

### Available Methods

- `list(q=None, page=None, per_page=None)`: List all heartbeats with optional filtering and pagination
- `detail()`: Get details of a specific heartbeat
- `pause()`: Pause a heartbeat
- `unpause()`: Resume a paused heartbeat
- `delete()`: Delete a heartbeat
- `event()`: Send a heartbeat event
- `create(heartbeat: HeartbeatCreateSchema)`: Create a new heartbeat

### Example: Managing Heartbeats

```python
# List all heartbeats
heartbeats = heartbeat.list()

# Get details of a specific heartbeat
details = heartbeat.detail()

# Pause a heartbeat
heartbeat.pause()

# Resume a heartbeat
heartbeat.unpause()

# Delete a heartbeat
heartbeat.delete()
```

### Example: Creating a Heartbeat

```python
from upassist.entities.heartbeat import Heartbeat, HeartbeatCreateSchema
from datetime import time

# Create a new heartbeat
heartbeat = Heartbeat()
new_heartbeat = heartbeat.create(
    HeartbeatCreateSchema(
        name="My Heartbeat",
        description="Monitor for my scheduled job",
        group_id="group-123",
        slug="my-heartbeat",
        fetch_interval=300,
        confirmation_period=60,
        realert_period=3600,
        alerts_on=True,
        paused=False,
        meta={"env": "prod"},
        call=False,
        send_sms=False,
        send_email=True,
        send_push_notification=False,
        maintenance_window_from=time(1, 0),  # 01:00
        maintenance_window_until=time(2, 0),  # 02:00
        maintenance_window_timezone="Europe/Belfast",
        alert_week_days=[1, 2, 3, 4, 5],
    )
)
print(new_heartbeat)
```

#### Parameters for `HeartbeatCreateSchema`

- `name` (str, required): Name of the heartbeat
- `description` (str, optional): Description
- `group_id` (str, optional): Group identifier
- `slug` (str, optional): Slug for the heartbeat
- `fetch_interval` (int, optional): Interval in seconds (default: 180)
- `confirmation_period` (int, optional): Seconds to wait before starting incident (default: 0)
- `realert_period` (int, optional): Seconds to notify users again about unresolved incident
- `alerts_on` (bool, optional): Alerts on incident messages (default: True)
- `paused` (bool, optional): Whether the heartbeat is paused (default: False)
- `meta` (dict, optional): Metadata object
- `call` (bool, optional): Enable call alerts (default: False)
- `send_sms` (bool, optional): Enable SMS alerts (default: False)
- `send_email` (bool, optional): Enable email alerts (default: True)
- `send_push_notification` (bool, optional): Enable push notifications (default: False)
- `maintenance_window_from` (time, optional): Maintenance window start time
- `maintenance_window_until` (time, optional): Maintenance window end time
- `maintenance_window_timezone` (str, optional): Timezone (default: Europe/Belfast)
- `alert_week_days` (list[int], optional): Days of the week to alert (0=Sunday)

## API Clients

The SDK provides both synchronous and asynchronous API clients:

```python
from upassist import SyncAPIClient, AsyncAPIClient

# Synchronous client
sync_client = SyncAPIClient(api_key="your-api-key")

# Asynchronous client
async_client = AsyncAPIClient(api_key="your-api-key")
```

You can specify which client to use when creating a Heartbeat instance:

```python
heartbeat = upassist.Heartbeat(
    "your-heartbeat-slug",
    api_client_cls=upassist.AsyncAPIClient  # Use async client
)
```

## Logs

The Logs entity allows you to collect and send log entries to the Upassist Cloud API.

### LogItemSchema Fields
- `dt` (datetime | None): The date and time of the log entry (ISO 8601 format).
- `host` (str | None): The host or source of the log entry.
- `message` (str | None): The log message.
- `file` (str | None): The file associated with the log entry.
- `data` (dict | None): Additional structured data for the log entry.

### Available Methods

- `collect(log_entries: list[LogItemSchema])`: Send a batch of log entries to the Upassist Cloud API

### Example: Collecting Logs

```python
from upassist.entities.logs import Logs, LogItemSchema
from datetime import datetime

# Initialize the Logs entity
logs = Logs()

# Create log entries
log_entries = [
    LogItemSchema(
        dt=datetime.utcnow(),
        host="server1",
        message="Started job",
        file="worker.py",
        data={"job_id": 123}
    ),
    LogItemSchema(
        dt=datetime.utcnow(),
        host="server1",
        message="Finished job",
        file="worker.py",
        data={"job_id": 123, "status": "success"}
    ),
]

# Send logs to Upassist Cloud
response = logs.collect(log_entries)
print(response)
```

### Advanced Usage

You can specify API credentials and version when creating a Logs instance:

```python
logs = Logs(
    api_key="your-api-key",  # Log Source API, Optional, defaults to upassist.config.API_KEY
    api_version="v1",        # Optional, defaults to upassist.config.API_VERSION
)
```

You can also use the async client for logging:

```python
from upassist import AsyncAPIClient

logs = Logs(api_client_cls=AsyncAPIClient)
```

---

For more information, visit [Upassist Cloud](https://upassist.cloud/)
