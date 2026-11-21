from enum import StrEnum


class HeartbeatStatusEnum(StrEnum):
    DOWN = "DOWN"
    OK = "OK"
    PAUSED = "PAUSED"

    def __str__(self) -> str:
        return str(self.value)
