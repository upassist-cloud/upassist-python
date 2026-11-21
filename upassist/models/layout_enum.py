from enum import StrEnum


class LayoutEnum(StrEnum):
    HORIZONTAL = "HORIZONTAL"
    VERTICAL = "VERTICAL"

    def __str__(self) -> str:
        return str(self.value)
