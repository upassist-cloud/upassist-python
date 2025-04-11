import upassist

upassist.config.API_KEY = "HORSoN5p8pY1ZFez9SqEMDy5cWjmdtIC"

heartbeat = upassist.Heartbeat(heartbeat_slug="cron-job-foo")
heartbeat.event()