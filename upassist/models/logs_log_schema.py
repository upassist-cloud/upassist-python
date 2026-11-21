from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.logs_log_schema_data_type_0 import LogsLogSchemaDataType0


T = TypeVar("T", bound="LogsLogSchema")


@_attrs_define
class LogsLogSchema:
    """
    Attributes:
        dt (datetime.datetime | None | Unset):
        host (None | str | Unset):
        message (None | str | Unset):
        file (None | str | Unset):
        data (LogsLogSchemaDataType0 | None | Unset):
    """

    dt: datetime.datetime | None | Unset = UNSET
    host: None | str | Unset = UNSET
    message: None | str | Unset = UNSET
    file: None | str | Unset = UNSET
    data: LogsLogSchemaDataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.logs_log_schema_data_type_0 import LogsLogSchemaDataType0  # noqa: PLC0415

        dt: None | str | Unset
        if isinstance(self.dt, Unset):
            dt = UNSET
        elif isinstance(self.dt, datetime.datetime):
            dt = self.dt.isoformat()
        else:
            dt = self.dt

        host: None | str | Unset
        if isinstance(self.host, Unset):
            host = UNSET
        else:
            host = self.host

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        file: None | str | Unset
        if isinstance(self.file, Unset):
            file = UNSET
        else:
            file = self.file

        data: dict[str, Any] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, LogsLogSchemaDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dt is not UNSET:
            field_dict["dt"] = dt
        if host is not UNSET:
            field_dict["host"] = host
        if message is not UNSET:
            field_dict["message"] = message
        if file is not UNSET:
            field_dict["file"] = file
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.logs_log_schema_data_type_0 import LogsLogSchemaDataType0  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_dt(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dt_type_0 = datetime.datetime.fromisoformat(data)

                return dt_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        dt = _parse_dt(d.pop("dt", UNSET))

        def _parse_host(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        host = _parse_host(d.pop("host", UNSET))

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_file(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file = _parse_file(d.pop("file", UNSET))

        def _parse_data(data: object) -> LogsLogSchemaDataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = LogsLogSchemaDataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LogsLogSchemaDataType0 | None | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        logs_log_schema = cls(
            dt=dt,
            host=host,
            message=message,
            file=file,
            data=data,
        )

        logs_log_schema.additional_properties = d
        return logs_log_schema

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
