from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.status_page_resource_list_schema import StatusPageResourceListSchema


T = TypeVar("T", bound="StatusPageSectionListDetailSchema")


@_attrs_define
class StatusPageSectionListDetailSchema:
    """
    Attributes:
        id (UUID):
        name (str):
        order (int):
        resources (list[StatusPageResourceListSchema]):
        text (None | str | Unset):
    """

    id: UUID
    name: str
    order: int
    resources: list[StatusPageResourceListSchema]
    text: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        order = self.order

        resources = []
        for resources_item_data in self.resources:
            resources_item = resources_item_data.to_dict()
            resources.append(resources_item)

        text: None | str | Unset
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "order": order,
                "resources": resources,
            }
        )
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.status_page_resource_list_schema import StatusPageResourceListSchema  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        order = d.pop("order")

        resources = []
        _resources = d.pop("resources")
        for resources_item_data in _resources:
            resources_item = StatusPageResourceListSchema.from_dict(resources_item_data)

            resources.append(resources_item)

        def _parse_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text = _parse_text(d.pop("text", UNSET))

        status_page_section_list_detail_schema = cls(
            id=id,
            name=name,
            order=order,
            resources=resources,
            text=text,
        )

        status_page_section_list_detail_schema.additional_properties = d
        return status_page_section_list_detail_schema

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
