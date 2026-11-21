from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ErrorIssueUpdateSchema")


@_attrs_define
class ErrorIssueUpdateSchema:
    """
    Attributes:
        is_resolved (bool | None | Unset):
        is_muted (bool | None | Unset):
    """

    is_resolved: bool | None | Unset = UNSET
    is_muted: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_resolved: bool | None | Unset
        if isinstance(self.is_resolved, Unset):
            is_resolved = UNSET
        else:
            is_resolved = self.is_resolved

        is_muted: bool | None | Unset
        if isinstance(self.is_muted, Unset):
            is_muted = UNSET
        else:
            is_muted = self.is_muted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_resolved is not UNSET:
            field_dict["is_resolved"] = is_resolved
        if is_muted is not UNSET:
            field_dict["is_muted"] = is_muted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_is_resolved(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_resolved = _parse_is_resolved(d.pop("is_resolved", UNSET))

        def _parse_is_muted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_muted = _parse_is_muted(d.pop("is_muted", UNSET))

        error_issue_update_schema = cls(
            is_resolved=is_resolved,
            is_muted=is_muted,
        )

        error_issue_update_schema.additional_properties = d
        return error_issue_update_schema

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
