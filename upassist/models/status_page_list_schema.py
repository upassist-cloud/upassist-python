from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.status_page_status_schema import StatusPageStatusSchema


T = TypeVar("T", bound="StatusPageListSchema")


@_attrs_define
class StatusPageListSchema:
    """
    Attributes:
        id (UUID):
        name (str):
        subdomain (str):
        published (bool):
        password_on (bool):
        resources_count (int):
        status (StatusPageStatusSchema):
        group_id (None | Unset | UUID):
        custom_domain (None | str | Unset):
    """

    id: UUID
    name: str
    subdomain: str
    published: bool
    password_on: bool
    resources_count: int
    status: StatusPageStatusSchema
    group_id: None | Unset | UUID = UNSET
    custom_domain: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        subdomain = self.subdomain

        published = self.published

        password_on = self.password_on

        resources_count = self.resources_count

        status = self.status.to_dict()

        group_id: None | str | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        elif isinstance(self.group_id, UUID):
            group_id = str(self.group_id)
        else:
            group_id = self.group_id

        custom_domain: None | str | Unset
        if isinstance(self.custom_domain, Unset):
            custom_domain = UNSET
        else:
            custom_domain = self.custom_domain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "subdomain": subdomain,
                "published": published,
                "password_on": password_on,
                "resources_count": resources_count,
                "status": status,
            }
        )
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if custom_domain is not UNSET:
            field_dict["custom_domain"] = custom_domain

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.status_page_status_schema import StatusPageStatusSchema  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        subdomain = d.pop("subdomain")

        published = d.pop("published")

        password_on = d.pop("password_on")

        resources_count = d.pop("resources_count")

        status = StatusPageStatusSchema.from_dict(d.pop("status"))

        def _parse_group_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                group_id_type_0 = UUID(data)

                return group_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        group_id = _parse_group_id(d.pop("group_id", UNSET))

        def _parse_custom_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_domain = _parse_custom_domain(d.pop("custom_domain", UNSET))

        status_page_list_schema = cls(
            id=id,
            name=name,
            subdomain=subdomain,
            published=published,
            password_on=password_on,
            resources_count=resources_count,
            status=status,
            group_id=group_id,
            custom_domain=custom_domain,
        )

        status_page_list_schema.additional_properties = d
        return status_page_list_schema

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
