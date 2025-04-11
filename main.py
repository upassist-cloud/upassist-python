import asyncio

import upassist

async def main():
    print(await upassist.Heartbeat(heartbeat_slug="123123123", api_client_cls=upassist.AsyncAPIClient).event())

upassist.config.API_KEY = "HORSoN5p8pY1ZFez9SqEMDy5cWjmdtIC"
asyncio.run(main())