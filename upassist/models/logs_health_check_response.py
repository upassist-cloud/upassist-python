from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LogsHealthCheckResponse")


@_attrs_define
class LogsHealthCheckResponse:
    """
    Attributes:
        status (str):
        timestamp (datetime.datetime):
        service (str):
        version (str):
    """

    status: str
    timestamp: datetime.datetime
    service: str
    version: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        timestamp = self.timestamp.isoformat()

        service = self.service

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "timestamp": timestamp,
                "service": service,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status")

        timestamp = datetime.datetime.fromisoformat(d.pop("timestamp"))

        service = d.pop("service")

        version = d.pop("version")

        logs_health_check_response = cls(
            status=status,
            timestamp=timestamp,
            service=service,
            version=version,
        )

        logs_health_check_response.additional_properties = d
        return logs_health_check_response

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
