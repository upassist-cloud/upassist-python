from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.resource_type_enum import ResourceTypeEnum
from ..models.resource_widget_enum import ResourceWidgetEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusPageResourceCreateSchema")


@_attrs_define
class StatusPageResourceCreateSchema:
    """
    Attributes:
        public_name (str):
        object_id (UUID):
        resource_type (ResourceTypeEnum):
        widget_type (ResourceWidgetEnum):
        order (int | Unset):  Default: 0.
        description (None | str | Unset):
    """

    public_name: str
    object_id: UUID
    resource_type: ResourceTypeEnum
    widget_type: ResourceWidgetEnum
    order: int | Unset = 0
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        public_name = self.public_name

        object_id = str(self.object_id)

        resource_type = self.resource_type.value

        widget_type = self.widget_type.value

        order = self.order

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "public_name": public_name,
                "object_id": object_id,
                "resource_type": resource_type,
                "widget_type": widget_type,
            }
        )
        if order is not UNSET:
            field_dict["order"] = order
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        public_name = d.pop("public_name")

        object_id = UUID(d.pop("object_id"))

        resource_type = ResourceTypeEnum(d.pop("resource_type"))

        widget_type = ResourceWidgetEnum(d.pop("widget_type"))

        order = d.pop("order", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        status_page_resource_create_schema = cls(
            public_name=public_name,
            object_id=object_id,
            resource_type=resource_type,
            widget_type=widget_type,
            order=order,
            description=description,
        )

        status_page_resource_create_schema.additional_properties = d
        return status_page_resource_create_schema

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
