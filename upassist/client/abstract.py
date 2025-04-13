from abc import ABC, abstractmethod
from typing import Any


class AbstractAPIClient(ABC):

    def __init__(self, api_key: str | None = None, api_version: str | None = None):
        self._check_required_packages()
        self.api_key = api_key
        self.api_version = api_version

    @property
    def base_api_url(self) -> str:
        return f"https://api.upassist.cloud/{self.api_version}/"

    @abstractmethod
    def _check_required_packages(self) -> None:
        return

    @abstractmethod
    def _request(
        self,
        method: str,
        url: str,
        params: dict | None = None,
        headers: dict | None = None,
        json: dict | None = None,
    ) -> Any:
        return

    def request(
        self,
        method: str,
        url: str,
        params: dict | None = None,
        headers: dict | None = None,
        json: dict | None = None,
    ) -> Any:
        if headers is None:
            headers = {}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        return self._request(
            method=method,
            url=url,
            params=params,
            headers=headers,
            json=json,
        )
