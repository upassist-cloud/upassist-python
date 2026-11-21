from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.log_schema_data_type_1 import LogSchemaDataType1


T = TypeVar("T", bound="LogSchema")


@_attrs_define
class LogSchema:
    """
    Attributes:
        time (datetime.datetime):
        source_id (UUID):
        data (LogSchemaDataType1 | str):
    """

    time: datetime.datetime
    source_id: UUID
    data: LogSchemaDataType1 | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.log_schema_data_type_1 import LogSchemaDataType1  # noqa: PLC0415

        time = self.time.isoformat()

        source_id = str(self.source_id)

        data: dict[str, Any] | str
        if isinstance(self.data, LogSchemaDataType1):
            data = self.data.to_dict()
        else:
            data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "time": time,
                "source_id": source_id,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.log_schema_data_type_1 import LogSchemaDataType1  # noqa: PLC0415

        d = dict(src_dict)
        time = datetime.datetime.fromisoformat(d.pop("time"))

        source_id = UUID(d.pop("source_id"))

        def _parse_data(data: object) -> LogSchemaDataType1 | str:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_1 = LogSchemaDataType1.from_dict(data)

                return data_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LogSchemaDataType1 | str, data)

        data = _parse_data(d.pop("data"))

        log_schema = cls(
            time=time,
            source_id=source_id,
            data=data,
        )

        log_schema.additional_properties = d
        return log_schema

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
