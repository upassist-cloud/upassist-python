from enum import StrEnum


class IntegrationSourceEnum(StrEnum):
    DISCORD = "DISCORD"
    EMAIL = "EMAIL"
    SLACK = "SLACK"
    TEAMS = "TEAMS"
    TELEGRAM = "TELEGRAM"
    WEBHOOK = "WEBHOOK"

    def __str__(self) -> str:
        return str(self.value)
