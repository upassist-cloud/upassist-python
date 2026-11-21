from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.heartbeat_update_schema_meta_type_0 import HeartbeatUpdateSchemaMetaType0


T = TypeVar("T", bound="HeartbeatUpdateSchema")


@_attrs_define
class HeartbeatUpdateSchema:
    """
    Attributes:
        name (str):
        description (None | str | Unset):
        group_id (None | Unset | UUID):
        slug (None | str | Unset):
        fetch_interval (int | Unset):  Default: 180.
        confirmation_period (int | Unset): Time in seconds to wait until beat before starting incident Default: 0.
        realert_period (int | None | Unset): Time in seconds to notify users again about unresolved incident
        alerts_on (bool | Unset): Alerts on incident messages Default: True.
        paused (bool | Unset):  Default: False.
        meta (HeartbeatUpdateSchemaMetaType0 | None | Unset):
        call (bool | Unset):  Default: False.
        send_sms (bool | Unset):  Default: False.
        send_email (bool | Unset):  Default: True.
        send_push_notification (bool | Unset):  Default: False.
        maintenance_window_from (None | str | Unset):
        maintenance_window_until (None | str | Unset):
        maintenance_window_timezone (Any | Unset):  Default: 'Europe/Belfast'.
        alert_week_days (list[int] | None | Unset):
    """

    name: str
    description: None | str | Unset = UNSET
    group_id: None | Unset | UUID = UNSET
    slug: None | str | Unset = UNSET
    fetch_interval: int | Unset = 180
    confirmation_period: int | Unset = 0
    realert_period: int | None | Unset = UNSET
    alerts_on: bool | Unset = True
    paused: bool | Unset = False
    meta: HeartbeatUpdateSchemaMetaType0 | None | Unset = UNSET
    call: bool | Unset = False
    send_sms: bool | Unset = False
    send_email: bool | Unset = True
    send_push_notification: bool | Unset = False
    maintenance_window_from: None | str | Unset = UNSET
    maintenance_window_until: None | str | Unset = UNSET
    maintenance_window_timezone: Any | Unset = "Europe/Belfast"
    alert_week_days: list[int] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.heartbeat_update_schema_meta_type_0 import HeartbeatUpdateSchemaMetaType0  # noqa: PLC0415

        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        group_id: None | str | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        elif isinstance(self.group_id, UUID):
            group_id = str(self.group_id)
        else:
            group_id = self.group_id

        slug: None | str | Unset
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        fetch_interval = self.fetch_interval

        confirmation_period = self.confirmation_period

        realert_period: int | None | Unset
        if isinstance(self.realert_period, Unset):
            realert_period = UNSET
        else:
            realert_period = self.realert_period

        alerts_on = self.alerts_on

        paused = self.paused

        meta: dict[str, Any] | None | Unset
        if isinstance(self.meta, Unset):
            meta = UNSET
        elif isinstance(self.meta, HeartbeatUpdateSchemaMetaType0):
            meta = self.meta.to_dict()
        else:
            meta = self.meta

        call = self.call

        send_sms = self.send_sms

        send_email = self.send_email

        send_push_notification = self.send_push_notification

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
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if slug is not UNSET:
            field_dict["slug"] = slug
        if fetch_interval is not UNSET:
            field_dict["fetch_interval"] = fetch_interval
        if confirmation_period is not UNSET:
            field_dict["confirmation_period"] = confirmation_period
        if realert_period is not UNSET:
            field_dict["realert_period"] = realert_period
        if alerts_on is not UNSET:
            field_dict["alerts_on"] = alerts_on
        if paused is not UNSET:
            field_dict["paused"] = paused
        if meta is not UNSET:
            field_dict["meta"] = meta
        if call is not UNSET:
            field_dict["call"] = call
        if send_sms is not UNSET:
            field_dict["send_sms"] = send_sms
        if send_email is not UNSET:
            field_dict["send_email"] = send_email
        if send_push_notification is not UNSET:
            field_dict["send_push_notification"] = send_push_notification
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
        from ..models.heartbeat_update_schema_meta_type_0 import HeartbeatUpdateSchemaMetaType0  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

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

        def _parse_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        fetch_interval = d.pop("fetch_interval", UNSET)

        confirmation_period = d.pop("confirmation_period", UNSET)

        def _parse_realert_period(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        realert_period = _parse_realert_period(d.pop("realert_period", UNSET))

        alerts_on = d.pop("alerts_on", UNSET)

        paused = d.pop("paused", UNSET)

        def _parse_meta(data: object) -> HeartbeatUpdateSchemaMetaType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = HeartbeatUpdateSchemaMetaType0.from_dict(data)

                return meta_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HeartbeatUpdateSchemaMetaType0 | None | Unset, data)

        meta = _parse_meta(d.pop("meta", UNSET))

        call = d.pop("call", UNSET)

        send_sms = d.pop("send_sms", UNSET)

        send_email = d.pop("send_email", UNSET)

        send_push_notification = d.pop("send_push_notification", UNSET)

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

        heartbeat_update_schema = cls(
            name=name,
            description=description,
            group_id=group_id,
            slug=slug,
            fetch_interval=fetch_interval,
            confirmation_period=confirmation_period,
            realert_period=realert_period,
            alerts_on=alerts_on,
            paused=paused,
            meta=meta,
            call=call,
            send_sms=send_sms,
            send_email=send_email,
            send_push_notification=send_push_notification,
            maintenance_window_from=maintenance_window_from,
            maintenance_window_until=maintenance_window_until,
            maintenance_window_timezone=maintenance_window_timezone,
            alert_week_days=alert_week_days,
        )

        heartbeat_update_schema.additional_properties = d
        return heartbeat_update_schema

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
