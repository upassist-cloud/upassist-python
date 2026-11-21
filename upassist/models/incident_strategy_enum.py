from enum import StrEnum


class IncidentStrategyEnum(StrEnum):
    CHECKS = "CHECKS"
    LOCATIONS = "LOCATIONS"
    PERIOD = "PERIOD"

    def __str__(self) -> str:
        return str(self.value)
