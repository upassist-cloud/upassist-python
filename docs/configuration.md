# Configuration

The Upassist Python SDK can be configured in several ways to suit your needs.

## API Key Configuration

### Global Configuration

Set your API key globally for all SDK operations:

```python
import upassist

upassist.config.API_KEY = 'your-api-key'
```

### Per-Instance Configuration

You can also specify the API key when creating instances:

```python
from upassist import Heartbeat, Logs

# Configure Heartbeat with specific API key
heartbeat = Heartbeat(
    heartbeat_slug="your-heartbeat-slug",
    api_key="your-api-key"
)

# Configure Logs with specific API key
logs = Logs(api_key="your-api-key")
```

## API Version

The SDK supports different API versions. You can configure this globally or per instance:

```python
import upassist

# Global configuration
upassist.config.API_VERSION = "v1"

# Per-instance configuration
heartbeat = upassist.Heartbeat(
    heartbeat_slug="your-heartbeat-slug",
    api_version="v1"
)
```

## API Client Selection

The SDK provides both synchronous and asynchronous clients. You can choose which one to use:

```python
from upassist import Heartbeat, SyncAPIClient, AsyncAPIClient

# Use synchronous client (default)
heartbeat = Heartbeat("your-heartbeat-slug")

# Use asynchronous client
heartbeat = Heartbeat(
    "your-heartbeat-slug",
    api_client_cls=AsyncAPIClient
)
```

## Environment Variables

You can also configure the SDK using environment variables:

```bash
export UPASSIST_API_KEY="your-api-key"
export UPASSIST_API_VERSION="v1"
```

The SDK will automatically pick up these environment variables if they are set.

## Configuration Priority

The configuration is applied in the following order of priority:

1. Per-instance configuration
2. Global configuration
3. Environment variables
4. Default values 