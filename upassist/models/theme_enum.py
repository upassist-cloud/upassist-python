from enum import StrEnum


class ThemeEnum(StrEnum):
    DARK = "DARK"
    LIGHT = "LIGHT"
    SYSTEM = "SYSTEM"

    def __str__(self) -> str:
        return str(self.value)
