from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_key_scope_enum import APIKeyScopeEnum

T = TypeVar("T", bound="APIKeySchema")


@_attrs_define
class APIKeySchema:
    """
    Attributes:
        id (UUID):
        name (str):
        created_at (datetime.datetime):
        key (str):
        scopes (list[APIKeyScopeEnum]):
    """

    id: UUID
    name: str
    created_at: datetime.datetime
    key: str
    scopes: list[APIKeyScopeEnum]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        created_at = self.created_at.isoformat()

        key = self.key

        scopes = []
        for scopes_item_data in self.scopes:
            scopes_item = scopes_item_data.value
            scopes.append(scopes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "created_at": created_at,
                "key": key,
                "scopes": scopes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        key = d.pop("key")

        scopes = []
        _scopes = d.pop("scopes")
        for scopes_item_data in _scopes:
            scopes_item = APIKeyScopeEnum(scopes_item_data)

            scopes.append(scopes_item)

        api_key_schema = cls(
            id=id,
            name=name,
            created_at=created_at,
            key=key,
            scopes=scopes,
        )

        api_key_schema.additional_properties = d
        return api_key_schema

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
