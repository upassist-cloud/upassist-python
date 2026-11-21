from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlatformListSchema")


@_attrs_define
class PlatformListSchema:
    """
    Attributes:
        id (UUID):
        name (str):
        icon (str):
        description (str):
        tags (list[str]):
        documentation_url (None | str | Unset):
    """

    id: UUID
    name: str
    icon: str
    description: str
    tags: list[str]
    documentation_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        icon = self.icon

        description = self.description

        tags = self.tags

        documentation_url: None | str | Unset
        if isinstance(self.documentation_url, Unset):
            documentation_url = UNSET
        else:
            documentation_url = self.documentation_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "icon": icon,
                "description": description,
                "tags": tags,
            }
        )
        if documentation_url is not UNSET:
            field_dict["documentation_url"] = documentation_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        icon = d.pop("icon")

        description = d.pop("description")

        tags = cast(list[str], d.pop("tags"))

        def _parse_documentation_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        documentation_url = _parse_documentation_url(d.pop("documentation_url", UNSET))

        platform_list_schema = cls(
            id=id,
            name=name,
            icon=icon,
            description=description,
            tags=tags,
            documentation_url=documentation_url,
        )

        platform_list_schema.additional_properties = d
        return platform_list_schema

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
