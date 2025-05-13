"""Generate API reference documentation."""

import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Create reference directory if it doesn't exist
reference_dir = project_root / "docs" / "reference"
reference_dir.mkdir(parents=True, exist_ok=True)

# Create an index file for the reference section
index_path = reference_dir / "index.md"
with open(index_path, "w") as fd:
    fd.write("# API Reference\n\n")
    fd.write(
        "This section contains the complete API reference for the Upassist Python SDK.\n\n"
    )
    fd.write(
        "Visit [Upassist Cloud](https://upassist.cloud/) to get started with "
        "monitoring your applications and services.\n\n"
    )
    fd.write("## Modules\n\n")
    fd.write(
        "- [Heartbeat](entities/heartbeat/index.md): Heartbeat monitoring functionality\n"
    )
    fd.write("- [Logs](entities/logs/index.md): Log management functionality\n")
    fd.write("- [API Clients](client/index.md): API client documentation\n\n")
    fd.write("## Overview\n\n")
    fd.write(
        "The Upassist Python SDK provides a comprehensive set of tools for interacting "
        "with the Upassist Cloud API. "
    )
    fd.write(
        "The SDK is designed to be both powerful and easy to use, with support for "
        "both synchronous and asynchronous operations.\n\n"
    )
    fd.write("### Key Features\n\n")
    fd.write(
        "- **Heartbeat Monitoring**: Create and manage heartbeat monitors for your applications\n"
    )
    fd.write("- **Log Management**: Collect and manage application logs\n")
    fd.write(
        "- **API Clients**: Both synchronous and asynchronous API clients available\n"
    )
    fd.write(
        "- **Type Safety**: Built with Pydantic for robust type checking and validation\n"
    )

# Map module paths to documentation files
module_mapping = {
    "entities/heartbeat": "entities/heartbeat/index.md",
    "entities/logs": "entities/logs/index.md",
    "client": "client/index.md",
}

# Module descriptions and examples
module_descriptions = {
    "entities/heartbeat": {
        "title": "Heartbeat",
        "description": "The Heartbeat module provides functionality to manage and interact with heartbeat monitors.",
        "features": [
            "Create and manage heartbeat monitors",
            "Send heartbeat events",
            "Configure alert settings",
            "Manage maintenance windows",
        ],
        "examples": [
            {
                "title": "Basic Usage",
                "description": "Create and use a heartbeat monitor",
                "code": """import upassist

# Configure API key
upassist.config.API_KEY = 'your-api-key'

# Create a heartbeat instance
heartbeat = upassist.Heartbeat("my-heartbeat")

# Send a heartbeat event
heartbeat.event()""",
            },
            {
                "title": "Advanced Configuration",
                "description": "Create a heartbeat with custom settings",
                "code": """from upassist.entities.heartbeat import Heartbeat, HeartbeatCreateSchema
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
)""",
            },
            {
                "title": "Managing Heartbeats",
                "description": "List, pause, and manage heartbeats",
                "code": """# List all heartbeats
heartbeats = heartbeat.list()

# Get details of a specific heartbeat
details = heartbeat.detail()

# Pause a heartbeat
heartbeat.pause()

# Resume a heartbeat
heartbeat.unpause()

# Delete a heartbeat
heartbeat.delete()""",
            },
        ],
    },
    "entities/logs": {
        "title": "Logs",
        "description": "The Logs module allows you to collect and send log entries to the Upassist Cloud API.",
        "features": [
            "Send log entries in batches",
            "Structured log data with timestamps",
            "Custom metadata support",
            "Type-safe log entries with Pydantic",
        ],
        "examples": [
            {
                "title": "Basic Usage",
                "description": "Send log entries to Upassist Cloud",
                "code": """from upassist.entities.logs import Logs, LogItemSchema
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
response = logs.collect(log_entries)""",
            },
            {
                "title": "Advanced Usage",
                "description": "Send logs with custom configuration",
                "code": """from upassist.entities.logs import Logs, LogItemSchema
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
response = logs.collect(log_entries)""",
            },
        ],
    },
    "client": {
        "title": "API Clients",
        "description": (
            "The SDK provides both synchronous and asynchronous API clients for interacting with "
            "the Upassist Cloud API. The clients automatically handle URL construction by "
            "prepending the base API URL to relative paths."
        ),
        "features": [
            "Synchronous client for simple use cases",
            "Asynchronous client for high-performance applications",
            "Automatic retry and error handling",
            "Type-safe API responses",
            "Automatic base URL handling",
        ],
        "examples": [
            {
                "title": "Synchronous Client",
                "description": "Use the synchronous client for simple operations",
                "code": """from upassist import SyncAPIClient

# Create a synchronous client
client = SyncAPIClient(api_key="your-api-key")

# Make API requests - base URL is automatically prepended
response = client.get("/heartbeats")  # Calls https://api.upassist.cloud/v1/heartbeats
response = client.get("heartbeats")   # Same as above

# Full URLs are used as-is
response = client.get("https://custom-api.upassist.cloud/v1/heartbeats")""",
            },
            {
                "title": "Asynchronous Client",
                "description": "Use the asynchronous client for high-performance operations",
                "code": """from upassist import AsyncAPIClient
import asyncio

async def main():
    # Create an asynchronous client
    client = AsyncAPIClient(api_key="your-api-key")

    # Make concurrent API requests - base URL is automatically prepended
    responses = await asyncio.gather(
        client.get("/heartbeats"),     # Calls https://api.upassist.cloud/v1/heartbeats
        client.get("logs"),            # Calls https://api.upassist.cloud/v1/logs
        client.get("https://custom-api.upassist.cloud/v1/metrics")  # Uses full URL
    )

    # Process responses
    heartbeats, logs, metrics = [r.json() for r in responses]

# Run the async code
asyncio.run(main())""",
            },
            {
                "title": "Error Handling",
                "description": "Handle API errors gracefully",
                "code": """from upassist import SyncAPIClient
from upassist.exceptions import APIError

client = SyncAPIClient(api_key="your-api-key")

try:
    response = client.get("/heartbeats")
except APIError as e:
    print(f"API Error: {e}")
    # Handle the error appropriately
""",
            },
        ],
    },
}

for path in sorted(Path("upassist").rglob("*.py")):
    module_path = path.relative_to("upassist").with_suffix("")
    parts = list(module_path.parts)

    if parts[-1] == "__init__":
        parts = parts[:-1]
    elif parts[-1] == "__main__":
        continue

    # Skip if parts is empty after processing
    if not parts:
        continue

    # Convert module path to documentation path
    module_key = "/".join(parts)
    if module_key in module_mapping:
        doc_path = module_mapping[module_key]
        full_doc_path = reference_dir / doc_path

        # Create parent directories if they don't exist
        full_doc_path.parent.mkdir(parents=True, exist_ok=True)

        with open(full_doc_path, "w") as fd:
            module_info = module_descriptions[module_key]
            fd.write(f"# {module_info['title']}\n\n")
            fd.write(f"{module_info['description']}\n\n")

            fd.write("## Features\n\n")
            for feature in module_info["features"]:
                fd.write(f"- {feature}\n")
            fd.write("\n")

            fd.write("## Examples\n\n")
            for example in module_info["examples"]:
                fd.write(f"### {example['title']}\n\n")     # type: ignore
                fd.write(f"{example['description']}\n\n")     # type: ignore
                fd.write("```python\n")
                fd.write(example["code"])     # type: ignore
                fd.write("\n```\n\n")

            fd.write("## API Reference\n\n")
            ident = ".".join(parts)
            fd.write(f"::: upassist.{ident}")

            # Add footer
            fd.write("\n\n---\n\n")
            fd.write(
                "For more information and to get started with monitoring your applications, visit [Upassist Cloud](https://upassist.cloud/)"
            )
