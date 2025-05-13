from datetime import date, datetime, time
from enum import Enum
from uuid import UUID

from pydantic import BaseModel, Field, NonNegativeInt, PositiveInt
from pydantic_extra_types.timezone_name import TimeZoneName

from upassist.schemas.base import BasePaginatedSchema, BaseSchema, UUIDSchema


class HeartbeatStatusEnum(str, Enum):
    """Enumeration of possible heartbeat statuses."""

    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"


class HeartbeatCreateSchema(BaseModel):
    """Schema for creating a new heartbeat.

    Attributes:
        name: Name of the heartbeat
        description: Optional description of the heartbeat
        group_id: Optional UUID of the group this heartbeat belongs to
        slug: Optional custom slug for the heartbeat
        fetch_interval: Interval in seconds between heartbeat checks (60-100000)
        confirmation_period: Time in seconds to wait before confirming an incident (0-100000)
        realert_period: Optional time in seconds before re-alerting about an incident
        alerts_on: Whether to send alerts on incidents
        paused: Whether the heartbeat is paused
        meta: Optional metadata dictionary
        call: Whether to make phone calls for alerts
        send_sms: Whether to send SMS alerts
        send_email: Whether to send email alerts
        send_push_notification: Whether to send push notifications
        maintenance_window_from: Optional start time for maintenance window
        maintenance_window_until: Optional end time for maintenance window
        maintenance_window_timezone: Timezone for maintenance window times
        alert_week_days: List of days (0-6) when alerts should be sent
    """

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
    maintenance_window_timezone: TimeZoneName = Field(default=TimeZoneName("Europe/Belfast"))
    alert_week_days: list[int] | None = Field(default_factory=lambda: [0, 1, 2, 3, 4, 5, 6])


class IncidentStatsSchema(BaseSchema):
    """Schema for incident statistics.

    Attributes:
        sum: Sum of incident durations
        avg: Average incident duration
        max: Maximum incident duration
        count: Number of incidents
        from_date: Start date of the statistics period
        to_date: End date of the statistics period
        from_datetime: Start datetime of the statistics period
        to_datetime: End datetime of the statistics period
        period_alias: Optional alias for the time period
        uptime_percents: Percentage of uptime during the period
    """

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
    """Base schema for heartbeat information.

    Attributes:
        name: Name of the heartbeat
        created_at: Creation timestamp
        slug: Unique identifier for the heartbeat
        group_id: Optional UUID of the group this heartbeat belongs to
        status: Current status of the heartbeat
        is_down: Whether the heartbeat is currently down
        last_up_at: Timestamp of last successful heartbeat
        last_down_at: Timestamp of last failure
        last_fetch_at: Timestamp of last check
        next_fetch_at: Timestamp of next scheduled check
        fetch_interval: Interval between checks in seconds
        confirmation_period: Time to wait before confirming incidents
        paused: Whether the heartbeat is paused
        alerts_on: Whether alerts are enabled
        call: Whether phone call alerts are enabled
        send_sms: Whether SMS alerts are enabled
        send_email: Whether email alerts are enabled
        send_push_notification: Whether push notifications are enabled
        maintenance_window_from: Start time of maintenance window
        maintenance_window_until: End time of maintenance window
        maintenance_window_timezone: Timezone for maintenance window
        alert_week_days: Days when alerts should be sent
    """

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
    maintenance_window_timezone: TimeZoneName = Field(default=TimeZoneName("Europe/Belfast"))
    alert_week_days: list[int] | None = None


class HeartbeatDetailSchema(HeartbeatSchema):
    """Schema for detailed heartbeat information.

    Additional attributes beyond HeartbeatSchema:
        description: Optional description of the heartbeat
        incidents_count: Number of incidents
        opened_incident_id: UUID of currently open incident if any
        confirmation_period: Time to wait before confirming incidents
        realert_period: Time before re-alerting about unresolved incidents
        meta: Optional metadata dictionary
        incident_stats: List of incident statistics
    """

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
    """Schema for heartbeat list items.

    Additional attributes beyond HeartbeatSchema:
        incidents_count: Number of incidents
        opened_incident_id: UUID of currently open incident if any
    """

    incidents_count: int | None = Field(default=0)
    opened_incident_id: UUID | None = None


class HeartbeatPaginatedSchema(BasePaginatedSchema):
    """Schema for paginated heartbeat list response.

    Attributes:
        data: List of HeartbeatListSchema items
    """

    data: list[HeartbeatListSchema]
