from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.log_filter_operator_enum import LogFilterOperatorEnum
from ..models.log_filter_type_enum import LogFilterTypeEnum

T = TypeVar("T", bound="LogFilterConditionSchema")


@_attrs_define
class LogFilterConditionSchema:
    """
    Attributes:
        type_ (LogFilterTypeEnum):
        field (str):
        operator (LogFilterOperatorEnum):
        value (str):
    """

    type_: LogFilterTypeEnum
    field: str
    operator: LogFilterOperatorEnum
    value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        field = self.field

        operator = self.operator.value

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "field": field,
                "operator": operator,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = LogFilterTypeEnum(d.pop("type"))

        field = d.pop("field")

        operator = LogFilterOperatorEnum(d.pop("operator"))

        value = d.pop("value")

        log_filter_condition_schema = cls(
            type_=type_,
            field=field,
            operator=operator,
            value=value,
        )

        log_filter_condition_schema.additional_properties = d
        return log_filter_condition_schema

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
