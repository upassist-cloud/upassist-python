from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProjectQuotaSchema")


@_attrs_define
class ProjectQuotaSchema:
    """
    Attributes:
        monitors_used (int):
        monitors_limit (int):
        heartbeats_used (int):
        heartbeats_limit (int):
        sites_used (int):
        sites_limit (int):
        members_limit (int):
    """

    monitors_used: int
    monitors_limit: int
    heartbeats_used: int
    heartbeats_limit: int
    sites_used: int
    sites_limit: int
    members_limit: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        monitors_used = self.monitors_used

        monitors_limit = self.monitors_limit

        heartbeats_used = self.heartbeats_used

        heartbeats_limit = self.heartbeats_limit

        sites_used = self.sites_used

        sites_limit = self.sites_limit

        members_limit = self.members_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "monitors_used": monitors_used,
                "monitors_limit": monitors_limit,
                "heartbeats_used": heartbeats_used,
                "heartbeats_limit": heartbeats_limit,
                "sites_used": sites_used,
                "sites_limit": sites_limit,
                "members_limit": members_limit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        monitors_used = d.pop("monitors_used")

        monitors_limit = d.pop("monitors_limit")

        heartbeats_used = d.pop("heartbeats_used")

        heartbeats_limit = d.pop("heartbeats_limit")

        sites_used = d.pop("sites_used")

        sites_limit = d.pop("sites_limit")

        members_limit = d.pop("members_limit")

        project_quota_schema = cls(
            monitors_used=monitors_used,
            monitors_limit=monitors_limit,
            heartbeats_used=heartbeats_used,
            heartbeats_limit=heartbeats_limit,
            sites_used=sites_used,
            sites_limit=sites_limit,
            members_limit=members_limit,
        )

        project_quota_schema.additional_properties = d
        return project_quota_schema

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
