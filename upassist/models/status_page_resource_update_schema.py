from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.resource_type_enum import ResourceTypeEnum
from ..models.resource_widget_enum import ResourceWidgetEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusPageResourceUpdateSchema")


@_attrs_define
class StatusPageResourceUpdateSchema:
    """
    Attributes:
        public_name (str):
        object_id (UUID):
        resource_type (ResourceTypeEnum):
        widget_type (ResourceWidgetEnum):
        id (None | Unset | UUID):
        order (int | Unset):  Default: 0.
        description (None | str | Unset):
    """

    public_name: str
    object_id: UUID
    resource_type: ResourceTypeEnum
    widget_type: ResourceWidgetEnum
    id: None | Unset | UUID = UNSET
    order: int | Unset = 0
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        public_name = self.public_name

        object_id = str(self.object_id)

        resource_type = self.resource_type.value

        widget_type = self.widget_type.value

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

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
        if id is not UNSET:
            field_dict["id"] = id
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

        def _parse_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        id = _parse_id(d.pop("id", UNSET))

        order = d.pop("order", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        status_page_resource_update_schema = cls(
            public_name=public_name,
            object_id=object_id,
            resource_type=resource_type,
            widget_type=widget_type,
            id=id,
            order=order,
            description=description,
        )

        status_page_resource_update_schema.additional_properties = d
        return status_page_resource_update_schema

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
