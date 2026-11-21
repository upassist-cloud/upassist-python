from enum import StrEnum


class EscalationTypeEnum(StrEnum):
    DISCORD = "DISCORD"
    EMAIL = "EMAIL"
    TELEGRAM = "TELEGRAM"

    def __str__(self) -> str:
        return str(self.value)
