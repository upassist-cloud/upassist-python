from enum import StrEnum


class ChartQueryTypeEnum(StrEnum):
    QUERY_BUILDER = "QUERY_BUILDER"
    SQL_EXPRESSION = "SQL_EXPRESSION"
    STATIC_TEXT = "STATIC_TEXT"

    def __str__(self) -> str:
        return str(self.value)
