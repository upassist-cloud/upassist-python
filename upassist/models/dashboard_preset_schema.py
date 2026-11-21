from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dashboard_preset_schema_values import DashboardPresetSchemaValues


T = TypeVar("T", bound="DashboardPresetSchema")


@_attrs_define
class DashboardPresetSchema:
    """
    Attributes:
        id (UUID):
        name (str):
        values (DashboardPresetSchemaValues):
    """

    id: UUID
    name: str
    values: DashboardPresetSchemaValues
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        values = self.values.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_preset_schema_values import DashboardPresetSchemaValues  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        values = DashboardPresetSchemaValues.from_dict(d.pop("values"))

        dashboard_preset_schema = cls(
            id=id,
            name=name,
            values=values,
        )

        dashboard_preset_schema.additional_properties = d
        return dashboard_preset_schema

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
