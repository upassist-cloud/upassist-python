# Upassist Python SDK

Welcome to the official documentation for the Upassist Cloud Python SDK. This SDK provides a simple and intuitive way to interact with the Upassist Cloud API.

## Features

- **Heartbeat Monitoring**: Create and manage heartbeat monitors for your applications
- **Log Management**: Collect and manage application logs
- **API Clients**: Both synchronous and asynchronous API clients available
- **Type Safety**: Built with Pydantic for robust type checking and validation

## Quick Start

```python
import upassist

# Configure your API key
upassist.config.API_KEY = 'your-api-key'

# Create a heartbeat instance
heartbeat = upassist.Heartbeat("your-heartbeat-slug")

# Send a heartbeat event
heartbeat.event()
```

## Installation

```bash
pip install upassist
```

For development dependencies:

```bash
pip install upassist[docs]
```

## Documentation Structure

- [Installation](installation.md): Detailed installation instructions
- [Configuration](configuration.md): How to configure the SDK
- [API Reference](reference/): Detailed API documentation
  - [Heartbeat](reference/heartbeat.md): Heartbeat monitoring functionality
  - [Logs](reference/logs.md): Log management functionality
  - [API Clients](reference/api_clients.md): API client documentation 