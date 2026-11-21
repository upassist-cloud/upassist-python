from enum import StrEnum


class ScanningTypeEnum(StrEnum):
    REGEXP = "REGEXP"
    SPECIAL_TAGS = "SPECIAL_TAGS"

    def __str__(self) -> str:
        return str(self.value)
