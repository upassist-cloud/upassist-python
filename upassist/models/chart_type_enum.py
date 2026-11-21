from enum import StrEnum


class ChartTypeEnum(StrEnum):
    BAR = "BAR"
    GAUGE = "GAUGE"
    HEATMAP = "HEATMAP"
    LINE = "LINE"
    NUMBER = "NUMBER"
    PIE = "PIE"
    SCATTER = "SCATTER"
    TABLE = "TABLE"
    TEXT = "TEXT"

    def __str__(self) -> str:
        return str(self.value)
