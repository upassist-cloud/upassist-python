from enum import StrEnum


class MonitorTypeEnum(StrEnum):
    ENDPOINT = "ENDPOINT"
    PING = "PING"

    def __str__(self) -> str:
        return str(self.value)
