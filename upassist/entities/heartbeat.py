import functools
from typing import Type

from upassist.client import AbstractAPIClient, SyncAPIClient
from upassist import config


def detail_action(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self.object_key:
            raise ValueError("`object_key` is required to perform detail object action")
        return func(self, *args, **kwargs)
    return wrapper


class Heartbeat:

    def __init__(
            self,
            object_key: str | None = None,
            api_key: str | None = None,
            api_version: str | None = None,
            api_client_cls: Type[AbstractAPIClient] = SyncAPIClient
    ):
        self.object_key = object_key
        self.api_client = api_client_cls(
            api_key=api_key or config.API_KEY,
            api_version=api_version or config.API_VERSION,
        )

    @detail_action
    def event(self):
        return self.api_client.request("get", f"https://heartbeats.upassist.cloud/api/event/{self.object_key}")
