from datetime import date, datetime, time
from enum import StrEnum
from uuid import UUID

from pydantic import BaseModel, Field, NonNegativeInt, PositiveInt
from pydantic_extra_types.timezone_name import TimeZoneName

from upassist.schemas.base import BasePaginatedSchema, BaseSchema, UUIDSchema


class HeartbeatStatusEnum(StrEnum):
    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"


class HeartbeatCreateSchema(BaseModel):
    name: str
    description: str | None = None
    group_id: UUID | None = None
    slug: str | None = None
    fetch_interval: PositiveInt = Field(default=180, ge=60, le=10**5)
    confirmation_period: NonNegativeInt = Field(default=0, le=10**5)
    realert_period: int | None = Field(default=None)
    alerts_on: bool = True
    paused: bool = False
    meta: dict | None = None
    call: bool = False
    send_sms: bool = False
    send_email: bool = True
    send_push_notification: bool = False
    maintenance_window_from: time | None = None
    maintenance_window_until: time | None = None
    maintenance_window_timezone: str = "Europe/Belfast"
    alert_week_days: list[int] | None = Field(
        default_factory=lambda: [0, 1, 2, 3, 4, 5, 6]
    )


class IncidentStatsSchema(BaseSchema):
    sum: int | None = None
    avg: int | None = None
    max: int | None = None
    count: int | None = None
    from_date: date
    to_date: date
    from_datetime: datetime
    to_datetime: datetime
    period_alias: str | None = None
    uptime_percents: float


class HeartbeatSchema(UUIDSchema):
    name: str
    created_at: datetime
    slug: str
    group_id: UUID | None = None
    status: HeartbeatStatusEnum | None
    is_down: bool
    last_up_at: datetime | None = None
    last_down_at: datetime | None = None
    last_fetch_at: datetime | None = None
    next_fetch_at: datetime | None = None
    fetch_interval: int
    confirmation_period: int | None = None
    paused: bool
    alerts_on: bool = Field(description="Alerts on incident messages")
    call: bool
    send_sms: bool
    send_email: bool
    send_push_notification: bool
    maintenance_window_from: time | None = None
    maintenance_window_until: time | None = None
    maintenance_window_timezone: TimeZoneName = Field(default="Europe/Belfast")
    alert_week_days: list[int] | None = None


class HeartbeatDetailSchema(HeartbeatSchema):
    description: str | None = None
    incidents_count: int | None = Field(default=0)
    opened_incident_id: UUID | None = None
    confirmation_period: NonNegativeInt | None = Field(
        default=None,
        description="Time in seconds to wait until beat before starting images",
    )
    realert_period: NonNegativeInt | None = Field(
        default=None,
        description="Time in seconds to notify users again abouts unresolved incident",
    )
    meta: dict | None = None
    incident_stats: list[IncidentStatsSchema]


class HeartbeatListSchema(HeartbeatSchema):
    incidents_count: int | None = Field(default=0)
    opened_incident_id: UUID | None = None


class HeartbeatPaginatedSchema(BasePaginatedSchema):
    data: list[HeartbeatListSchema]
