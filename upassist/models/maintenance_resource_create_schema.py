from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.maintenance_resource_level import MaintenanceResourceLevel
from ..models.maintenance_resource_type_enum import MaintenanceResourceTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="MaintenanceResourceCreateSchema")


@_attrs_define
class MaintenanceResourceCreateSchema:
    """
    Attributes:
        public_name (str):
        object_id (UUID):
        resource_type (MaintenanceResourceTypeEnum):
        level (MaintenanceResourceLevel | Unset):
    """

    public_name: str
    object_id: UUID
    resource_type: MaintenanceResourceTypeEnum
    level: MaintenanceResourceLevel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        public_name = self.public_name

        object_id = str(self.object_id)

        resource_type = self.resource_type.value

        level: str | Unset = UNSET
        if not isinstance(self.level, Unset):
            level = self.level.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "public_name": public_name,
                "object_id": object_id,
                "resource_type": resource_type,
            }
        )
        if level is not UNSET:
            field_dict["level"] = level

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        public_name = d.pop("public_name")

        object_id = UUID(d.pop("object_id"))

        resource_type = MaintenanceResourceTypeEnum(d.pop("resource_type"))

        _level = d.pop("level", UNSET)
        level: MaintenanceResourceLevel | Unset
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = MaintenanceResourceLevel(_level)

        maintenance_resource_create_schema = cls(
            public_name=public_name,
            object_id=object_id,
            resource_type=resource_type,
            level=level,
        )

        maintenance_resource_create_schema.additional_properties = d
        return maintenance_resource_create_schema

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
