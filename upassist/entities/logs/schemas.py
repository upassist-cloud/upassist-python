from datetime import datetime
from typing import Any

from pydantic import BaseModel


class LogItemSchema(BaseModel):
    dt: datetime | None = None
    host: str | None = None
    message: str | None = None
    file: str | None = None
    data: dict[str, Any] | None = None
