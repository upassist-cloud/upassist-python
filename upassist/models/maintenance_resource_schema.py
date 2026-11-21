from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.maintenance_resource_level import MaintenanceResourceLevel
from ..models.maintenance_resource_type_enum import MaintenanceResourceTypeEnum

T = TypeVar("T", bound="MaintenanceResourceSchema")


@_attrs_define
class MaintenanceResourceSchema:
    """
    Attributes:
        id (UUID):
        public_name (str):
        object_id (UUID):
        resource_type (MaintenanceResourceTypeEnum):
        level (MaintenanceResourceLevel):
    """

    id: UUID
    public_name: str
    object_id: UUID
    resource_type: MaintenanceResourceTypeEnum
    level: MaintenanceResourceLevel
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        public_name = self.public_name

        object_id = str(self.object_id)

        resource_type = self.resource_type.value

        level = self.level.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "public_name": public_name,
                "object_id": object_id,
                "resource_type": resource_type,
                "level": level,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        public_name = d.pop("public_name")

        object_id = UUID(d.pop("object_id"))

        resource_type = MaintenanceResourceTypeEnum(d.pop("resource_type"))

        level = MaintenanceResourceLevel(d.pop("level"))

        maintenance_resource_schema = cls(
            id=id,
            public_name=public_name,
            object_id=object_id,
            resource_type=resource_type,
            level=level,
        )

        maintenance_resource_schema.additional_properties = d
        return maintenance_resource_schema

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
