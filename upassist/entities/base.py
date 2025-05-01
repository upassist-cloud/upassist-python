from upassist import config
from upassist.client._sync import SyncAPIClient
from upassist.client.abstract import AbstractAPIClient


class BaseEntity:
    """Base class for all API entities.

    This class provides common functionality for interacting with the API,
    including API client initialization and base URL management.
    """

    def __init__(
        self,
        api_key: str | None = None,
        api_version: str | None = None,
        api_client_cls: type[AbstractAPIClient] = SyncAPIClient,
    ):
        """Initialize a new entity instance.

        Args:
            api_key: Optional API key for authentication
            api_version: Optional API version to use
            api_client_cls: Class to use for API client implementation
        """
        self.api_client = api_client_cls(
            api_key=api_key or config.API_KEY,
            api_version=api_version or config.API_VERSION,
        )

    @property
    def base_api_url(self) -> str:
        """Get the base URL for API endpoints.

        Returns:
            Base URL for API endpoints
        """
        return self.api_client.base_api_url
