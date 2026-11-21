from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.project_quota_schema import ProjectQuotaSchema


T = TypeVar("T", bound="ProjectPublicDetailSchema")


@_attrs_define
class ProjectPublicDetailSchema:
    """
    Attributes:
        id (UUID):
        name (str):
        is_paid (bool):
        tariff_name (str):
        quotas (ProjectQuotaSchema):
    """

    id: UUID
    name: str
    is_paid: bool
    tariff_name: str
    quotas: ProjectQuotaSchema
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        is_paid = self.is_paid

        tariff_name = self.tariff_name

        quotas = self.quotas.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "is_paid": is_paid,
                "tariff_name": tariff_name,
                "quotas": quotas,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_quota_schema import ProjectQuotaSchema  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        is_paid = d.pop("is_paid")

        tariff_name = d.pop("tariff_name")

        quotas = ProjectQuotaSchema.from_dict(d.pop("quotas"))

        project_public_detail_schema = cls(
            id=id,
            name=name,
            is_paid=is_paid,
            tariff_name=tariff_name,
            quotas=quotas,
        )

        project_public_detail_schema.additional_properties = d
        return project_public_detail_schema

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
