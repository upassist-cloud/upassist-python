# API Clients

The SDK provides both synchronous and asynchronous API clients for interacting with the Upassist Cloud API. The clients automatically handle URL construction by prepending the base API URL to relative paths.

## Features

- Synchronous client for simple use cases
- Asynchronous client for high-performance applications
- Automatic retry and error handling
- Type-safe API responses
- Automatic base URL handling

## Examples

### Synchronous Client

Use the synchronous client for simple operations

```python
from upassist import SyncAPIClient

# Create a synchronous client
client = SyncAPIClient(api_key="your-api-key")

# Make API requests - base URL is automatically prepended
response = client.get("/heartbeats")  # Calls https://api.upassist.cloud/v1/heartbeats
response = client.get("heartbeats")   # Same as above

# Full URLs are used as-is
response = client.get("https://custom-api.upassist.cloud/v1/heartbeats")
```

### Asynchronous Client

Use the asynchronous client for high-performance operations

```python
from upassist import AsyncAPIClient
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
asyncio.run(main())
```

### Error Handling

Handle API errors gracefully

```python
from upassist import SyncAPIClient
from upassist.exceptions import APIError

client = SyncAPIClient(api_key="your-api-key")

try:
    response = client.get("/heartbeats")
except APIError as e:
    print(f"API Error: {e}")
    # Handle the error appropriately

```

## API Reference

::: upassist.client

---

For more information and to get started with monitoring your applications, visit [Upassist Cloud](https://upassist.cloud/)