from enum import StrEnum


class LogFilterTypeEnum(StrEnum):
    INTEGER = "INTEGER"
    STRING = "STRING"

    def __str__(self) -> str:
        return str(self.value)
