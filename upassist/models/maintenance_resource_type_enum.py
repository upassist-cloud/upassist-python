from enum import StrEnum


class MaintenanceResourceTypeEnum(StrEnum):
    HEARTBEAT = "HEARTBEAT"
    MONITOR = "MONITOR"
    MONITOR_GROUP = "MONITOR_GROUP"

    def __str__(self) -> str:
        return str(self.value)
