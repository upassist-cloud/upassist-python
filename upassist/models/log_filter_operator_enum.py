from enum import StrEnum


class LogFilterOperatorEnum(StrEnum):
    CONTAINS = "CONTAINS"
    EQUALS = "EQUALS"
    GT = "GT"
    GTE = "GTE"
    LT = "LT"
    LTE = "LTE"
    NOT_CONTAINS = "NOT_CONTAINS"
    NOT_EQUALS = "NOT_EQUALS"
    NOT_REGEX = "NOT_REGEX"
    REGEX = "REGEX"

    def __str__(self) -> str:
        return str(self.value)
