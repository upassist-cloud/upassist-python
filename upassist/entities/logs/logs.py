from upassist.entities.base import BaseEntity
from upassist.schemas.base import DetailResponse

from .schemas import LogItemSchema


class Logs(BaseEntity):
    base_logs_api_url: str = "https://logs.upassist.cloud/collect"

    def collect(self, logs: list[LogItemSchema]) -> DetailResponse:
        response = self.api_client.request(
            "POST",
            self.base_logs_api_url,
            json=[log.model_dump(mode="json") for log in logs],
        )
        return DetailResponse.model_validate(response)
