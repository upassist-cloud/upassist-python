from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SdkSetupSchema")


@_attrs_define
class SdkSetupSchema:
    """
    Attributes:
        dsn (str):
        python_snippet (str):
        javascript_snippet (str):
    """

    dsn: str
    python_snippet: str
    javascript_snippet: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dsn = self.dsn

        python_snippet = self.python_snippet

        javascript_snippet = self.javascript_snippet

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dsn": dsn,
                "python_snippet": python_snippet,
                "javascript_snippet": javascript_snippet,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dsn = d.pop("dsn")

        python_snippet = d.pop("python_snippet")

        javascript_snippet = d.pop("javascript_snippet")

        sdk_setup_schema = cls(
            dsn=dsn,
            python_snippet=python_snippet,
            javascript_snippet=javascript_snippet,
        )

        sdk_setup_schema.additional_properties = d
        return sdk_setup_schema

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
