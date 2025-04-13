import importlib.util
from typing import Any

from ..errors import APIError
from .abstract import AbstractAPIClient


class SyncAPIClient(AbstractAPIClient):

    def _check_required_packages(self) -> None:
        if not importlib.util.find_spec("aiohttp"):
            raise ImportError(
                "You need to install the `requests` package to use sync client"
            )

    def _request(
        self,
        method: str,
        url: str,
        params: dict | None = None,
        headers: dict | None = None,
        json: dict | None = None,
    ) -> Any:
        import requests

        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            json=json,
            params=params,
        )
        if not response.ok:
            raise APIError(response.json())
        return response.json()
