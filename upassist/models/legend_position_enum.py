from enum import StrEnum


class LegendPositionEnum(StrEnum):
    BELLOW = "BELLOW"
    HIDDEN = "HIDDEN"
    RIGHT = "RIGHT"

    def __str__(self) -> str:
        return str(self.value)
