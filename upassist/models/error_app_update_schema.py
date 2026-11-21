from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ErrorAppUpdateSchema")


@_attrs_define
class ErrorAppUpdateSchema:
    """
    Attributes:
        name (None | str | Unset):
        platform (None | str | Unset):
        group_id (None | Unset | UUID):
        events_retention_days (int | None | Unset):
        max_events (int | None | Unset):
        paused (bool | None | Unset):
        alerts_on (bool | None | Unset):
        alert_suppressed_environments (list[str] | None | Unset):
    """

    name: None | str | Unset = UNSET
    platform: None | str | Unset = UNSET
    group_id: None | Unset | UUID = UNSET
    events_retention_days: int | None | Unset = UNSET
    max_events: int | None | Unset = UNSET
    paused: bool | None | Unset = UNSET
    alerts_on: bool | None | Unset = UNSET
    alert_suppressed_environments: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        platform: None | str | Unset
        if isinstance(self.platform, Unset):
            platform = UNSET
        else:
            platform = self.platform

        group_id: None | str | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        elif isinstance(self.group_id, UUID):
            group_id = str(self.group_id)
        else:
            group_id = self.group_id

        events_retention_days: int | None | Unset
        if isinstance(self.events_retention_days, Unset):
            events_retention_days = UNSET
        else:
            events_retention_days = self.events_retention_days

        max_events: int | None | Unset
        if isinstance(self.max_events, Unset):
            max_events = UNSET
        else:
            max_events = self.max_events

        paused: bool | None | Unset
        if isinstance(self.paused, Unset):
            paused = UNSET
        else:
            paused = self.paused

        alerts_on: bool | None | Unset
        if isinstance(self.alerts_on, Unset):
            alerts_on = UNSET
        else:
            alerts_on = self.alerts_on

        alert_suppressed_environments: list[str] | None | Unset
        if isinstance(self.alert_suppressed_environments, Unset):
            alert_suppressed_environments = UNSET
        elif isinstance(self.alert_suppressed_environments, list):
            alert_suppressed_environments = self.alert_suppressed_environments

        else:
            alert_suppressed_environments = self.alert_suppressed_environments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if platform is not UNSET:
            field_dict["platform"] = platform
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if events_retention_days is not UNSET:
            field_dict["events_retention_days"] = events_retention_days
        if max_events is not UNSET:
            field_dict["max_events"] = max_events
        if paused is not UNSET:
            field_dict["paused"] = paused
        if alerts_on is not UNSET:
            field_dict["alerts_on"] = alerts_on
        if alert_suppressed_environments is not UNSET:
            field_dict["alert_suppressed_environments"] = alert_suppressed_environments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_platform(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        platform = _parse_platform(d.pop("platform", UNSET))

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

        def _parse_events_retention_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        events_retention_days = _parse_events_retention_days(d.pop("events_retention_days", UNSET))

        def _parse_max_events(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_events = _parse_max_events(d.pop("max_events", UNSET))

        def _parse_paused(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        paused = _parse_paused(d.pop("paused", UNSET))

        def _parse_alerts_on(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        alerts_on = _parse_alerts_on(d.pop("alerts_on", UNSET))

        def _parse_alert_suppressed_environments(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                alert_suppressed_environments_type_0 = cast(list[str], data)

                return alert_suppressed_environments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        alert_suppressed_environments = _parse_alert_suppressed_environments(
            d.pop("alert_suppressed_environments", UNSET)
        )

        error_app_update_schema = cls(
            name=name,
            platform=platform,
            group_id=group_id,
            events_retention_days=events_retention_days,
            max_events=max_events,
            paused=paused,
            alerts_on=alerts_on,
            alert_suppressed_environments=alert_suppressed_environments,
        )

        error_app_update_schema.additional_properties = d
        return error_app_update_schema

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
