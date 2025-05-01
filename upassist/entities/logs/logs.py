from upassist.entities.base import BaseEntity
from upassist.schemas.base import DetailResponse

from .schemas import LogItemSchema


class Logs(BaseEntity):
    """Entity for managing log collection and submission.

    This class provides functionality to collect and submit logs to the logging service.
    """

    base_logs_api_url: str = "https://logs.upassist.cloud/collect"

    def collect(self, logs: list[LogItemSchema]) -> DetailResponse:
        """Submit a collection of logs to the logging service.

        Args:
            logs: List of log items to submit

        Returns:
            DetailResponse containing the submission result
        """
        response = self.api_client.post(
            self.base_logs_api_url,
            json=[log.model_dump(mode="json") for log in logs],
        )
        return DetailResponse.model_validate(response)
