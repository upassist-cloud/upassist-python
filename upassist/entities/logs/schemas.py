from datetime import datetime
from typing import Any

from pydantic import BaseModel


class LogItemSchema(BaseModel):
    """Schema for individual log items.

    Attributes:
        dt: Timestamp of the log entry
        host: Hostname or source of the log
        message: Log message content
        file: Source file or location
        data: Additional structured data associated with the log
    """

    dt: datetime | None = None
    host: str | None = None
    message: str | None = None
    file: str | None = None
    data: dict[str, Any] | None = None
