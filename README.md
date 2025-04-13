# Official Upassist Cloud Python SDK

## Installation

```
pip install upassist
```

## Heartbeat event

```python
import upassist

upassist.config.API_KEY = 'you-api-key'

heartbeat = upassist.Heartbeat("cron-job-foo")
heartbeat.event()
```
