from enum import StrEnum


class PolicySortingEnum(StrEnum):
    NAME = "name"

    def __str__(self) -> str:
        return str(self.value)
