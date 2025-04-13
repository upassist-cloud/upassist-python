import functools
from typing import Type

from upassist import config
from upassist.client import AbstractAPIClient, SyncAPIClient


def attribute_required(attribute: str):
    def wrapper(func):
        @functools.wraps(func)
        def inner(self, *args, **kwargs):
            if not getattr(self, attribute):
                raise ValueError(f"`{attribute}` is required to perform object action")
            return func(self, *args, **kwargs)

        return inner

    return wrapper


heartbeat_slug_required = attribute_required("heartbeat_slug")


class Heartbeat:

    def __init__(
        self,
        heartbeat_slug: str | None = None,
        api_key: str | None = None,
        api_version: str | None = None,
        api_client_cls: Type[AbstractAPIClient] = SyncAPIClient,
    ):
        self.heartbeat_slug = heartbeat_slug
        self.api_client = api_client_cls(
            api_key=api_key or config.API_KEY,
            api_version=api_version or config.API_VERSION,
        )

    def list(
        self, q: str | None = None, page: int | None = None, per_page: int | None = None
    ):
        return self.api_client.request(
            "GET",
            "https://api.upassist.cloud/v1/heartbeats",
            params={
                "q": q,
                "page": page,
                "per_page": per_page,
            },
        )

    @heartbeat_slug_required
    def detail(self):
        return self.api_client.request(
            "GET", f"https://api.upassist.cloud/v1/heartbeats/{self.heartbeat_slug}"
        )

    @heartbeat_slug_required
    def pause(self):
        return self.api_client.request(
            "PATCH",
            f"https://api.upassist.cloud/v1/heartbeats/{self.heartbeat_slug}/pause",
        )

    @heartbeat_slug_required
    def unpause(self):
        return self.api_client.request(
            "PATCH",
            f"https://api.upassist.cloud/v1/heartbeats/{self.heartbeat_slug}/unpause",
        )

    @heartbeat_slug_required
    def delete(self):
        return self.api_client.request(
            "DELETE", f"https://api.upassist.cloud/v1/heartbeats/{self.heartbeat_slug}"
        )

    @heartbeat_slug_required
    def event(self):
        return self.api_client.request(
            "GET", f"https://heartbeats.upassist.cloud/api/event/{self.heartbeat_slug}"
        )
