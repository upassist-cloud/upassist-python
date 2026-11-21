from enum import StrEnum


class MaintenanceTimelineTypeEnum(StrEnum):
    ONGOING = "ONGOING"
    PAST = "PAST"
    UPCOMING = "UPCOMING"

    def __str__(self) -> str:
        return str(self.value)
