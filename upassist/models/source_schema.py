from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SourceSchema")


@_attrs_define
class SourceSchema:
    """
    Attributes:
        id (UUID):
        name (str):
        logs_retention_days (int):
        metrics_retention_days (int):
        group_id (None | Unset | UUID):
        default_dashboard_id (None | Unset | UUID):
    """

    id: UUID
    name: str
    logs_retention_days: int
    metrics_retention_days: int
    group_id: None | Unset | UUID = UNSET
    default_dashboard_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        logs_retention_days = self.logs_retention_days

        metrics_retention_days = self.metrics_retention_days

        group_id: None | str | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        elif isinstance(self.group_id, UUID):
            group_id = str(self.group_id)
        else:
            group_id = self.group_id

        default_dashboard_id: None | str | Unset
        if isinstance(self.default_dashboard_id, Unset):
            default_dashboard_id = UNSET
        elif isinstance(self.default_dashboard_id, UUID):
            default_dashboard_id = str(self.default_dashboard_id)
        else:
            default_dashboard_id = self.default_dashboard_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "logs_retention_days": logs_retention_days,
                "metrics_retention_days": metrics_retention_days,
            }
        )
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if default_dashboard_id is not UNSET:
            field_dict["default_dashboard_id"] = default_dashboard_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        logs_retention_days = d.pop("logs_retention_days")

        metrics_retention_days = d.pop("metrics_retention_days")

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

        def _parse_default_dashboard_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                default_dashboard_id_type_0 = UUID(data)

                return default_dashboard_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        default_dashboard_id = _parse_default_dashboard_id(d.pop("default_dashboard_id", UNSET))

        source_schema = cls(
            id=id,
            name=name,
            logs_retention_days=logs_retention_days,
            metrics_retention_days=metrics_retention_days,
            group_id=group_id,
            default_dashboard_id=default_dashboard_id,
        )

        source_schema.additional_properties = d
        return source_schema

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
