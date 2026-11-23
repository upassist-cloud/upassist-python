from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.incident_create_schema_meta_type_0 import IncidentCreateSchemaMetaType0


T = TypeVar("T", bound="IncidentCreateSchema")


@_attrs_define
class IncidentCreateSchema:
    """
    Attributes:
        name (str): Incident title or summary
        cause (str): Root cause or description of the incident
        started_at (datetime.datetime | None | Unset): Start time (UTC). Defaults to current time if omitted.
        severity (None | str | Unset): Optional severity indicator (e.g. critical, major, minor, warning)
        meta (IncidentCreateSchemaMetaType0 | None | Unset): Arbitrary custom metadata dictionary
        send_alert (bool | Unset): Whether to dispatch alert notifications to project integrations Default: True.
        monitor_id (None | Unset | UUID): Optional associated monitor ID
        heartbeat_id (None | Unset | UUID): Optional associated heartbeat ID
        site_alert_id (None | Unset | UUID): Optional associated site alert ID
    """

    name: str
    cause: str
    started_at: datetime.datetime | None | Unset = UNSET
    severity: None | str | Unset = UNSET
    meta: IncidentCreateSchemaMetaType0 | None | Unset = UNSET
    send_alert: bool | Unset = True
    monitor_id: None | Unset | UUID = UNSET
    heartbeat_id: None | Unset | UUID = UNSET
    site_alert_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.incident_create_schema_meta_type_0 import IncidentCreateSchemaMetaType0  # noqa: PLC0415

        name = self.name

        cause = self.cause

        started_at: None | str | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        elif isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        severity: None | str | Unset
        if isinstance(self.severity, Unset):
            severity = UNSET
        else:
            severity = self.severity

        meta: dict[str, Any] | None | Unset
        if isinstance(self.meta, Unset):
            meta = UNSET
        elif isinstance(self.meta, IncidentCreateSchemaMetaType0):
            meta = self.meta.to_dict()
        else:
            meta = self.meta

        send_alert = self.send_alert

        monitor_id: None | str | Unset
        if isinstance(self.monitor_id, Unset):
            monitor_id = UNSET
        elif isinstance(self.monitor_id, UUID):
            monitor_id = str(self.monitor_id)
        else:
            monitor_id = self.monitor_id

        heartbeat_id: None | str | Unset
        if isinstance(self.heartbeat_id, Unset):
            heartbeat_id = UNSET
        elif isinstance(self.heartbeat_id, UUID):
            heartbeat_id = str(self.heartbeat_id)
        else:
            heartbeat_id = self.heartbeat_id

        site_alert_id: None | str | Unset
        if isinstance(self.site_alert_id, Unset):
            site_alert_id = UNSET
        elif isinstance(self.site_alert_id, UUID):
            site_alert_id = str(self.site_alert_id)
        else:
            site_alert_id = self.site_alert_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "cause": cause,
            }
        )
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if severity is not UNSET:
            field_dict["severity"] = severity
        if meta is not UNSET:
            field_dict["meta"] = meta
        if send_alert is not UNSET:
            field_dict["send_alert"] = send_alert
        if monitor_id is not UNSET:
            field_dict["monitor_id"] = monitor_id
        if heartbeat_id is not UNSET:
            field_dict["heartbeat_id"] = heartbeat_id
        if site_alert_id is not UNSET:
            field_dict["site_alert_id"] = site_alert_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.incident_create_schema_meta_type_0 import IncidentCreateSchemaMetaType0  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        cause = d.pop("cause")

        def _parse_started_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = datetime.datetime.fromisoformat(data)

                return started_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))

        def _parse_severity(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        severity = _parse_severity(d.pop("severity", UNSET))

        def _parse_meta(data: object) -> IncidentCreateSchemaMetaType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = IncidentCreateSchemaMetaType0.from_dict(data)

                return meta_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IncidentCreateSchemaMetaType0 | None | Unset, data)

        meta = _parse_meta(d.pop("meta", UNSET))

        send_alert = d.pop("send_alert", UNSET)

        def _parse_monitor_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                monitor_id_type_0 = UUID(data)

                return monitor_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        monitor_id = _parse_monitor_id(d.pop("monitor_id", UNSET))

        def _parse_heartbeat_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                heartbeat_id_type_0 = UUID(data)

                return heartbeat_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        heartbeat_id = _parse_heartbeat_id(d.pop("heartbeat_id", UNSET))

        def _parse_site_alert_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                site_alert_id_type_0 = UUID(data)

                return site_alert_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        site_alert_id = _parse_site_alert_id(d.pop("site_alert_id", UNSET))

        incident_create_schema = cls(
            name=name,
            cause=cause,
            started_at=started_at,
            severity=severity,
            meta=meta,
            send_alert=send_alert,
            monitor_id=monitor_id,
            heartbeat_id=heartbeat_id,
            site_alert_id=site_alert_id,
        )

        incident_create_schema.additional_properties = d
        return incident_create_schema

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
