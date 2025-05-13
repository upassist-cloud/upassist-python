from abc import ABC, abstractmethod
from typing import Any

from upassist import config


class AbstractAPIClient(ABC):
    """Base class for API clients that provides common functionality for making HTTP requests.

    This abstract class defines the interface and common functionality for API clients.
    It handles authentication, request formatting, and provides convenience methods
    for different HTTP methods.

    The client can be initialized with an API key and version, or it will use the values
    from the config module if not provided.

    Example:
        ```python
        from upassist import config
        from upassist.client import YourAPIClient

        # Initialize with config values
        client = YourAPIClient()  # Uses config.API_KEY and config.API_VERSION

        # Or override config values
        client = YourAPIClient(
            api_key="your-api-key",
            api_version="v1"
        )

        # Make requests using convenience methods
        response = client.get('users', params={'page': 1})
        response = client.post('users', json={'name': 'John'})
        response = client.delete('users/123')

        # Or use the base request method
        response = client.request(
            method='GET',
            url='users',
            params={'page': 1}
        )
        ```
    """

    def __init__(self, api_key: str | None = None, api_version: str | None = None):
        """Initialize the API client.

        Args:
            api_key: Optional API key. If not provided, uses config.API_KEY
            api_version: Optional API version. If not provided, uses config.API_VERSION
        """
        self._check_required_packages()
        self.api_key = api_key or config.API_KEY
        self.api_version = api_version or config.API_VERSION

    @property
    def base_api_url(self) -> str:
        return f"https://api.upassist.cloud/{self.api_version}"

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
        json: dict[Any, Any] | list[Any] | None = None,
    ) -> Any:
        return

    def request(
        self,
        method: str,
        url: str,
        params: dict | None = None,
        headers: dict | None = None,
        json: dict[Any, Any] | list[Any] | None = None,
    ) -> Any:
        if headers is None:
            headers = {}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"

        # Prepend base_api_url if URL doesn't start with http
        if not url.startswith(("http://", "https://")):
            url = f"{self.base_api_url}/{url.lstrip('/')}"

        return self._request(
            method=method,
            url=url,
            params=params,
            headers=headers,
            json=json,
        )

    def get(self, url: str, params: dict | None = None, headers: dict | None = None) -> Any:
        return self.request(method="GET", url=url, params=params, headers=headers)

    def post(
        self,
        url: str,
        json: dict[Any, Any] | list[Any] | None = None,
        params: dict | None = None,
        headers: dict | None = None,
    ) -> Any:
        return self.request(method="POST", url=url, json=json, params=params, headers=headers)

    def put(
        self,
        url: str,
        json: dict[Any, Any] | list[Any] | None = None,
        params: dict | None = None,
        headers: dict | None = None,
    ) -> Any:
        return self.request(method="PUT", url=url, json=json, params=params, headers=headers)

    def patch(
        self,
        url: str,
        json: dict[Any, Any] | list[Any] | None = None,
        params: dict | None = None,
        headers: dict | None = None,
    ) -> Any:
        return self.request(method="PATCH", url=url, json=json, params=params, headers=headers)

    def delete(self, url: str, params: dict | None = None, headers: dict | None = None) -> Any:
        return self.request(method="DELETE", url=url, params=params, headers=headers)

    def head(self, url: str, params: dict | None = None, headers: dict | None = None) -> Any:
        return self.request(method="HEAD", url=url, params=params, headers=headers)

    def options(self, url: str, params: dict | None = None, headers: dict | None = None) -> Any:
        return self.request(method="OPTIONS", url=url, params=params, headers=headers)
