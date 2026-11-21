from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ErrorAppTestEventSchema")


@_attrs_define
class ErrorAppTestEventSchema:
    """
    Attributes:
        issue_id (None | Unset | UUID):
        event_id (None | Unset | UUID):
    """

    issue_id: None | Unset | UUID = UNSET
    event_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issue_id: None | str | Unset
        if isinstance(self.issue_id, Unset):
            issue_id = UNSET
        elif isinstance(self.issue_id, UUID):
            issue_id = str(self.issue_id)
        else:
            issue_id = self.issue_id

        event_id: None | str | Unset
        if isinstance(self.event_id, Unset):
            event_id = UNSET
        elif isinstance(self.event_id, UUID):
            event_id = str(self.event_id)
        else:
            event_id = self.event_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if issue_id is not UNSET:
            field_dict["issue_id"] = issue_id
        if event_id is not UNSET:
            field_dict["event_id"] = event_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_issue_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                issue_id_type_0 = UUID(data)

                return issue_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        issue_id = _parse_issue_id(d.pop("issue_id", UNSET))

        def _parse_event_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                event_id_type_0 = UUID(data)

                return event_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        event_id = _parse_event_id(d.pop("event_id", UNSET))

        error_app_test_event_schema = cls(
            issue_id=issue_id,
            event_id=event_id,
        )

        error_app_test_event_schema.additional_properties = d
        return error_app_test_event_schema

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
