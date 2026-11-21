from enum import StrEnum


class ProjectMemberRoleEnum(StrEnum):
    ADMIN = "ADMIN"
    MEMBER = "MEMBER"
    OWNER = "OWNER"

    def __str__(self) -> str:
        return str(self.value)
