# Heartbeat

The Heartbeat module provides functionality to manage and interact with heartbeat monitors.

## Features

- Create and manage heartbeat monitors
- Send heartbeat events
- Configure alert settings
- Manage maintenance windows

## Examples

### Basic Usage

Create and use a heartbeat monitor

```python
import upassist

# Configure API key
upassist.config.API_KEY = 'your-api-key'

# Create a heartbeat instance
heartbeat = upassist.Heartbeat("my-heartbeat")

# Send a heartbeat event
heartbeat.event()
```

### Advanced Configuration

Create a heartbeat with custom settings

```python
from upassist.entities.heartbeat import Heartbeat, HeartbeatCreateSchema
from datetime import time

heartbeat = Heartbeat()
new_heartbeat = heartbeat.create(
    HeartbeatCreateSchema(
        name="Production Server Monitor",
        description="Monitors the production server health",
        group_id="prod-servers",
        slug="prod-server-monitor",
        fetch_interval=300,  # Check every 5 minutes
        confirmation_period=60,  # Wait 1 minute before alerting
        realert_period=3600,  # Re-alert every hour
        alerts_on=True,
        maintenance_window_from=time(2, 0),  # 02:00
        maintenance_window_until=time(3, 0),  # 03:00
        maintenance_window_timezone="UTC",
        alert_week_days=[1, 2, 3, 4, 5]  # Monday to Friday
    )
)
```

### Managing Heartbeats

List, pause, and manage heartbeats

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

## API Reference

::: upassist.entities.heartbeat

---

For more information and to get started with monitoring your applications, visit [Upassist Cloud](https://upassist.cloud/)