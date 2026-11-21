from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.heartbeat_status_enum import HeartbeatStatusEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="HeartbeatSchema")


@_attrs_define
class HeartbeatSchema:
    """
    Attributes:
        id (UUID):
        name (str):
        created_at (datetime.datetime):
        slug (str):
        is_down (bool):
        fetch_interval (int):
        paused (bool):
        alerts_on (bool): Alerts on incident messages
        call (bool):
        send_sms (bool):
        send_email (bool):
        send_push_notification (bool):
        group_id (None | Unset | UUID):
        status (HeartbeatStatusEnum | None | Unset):
        last_up_at (datetime.datetime | None | Unset):
        last_down_at (datetime.datetime | None | Unset):
        last_fetch_at (datetime.datetime | None | Unset):
        next_fetch_at (datetime.datetime | None | Unset):
        confirmation_period (int | None | Unset):
        maintenance_window_from (None | str | Unset):
        maintenance_window_until (None | str | Unset):
        maintenance_window_timezone (Any | Unset):  Default: 'Europe/Belfast'.
        alert_week_days (list[int] | None | Unset):
    """

    id: UUID
    name: str
    created_at: datetime.datetime
    slug: str
    is_down: bool
    fetch_interval: int
    paused: bool
    alerts_on: bool
    call: bool
    send_sms: bool
    send_email: bool
    send_push_notification: bool
    group_id: None | Unset | UUID = UNSET
    status: HeartbeatStatusEnum | None | Unset = UNSET
    last_up_at: datetime.datetime | None | Unset = UNSET
    last_down_at: datetime.datetime | None | Unset = UNSET
    last_fetch_at: datetime.datetime | None | Unset = UNSET
    next_fetch_at: datetime.datetime | None | Unset = UNSET
    confirmation_period: int | None | Unset = UNSET
    maintenance_window_from: None | str | Unset = UNSET
    maintenance_window_until: None | str | Unset = UNSET
    maintenance_window_timezone: Any | Unset = "Europe/Belfast"
    alert_week_days: list[int] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        created_at = self.created_at.isoformat()

        slug = self.slug

        is_down = self.is_down

        fetch_interval = self.fetch_interval

        paused = self.paused

        alerts_on = self.alerts_on

        call = self.call

        send_sms = self.send_sms

        send_email = self.send_email

        send_push_notification = self.send_push_notification

        group_id: None | str | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        elif isinstance(self.group_id, UUID):
            group_id = str(self.group_id)
        else:
            group_id = self.group_id

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, HeartbeatStatusEnum):
            status = self.status.value
        else:
            status = self.status

        last_up_at: None | str | Unset
        if isinstance(self.last_up_at, Unset):
            last_up_at = UNSET
        elif isinstance(self.last_up_at, datetime.datetime):
            last_up_at = self.last_up_at.isoformat()
        else:
            last_up_at = self.last_up_at

        last_down_at: None | str | Unset
        if isinstance(self.last_down_at, Unset):
            last_down_at = UNSET
        elif isinstance(self.last_down_at, datetime.datetime):
            last_down_at = self.last_down_at.isoformat()
        else:
            last_down_at = self.last_down_at

        last_fetch_at: None | str | Unset
        if isinstance(self.last_fetch_at, Unset):
            last_fetch_at = UNSET
        elif isinstance(self.last_fetch_at, datetime.datetime):
            last_fetch_at = self.last_fetch_at.isoformat()
        else:
            last_fetch_at = self.last_fetch_at

        next_fetch_at: None | str | Unset
        if isinstance(self.next_fetch_at, Unset):
            next_fetch_at = UNSET
        elif isinstance(self.next_fetch_at, datetime.datetime):
            next_fetch_at = self.next_fetch_at.isoformat()
        else:
            next_fetch_at = self.next_fetch_at

        confirmation_period: int | None | Unset
        if isinstance(self.confirmation_period, Unset):
            confirmation_period = UNSET
        else:
            confirmation_period = self.confirmation_period

        maintenance_window_from: None | str | Unset
        if isinstance(self.maintenance_window_from, Unset):
            maintenance_window_from = UNSET
        else:
            maintenance_window_from = self.maintenance_window_from

        maintenance_window_until: None | str | Unset
        if isinstance(self.maintenance_window_until, Unset):
            maintenance_window_until = UNSET
        else:
            maintenance_window_until = self.maintenance_window_until

        maintenance_window_timezone = self.maintenance_window_timezone

        alert_week_days: list[int] | None | Unset
        if isinstance(self.alert_week_days, Unset):
            alert_week_days = UNSET
        elif isinstance(self.alert_week_days, list):
            alert_week_days = self.alert_week_days

        else:
            alert_week_days = self.alert_week_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "created_at": created_at,
                "slug": slug,
                "is_down": is_down,
                "fetch_interval": fetch_interval,
                "paused": paused,
                "alerts_on": alerts_on,
                "call": call,
                "send_sms": send_sms,
                "send_email": send_email,
                "send_push_notification": send_push_notification,
            }
        )
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if status is not UNSET:
            field_dict["status"] = status
        if last_up_at is not UNSET:
            field_dict["last_up_at"] = last_up_at
        if last_down_at is not UNSET:
            field_dict["last_down_at"] = last_down_at
        if last_fetch_at is not UNSET:
            field_dict["last_fetch_at"] = last_fetch_at
        if next_fetch_at is not UNSET:
            field_dict["next_fetch_at"] = next_fetch_at
        if confirmation_period is not UNSET:
            field_dict["confirmation_period"] = confirmation_period
        if maintenance_window_from is not UNSET:
            field_dict["maintenance_window_from"] = maintenance_window_from
        if maintenance_window_until is not UNSET:
            field_dict["maintenance_window_until"] = maintenance_window_until
        if maintenance_window_timezone is not UNSET:
            field_dict["maintenance_window_timezone"] = maintenance_window_timezone
        if alert_week_days is not UNSET:
            field_dict["alert_week_days"] = alert_week_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        slug = d.pop("slug")

        is_down = d.pop("is_down")

        fetch_interval = d.pop("fetch_interval")

        paused = d.pop("paused")

        alerts_on = d.pop("alerts_on")

        call = d.pop("call")

        send_sms = d.pop("send_sms")

        send_email = d.pop("send_email")

        send_push_notification = d.pop("send_push_notification")

        def _parse_group_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                group_id_type_0 = UUID(data)

                return group_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        group_id = _parse_group_id(d.pop("group_id", UNSET))

        def _parse_status(data: object) -> HeartbeatStatusEnum | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = HeartbeatStatusEnum(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HeartbeatStatusEnum | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_last_up_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_up_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_up_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_up_at = _parse_last_up_at(d.pop("last_up_at", UNSET))

        def _parse_last_down_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_down_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_down_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_down_at = _parse_last_down_at(d.pop("last_down_at", UNSET))

        def _parse_last_fetch_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_fetch_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_fetch_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_fetch_at = _parse_last_fetch_at(d.pop("last_fetch_at", UNSET))

        def _parse_next_fetch_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_fetch_at_type_0 = datetime.datetime.fromisoformat(data)

                return next_fetch_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        next_fetch_at = _parse_next_fetch_at(d.pop("next_fetch_at", UNSET))

        def _parse_confirmation_period(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        confirmation_period = _parse_confirmation_period(d.pop("confirmation_period", UNSET))

        def _parse_maintenance_window_from(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        maintenance_window_from = _parse_maintenance_window_from(d.pop("maintenance_window_from", UNSET))

        def _parse_maintenance_window_until(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        maintenance_window_until = _parse_maintenance_window_until(d.pop("maintenance_window_until", UNSET))

        maintenance_window_timezone = d.pop("maintenance_window_timezone", UNSET)

        def _parse_alert_week_days(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                alert_week_days_type_0 = cast(list[int], data)

                return alert_week_days_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        alert_week_days = _parse_alert_week_days(d.pop("alert_week_days", UNSET))

        heartbeat_schema = cls(
            id=id,
            name=name,
            created_at=created_at,
            slug=slug,
            is_down=is_down,
            fetch_interval=fetch_interval,
            paused=paused,
            alerts_on=alerts_on,
            call=call,
            send_sms=send_sms,
            send_email=send_email,
            send_push_notification=send_push_notification,
            group_id=group_id,
            status=status,
            last_up_at=last_up_at,
            last_down_at=last_down_at,
            last_fetch_at=last_fetch_at,
            next_fetch_at=next_fetch_at,
            confirmation_period=confirmation_period,
            maintenance_window_from=maintenance_window_from,
            maintenance_window_until=maintenance_window_until,
            maintenance_window_timezone=maintenance_window_timezone,
            alert_week_days=alert_week_days,
        )

        heartbeat_schema.additional_properties = d
        return heartbeat_schema

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
