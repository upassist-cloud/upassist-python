from enum import StrEnum


class DashboardVariableTypeEnum(StrEnum):
    BOOLEAN = "BOOLEAN"
    DATE = "DATE"
    DATETIME = "DATETIME"
    NUMBER = "NUMBER"
    SELECT = "SELECT"
    SQL_EXPRESSION = "SQL_EXPRESSION"
    TEXT = "TEXT"

    def __str__(self) -> str:
        return str(self.value)
