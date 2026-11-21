from enum import StrEnum


class AxisScaleEnum(StrEnum):
    LINEAR = "LINEAR"
    LOGARITHMIC = "LOGARITHMIC"

    def __str__(self) -> str:
        return str(self.value)
