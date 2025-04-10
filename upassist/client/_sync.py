from typing import Any

from .abstract import AbstractAPIClient

class SyncAPIClient(AbstractAPIClient):

    def _check_required_packages(self) -> None:
        try:
            import requests
        except ImportError as e:
            raise ImportError("You need to install the requests package to use sync client") from e

    def _request(self, method: str, url: str, params: dict | None = None, headers: dict | None = None, json: dict | None = None) -> Any:
        import requests
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            json=json,
            params=params,
        )
        return response.json()
