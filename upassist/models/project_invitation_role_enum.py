from enum import StrEnum


class ProjectInvitationRoleEnum(StrEnum):
    ADMIN = "ADMIN"
    MEMBER = "MEMBER"

    def __str__(self) -> str:
        return str(self.value)
