from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ErrorAppCreateSchema")


@_attrs_define
class ErrorAppCreateSchema:
    """
    Attributes:
        name (str):
        platform (str | Unset):  Default: 'python'.
        group_id (None | Unset | UUID):
        events_retention_days (int | Unset):  Default: 90.
        max_events (int | None | Unset):
    """

    name: str
    platform: str | Unset = "python"
    group_id: None | Unset | UUID = UNSET
    events_retention_days: int | Unset = 90
    max_events: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        platform = self.platform

        group_id: None | str | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        elif isinstance(self.group_id, UUID):
            group_id = str(self.group_id)
        else:
            group_id = self.group_id

        events_retention_days = self.events_retention_days

        max_events: int | None | Unset
        if isinstance(self.max_events, Unset):
            max_events = UNSET
        else:
            max_events = self.max_events

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if platform is not UNSET:
            field_dict["platform"] = platform
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if events_retention_days is not UNSET:
            field_dict["events_retention_days"] = events_retention_days
        if max_events is not UNSET:
            field_dict["max_events"] = max_events

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        platform = d.pop("platform", UNSET)

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

        events_retention_days = d.pop("events_retention_days", UNSET)

        def _parse_max_events(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_events = _parse_max_events(d.pop("max_events", UNSET))

        error_app_create_schema = cls(
            name=name,
            platform=platform,
            group_id=group_id,
            events_retention_days=events_retention_days,
            max_events=max_events,
        )

        error_app_create_schema.additional_properties = d
        return error_app_create_schema

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
