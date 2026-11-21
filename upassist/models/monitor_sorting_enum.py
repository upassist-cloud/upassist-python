from enum import StrEnum


class MonitorSortingEnum(StrEnum):
    CREATED_AT = "created_at"
    FETCH_INTERVAL = "fetch_interval"
    NAME = "name"

    def __str__(self) -> str:
        return str(self.value)
