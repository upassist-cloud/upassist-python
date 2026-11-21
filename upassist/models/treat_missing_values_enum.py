from enum import StrEnum


class TreatMissingValuesEnum(StrEnum):
    CONNECTED = "CONNECTED"
    DISCONNECTED = "DISCONNECTED"
    PREVIOUS = "PREVIOUS"
    ZERO = "ZERO"

    def __str__(self) -> str:
        return str(self.value)
