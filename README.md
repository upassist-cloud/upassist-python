# Official Upassist Cloud Python SDK

## Installation

```
pip install upassist
```

## Heartbeat event

You can configure all of your monitors using a single YAML file. This can be version controlled and synced to Cronitor as part of
a deployment or build process. For details on all of the attributes that can be set, see the [Monitor API](https://cronitor.io/docs/monitor-api) documentation.


```python
import upassist

upassist.api_key = 'you-api-key'

heartbeat = upassist.Heartbeat(heartbeat_slug="cron-job-foo")
heartbeat.event()
```
