from enum import StrEnum


class IncidentContentTypeEnum(StrEnum):
    CHART_ALERT = "CHART_ALERT"
    ERROR_ISSUE = "ERROR_ISSUE"
    HEARTBEAT = "HEARTBEAT"
    MANUAL = "MANUAL"
    MONITOR = "MONITOR"
    SITE_ALERT = "SITE_ALERT"

    def __str__(self) -> str:
        return str(self.value)
