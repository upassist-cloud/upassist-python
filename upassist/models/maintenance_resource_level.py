from enum import StrEnum


class MaintenanceResourceLevel(StrEnum):
    HIGH = "HIGH"
    LOW = "LOW"
    MEDIUM = "MEDIUM"

    def __str__(self) -> str:
        return str(self.value)
