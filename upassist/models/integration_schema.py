from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.integration_source_enum import IntegrationSourceEnum

if TYPE_CHECKING:
    from ..models.integration_schema_data import IntegrationSchemaData


T = TypeVar("T", bound="IntegrationSchema")


@_attrs_define
class IntegrationSchema:
    """
    Attributes:
        id (UUID):
        name (str):
        source (IntegrationSourceEnum):
        data (IntegrationSchemaData):
        is_active (bool):
        created_at (datetime.datetime):
    """

    id: UUID
    name: str
    source: IntegrationSourceEnum
    data: IntegrationSchemaData
    is_active: bool
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        source = self.source.value

        data = self.data.to_dict()

        is_active = self.is_active

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "source": source,
                "data": data,
                "is_active": is_active,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integration_schema_data import IntegrationSchemaData  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        source = IntegrationSourceEnum(d.pop("source"))

        data = IntegrationSchemaData.from_dict(d.pop("data"))

        is_active = d.pop("is_active")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        integration_schema = cls(
            id=id,
            name=name,
            source=source,
            data=data,
            is_active=is_active,
            created_at=created_at,
        )

        integration_schema.additional_properties = d
        return integration_schema

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
