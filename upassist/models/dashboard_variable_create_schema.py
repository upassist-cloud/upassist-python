from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dashboard_variable_type_enum import DashboardVariableTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="DashboardVariableCreateSchema")


@_attrs_define
class DashboardVariableCreateSchema:
    """
    Attributes:
        name (str):
        type_ (DashboardVariableTypeEnum):
        default_value (None | str | Unset):
        select_list (list[str] | None | Unset):
    """

    name: str
    type_: DashboardVariableTypeEnum
    default_value: None | str | Unset = UNSET
    select_list: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        default_value: None | str | Unset
        if isinstance(self.default_value, Unset):
            default_value = UNSET
        else:
            default_value = self.default_value

        select_list: list[str] | None | Unset
        if isinstance(self.select_list, Unset):
            select_list = UNSET
        elif isinstance(self.select_list, list):
            select_list = self.select_list

        else:
            select_list = self.select_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
            }
        )
        if default_value is not UNSET:
            field_dict["default_value"] = default_value
        if select_list is not UNSET:
            field_dict["select_list"] = select_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = DashboardVariableTypeEnum(d.pop("type"))

        def _parse_default_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_value = _parse_default_value(d.pop("default_value", UNSET))

        def _parse_select_list(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                select_list_type_0 = cast(list[str], data)

                return select_list_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        select_list = _parse_select_list(d.pop("select_list", UNSET))

        dashboard_variable_create_schema = cls(
            name=name,
            type_=type_,
            default_value=default_value,
            select_list=select_list,
        )

        dashboard_variable_create_schema.additional_properties = d
        return dashboard_variable_create_schema

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
