from typing import Any

from .abstract import AbstractAPIClient

class AsyncAPIClient(AbstractAPIClient):

    def _check_required_packages(self):
        try:
            import aiohttp
        except ImportError as e:
            raise ImportError("You need to install the aiohttp package to use async client") from e

    async def _request(self, method: str, url: str, params: dict | None = None, headers: dict | None = None, json: dict | None = None) -> Any:
        import aiohttp

        async with aiohttp.ClientSession() as session:
            async with session.request(method, url, headers=headers, json=json, params=params) as response:
                return await response.json()
