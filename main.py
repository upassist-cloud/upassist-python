import upassist

upassist.config.API_KEY = "HORSoN5p8pY1ZFez9SqEMDy5cWjmdtIC"

heartbeat = upassist.Heartbeat(heartbeat_slug="db5d460-c32a-446c-86fa-5c65a901ce87")
print(heartbeat.detail())
