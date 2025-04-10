import asyncio

from upassist.client import AsyncAPIClient
from upassist.entities.heartbeat import Heartbeat


async def main():
    print(await Heartbeat(object_key="123123123", api_client_cls=AsyncAPIClient).event())


asyncio.run(main())