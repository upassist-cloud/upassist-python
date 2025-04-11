import functools
import uuid
from typing import Type
from uuid import UUID

from upassist.client import AbstractAPIClient, SyncAPIClient
from upassist import config


def attribute_required(attribute: str):
    def wrapper(func):
        @functools.wraps(func)
        def inner(self, *args, **kwargs):
            if not getattr(self, attribute):
                raise ValueError(f"`{attribute}` is required to perform object action")
            return func(self, *args, **kwargs)
        return inner
    return wrapper


class Heartbeat:

    def __init__(
            self,
            heartbeat_id: str | UUID | None = None,
            heartbeat_slug: str | None = None,
            api_key: str | None = None,
            api_version: str | None = None,
            api_client_cls: Type[AbstractAPIClient] = SyncAPIClient
    ):
        self.heartbeat_id = heartbeat_id
        self.heartbeat_slug = heartbeat_slug
        self.api_client = api_client_cls(
            api_key=api_key or config.API_KEY,
            api_version=api_version or config.API_VERSION,
        )

    @attribute_required("heartbeat_slug")
    def event(self):
        return self.api_client.request("get", f"https://heartbeats.upassist.cloud/api/event/{self.heartbeat_slug}")
