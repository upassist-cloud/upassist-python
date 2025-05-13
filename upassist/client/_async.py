import importlib.util
from typing import Any

from ..errors import APIError
from .abstract import AbstractAPIClient


class AsyncAPIClient(AbstractAPIClient):

    def _check_required_packages(self):
        if not importlib.util.find_spec("aiohttp"):
            raise ImportError("You need to install the `aiohttp` package to use async client")

    async def _request(
        self,
        method: str,
        url: str,
        params: dict | None = None,
        headers: dict | None = None,
        json: dict[Any, Any] | list[Any] | None = None,
    ) -> Any:
        import aiohttp

        async with aiohttp.ClientSession() as session:
            async with session.request(method, url, headers=headers, json=json, params=params) as response:
                if not response.ok:
                    raise APIError(await response.json(), response.url)
                return await response.json()
