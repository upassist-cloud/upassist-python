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
    """A class representing a heartbeat monitoring entity.

    This class provides functionality to manage and interact with heartbeat monitors,
    including creating, listing, pausing, and managing heartbeat events.
    """

    base_heartbeat_event_api_url: str = "https://heartbeats.upassist.cloud/api"

    def __init__(
        self,
        heartbeat_slug: str | None = None,
        api_key: str | None = None,
        api_version: str | None = None,
        api_client_cls: type[AbstractAPIClient] = SyncAPIClient,
    ):
        """Initialize a new Heartbeat instance.

        Args:
            heartbeat_slug: Unique identifier for the heartbeat
            api_key: API key for authentication
            api_version: API version to use
            api_client_cls: Class to use for API client implementation
        """
        super().__init__(
            api_key=api_key or config.API_KEY,
            api_version=api_version or config.API_VERSION,
            api_client_cls=api_client_cls,
        )
        self.heartbeat_slug = heartbeat_slug

    def list(
        self, q: str | None = None, page: int | None = None, per_page: int | None = None
    ) -> HeartbeatPaginatedSchema:
        """List all heartbeats with optional filtering and pagination.

        Args:
            q: Search query string
            page: Page number for pagination
            per_page: Number of items per page

        Returns:
            HeartbeatPaginatedSchema containing the list of heartbeats
        """
        response = self.api_client.get(
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
        """Get the base URL for heartbeat API endpoints.

        Returns:
            Base URL for heartbeat API endpoints
        """
        return f"{self.api_client.base_api_url}/heartbeats"

    @heartbeat_slug_required
    def detail(self) -> HeartbeatDetailSchema:
        """Get detailed information about a specific heartbeat.

        Returns:
            HeartbeatDetailSchema containing detailed heartbeat information
        """
        response = self.api_client.get(f"{self.base_heartbeats_api_url}/{self.heartbeat_slug}")
        return HeartbeatDetailSchema.model_validate(response)

    @heartbeat_slug_required
    def pause(self):
        """Pause the heartbeat monitoring."""
        return self.api_client.patch(
            f"{self.base_heartbeats_api_url}/{self.heartbeat_slug}/pause",
        )

    @heartbeat_slug_required
    def unpause(self):
        """Resume the heartbeat monitoring."""
        return self.api_client.patch(
            f"{self.base_heartbeats_api_url}/{self.heartbeat_slug}/unpause",
        )

    @heartbeat_slug_required
    def delete(self) -> None:
        """Delete the heartbeat."""
        self.api_client.delete(f"{self.base_heartbeats_api_url}/{self.heartbeat_slug}")

    @heartbeat_slug_required
    def event(self) -> DetailResponse:
        """Get the current event status of the heartbeat.

        Returns:
            DetailResponse containing the event status
        """
        return self.api_client.get(f"{self.base_heartbeat_event_api_url}/event/{self.heartbeat_slug}")

    def create(self, heartbeat: HeartbeatCreateSchema) -> HeartbeatSchema:
        """Create a new heartbeat.

        Args:
            heartbeat: The heartbeat configuration.

        Returns:
            HeartbeatSchema containing the created heartbeat information
        """
        response = self.api_client.post(
            self.base_heartbeats_api_url,
            json=heartbeat.model_dump(exclude_unset=True),
        )
        return HeartbeatSchema.model_validate(response)
