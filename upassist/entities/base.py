from typing import Type

from upassist import config
from upassist.client._sync import SyncAPIClient
from upassist.client.abstract import AbstractAPIClient


class BaseEntity:
    def __init__(
        self,
        api_key: str | None = None,
        api_version: str | None = None,
        api_client_cls: Type[AbstractAPIClient] = SyncAPIClient,
    ):
        self.api_client = api_client_cls(
            api_key=api_key or config.API_KEY,
            api_version=api_version or config.API_VERSION,
        )

    @property
    def base_api_url(self) -> str:
        return self.api_client.base_api_url
