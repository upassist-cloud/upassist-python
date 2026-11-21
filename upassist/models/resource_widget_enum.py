from enum import StrEnum


class ResourceWidgetEnum(StrEnum):
    STATUS_HISTORY = "STATUS_HISTORY"
    STATUS_HISTORY_AND_CHART = "STATUS_HISTORY_AND_CHART"
    STATUS_ONLY = "STATUS_ONLY"

    def __str__(self) -> str:
        return str(self.value)
