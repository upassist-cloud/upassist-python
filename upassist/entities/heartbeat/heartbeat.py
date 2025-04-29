from typing import Type

from upassist import config
from upassist.client import AbstractAPIClient, SyncAPIClient
from upassist.entities.base import BaseEntity
from upassist.schemas.base import DetailResponse
from upassist.utils.attributes import attribute_required

from .schemas import (
    HeartbeatCreateSchema,
    HeartbeatDetailSchema,
    HeartbeatPaginatedSchema,
    HeartbeatSchema,
)

heartbeat_slug_required = attribute_required("heartbeat_slug")


class Heartbeat(BaseEntity):
    base_heartbeat_event_api_url: str = "https://heartbeats.upassist.cloud/api"

    def __init__(
        self,
        heartbeat_slug: str | None = None,
        api_key: str | None = None,
        api_version: str | None = None,
        api_client_cls: Type[AbstractAPIClient] = SyncAPIClient,
    ):
        super().__init__(
            api_key=api_key or config.API_KEY,
            api_version=api_version or config.API_VERSION,
            api_client_cls=api_client_cls,
        )
        self.heartbeat_slug = heartbeat_slug

    def list(
        self, q: str | None = None, page: int | None = None, per_page: int | None = None
    ) -> HeartbeatPaginatedSchema:
        response = self.api_client.request(
            "GET",
            self.base_heartbeats_api_url,
            params={
                "q": q,
                "page": page,
                "per_page": per_page,
            },
        )
        return HeartbeatPaginatedSchema.model_validate(response)

    @property
    def base_heartbeats_api_url(self) -> str:
        return f"{self.api_client.base_api_url}/heartbeats"

    @heartbeat_slug_required
    def detail(self) -> HeartbeatDetailSchema:
        response = self.api_client.request(
            "GET", f"{self.base_heartbeats_api_url}/{self.heartbeat_slug}"
        )
        return HeartbeatDetailSchema.model_validate(response)

    @heartbeat_slug_required
    def pause(self):
        return self.api_client.request(
            "PATCH",
            f"{self.base_heartbeats_api_url}/{self.heartbeat_slug}/pause",
        )

    @heartbeat_slug_required
    def unpause(self):
        return self.api_client.request(
            "PATCH",
            f"{self.base_heartbeats_api_url}/{self.heartbeat_slug}/unpause",
        )

    @heartbeat_slug_required
    def delete(self) -> None:
        self.api_client.request(
            "DELETE", f"{self.base_heartbeats_api_url}/{self.heartbeat_slug}"
        )

    @heartbeat_slug_required
    def event(self) -> DetailResponse:
        return self.api_client.request(
            "GET", f"{self.base_heartbeat_event_api_url}/event/{self.heartbeat_slug}"
        )

    def create(self, heartbeat: HeartbeatCreateSchema) -> HeartbeatSchema:
        """
        Create a new heartbeat.

        Args:
            heartbeat (HeartbeatCreateSchema): The heartbeat configuration.
        """
        response = self.api_client.request(
            "POST",
            self.base_heartbeats_api_url,
            json=heartbeat.model_dump(exclude_unset=True),
        )
        return HeartbeatSchema.model_validate(response)
