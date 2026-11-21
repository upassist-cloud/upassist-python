from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.integration_update_schema_data import IntegrationUpdateSchemaData


T = TypeVar("T", bound="IntegrationUpdateSchema")


@_attrs_define
class IntegrationUpdateSchema:
    """
    Attributes:
        name (str):
        data (IntegrationUpdateSchemaData):
        is_active (bool | Unset):  Default: True.
    """

    name: str
    data: IntegrationUpdateSchemaData
    is_active: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        data = self.data.to_dict()

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "data": data,
            }
        )
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integration_update_schema_data import IntegrationUpdateSchemaData  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        data = IntegrationUpdateSchemaData.from_dict(d.pop("data"))

        is_active = d.pop("is_active", UNSET)

        integration_update_schema = cls(
            name=name,
            data=data,
            is_active=is_active,
        )

        integration_update_schema.additional_properties = d
        return integration_update_schema

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
