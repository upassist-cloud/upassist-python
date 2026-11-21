from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.status_page_resource_create_schema import StatusPageResourceCreateSchema


T = TypeVar("T", bound="StatusPageSectionCreateSchema")


@_attrs_define
class StatusPageSectionCreateSchema:
    """
    Attributes:
        name (str):
        resources (list[StatusPageResourceCreateSchema]):
        order (int | Unset):  Default: 0.
    """

    name: str
    resources: list[StatusPageResourceCreateSchema]
    order: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        resources = []
        for resources_item_data in self.resources:
            resources_item = resources_item_data.to_dict()
            resources.append(resources_item)

        order = self.order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "resources": resources,
            }
        )
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.status_page_resource_create_schema import StatusPageResourceCreateSchema  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        resources = []
        _resources = d.pop("resources")
        for resources_item_data in _resources:
            resources_item = StatusPageResourceCreateSchema.from_dict(resources_item_data)

            resources.append(resources_item)

        order = d.pop("order", UNSET)

        status_page_section_create_schema = cls(
            name=name,
            resources=resources,
            order=order,
        )

        status_page_section_create_schema.additional_properties = d
        return status_page_section_create_schema

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
