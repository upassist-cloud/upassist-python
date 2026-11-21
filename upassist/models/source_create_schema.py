from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SourceCreateSchema")


@_attrs_define
class SourceCreateSchema:
    """
    Attributes:
        name (str):
        platform_id (UUID):
        group_id (None | Unset | UUID):
        logs_retention_days (int | Unset):  Default: 30.
        metrics_retention_days (int | Unset):  Default: 30.
        logs_pattern (str | Unset):  Default: '{host} {platform} {level} {nginx.status} {nginx.method} {nginx.host}
            {nginx.path} {nginx.client} {nginx.agent} {apache2.status} {apache2.method} {apache2.host} {apache2.path}
            {apache2.agent} {http.status} {http.method} {http.path} {http.client} {http.agent} {message}'.
    """

    name: str
    platform_id: UUID
    group_id: None | Unset | UUID = UNSET
    logs_retention_days: int | Unset = 30
    metrics_retention_days: int | Unset = 30
    logs_pattern: str | Unset = (
        "{host} {platform} {level} {nginx.status} {nginx.method} {nginx.host} {nginx.path} {nginx.client} {nginx.agent} {apache2.status} {apache2.method} {apache2.host} {apache2.path} {apache2.agent} {http.status} {http.method} {http.path} {http.client} {http.agent} {message}"
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        platform_id = str(self.platform_id)

        group_id: None | str | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        elif isinstance(self.group_id, UUID):
            group_id = str(self.group_id)
        else:
            group_id = self.group_id

        logs_retention_days = self.logs_retention_days

        metrics_retention_days = self.metrics_retention_days

        logs_pattern = self.logs_pattern

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "platform_id": platform_id,
            }
        )
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if logs_retention_days is not UNSET:
            field_dict["logs_retention_days"] = logs_retention_days
        if metrics_retention_days is not UNSET:
            field_dict["metrics_retention_days"] = metrics_retention_days
        if logs_pattern is not UNSET:
            field_dict["logs_pattern"] = logs_pattern

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        platform_id = UUID(d.pop("platform_id"))

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

        logs_retention_days = d.pop("logs_retention_days", UNSET)

        metrics_retention_days = d.pop("metrics_retention_days", UNSET)

        logs_pattern = d.pop("logs_pattern", UNSET)

        source_create_schema = cls(
            name=name,
            platform_id=platform_id,
            group_id=group_id,
            logs_retention_days=logs_retention_days,
            metrics_retention_days=metrics_retention_days,
            logs_pattern=logs_pattern,
        )

        source_create_schema.additional_properties = d
        return source_create_schema

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
