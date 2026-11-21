from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.monitor_type_enum import MonitorTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="MonitorPublicSchema")


@_attrs_define
class MonitorPublicSchema:
    """
    Attributes:
        id (UUID):
        uri (str):
        name (str):
        monitor_type (MonitorTypeEnum):
        paused (bool):
        fetch_interval (int):
        alerts_on (bool):
        created_at (datetime.datetime):
        group_id (None | Unset | UUID):
        timeout (int | None | Unset):
        description (None | str | Unset):
        is_down (bool | None | Unset):
        is_verified (bool | None | Unset):
        last_fetch_at (datetime.datetime | None | Unset):
        last_down_at (datetime.datetime | None | Unset):
        last_up_time (datetime.datetime | None | Unset):
        incidents_count (int | None | Unset):
        opened_incident_id (None | Unset | UUID):
    """

    id: UUID
    uri: str
    name: str
    monitor_type: MonitorTypeEnum
    paused: bool
    fetch_interval: int
    alerts_on: bool
    created_at: datetime.datetime
    group_id: None | Unset | UUID = UNSET
    timeout: int | None | Unset = UNSET
    description: None | str | Unset = UNSET
    is_down: bool | None | Unset = UNSET
    is_verified: bool | None | Unset = UNSET
    last_fetch_at: datetime.datetime | None | Unset = UNSET
    last_down_at: datetime.datetime | None | Unset = UNSET
    last_up_time: datetime.datetime | None | Unset = UNSET
    incidents_count: int | None | Unset = UNSET
    opened_incident_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        uri = self.uri

        name = self.name

        monitor_type = self.monitor_type.value

        paused = self.paused

        fetch_interval = self.fetch_interval

        alerts_on = self.alerts_on

        created_at = self.created_at.isoformat()

        group_id: None | str | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        elif isinstance(self.group_id, UUID):
            group_id = str(self.group_id)
        else:
            group_id = self.group_id

        timeout: int | None | Unset
        if isinstance(self.timeout, Unset):
            timeout = UNSET
        else:
            timeout = self.timeout

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        is_down: bool | None | Unset
        if isinstance(self.is_down, Unset):
            is_down = UNSET
        else:
            is_down = self.is_down

        is_verified: bool | None | Unset
        if isinstance(self.is_verified, Unset):
            is_verified = UNSET
        else:
            is_verified = self.is_verified

        last_fetch_at: None | str | Unset
        if isinstance(self.last_fetch_at, Unset):
            last_fetch_at = UNSET
        elif isinstance(self.last_fetch_at, datetime.datetime):
            last_fetch_at = self.last_fetch_at.isoformat()
        else:
            last_fetch_at = self.last_fetch_at

        last_down_at: None | str | Unset
        if isinstance(self.last_down_at, Unset):
            last_down_at = UNSET
        elif isinstance(self.last_down_at, datetime.datetime):
            last_down_at = self.last_down_at.isoformat()
        else:
            last_down_at = self.last_down_at

        last_up_time: None | str | Unset
        if isinstance(self.last_up_time, Unset):
            last_up_time = UNSET
        elif isinstance(self.last_up_time, datetime.datetime):
            last_up_time = self.last_up_time.isoformat()
        else:
            last_up_time = self.last_up_time

        incidents_count: int | None | Unset
        if isinstance(self.incidents_count, Unset):
            incidents_count = UNSET
        else:
            incidents_count = self.incidents_count

        opened_incident_id: None | str | Unset
        if isinstance(self.opened_incident_id, Unset):
            opened_incident_id = UNSET
        elif isinstance(self.opened_incident_id, UUID):
            opened_incident_id = str(self.opened_incident_id)
        else:
            opened_incident_id = self.opened_incident_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "uri": uri,
                "name": name,
                "monitor_type": monitor_type,
                "paused": paused,
                "fetch_interval": fetch_interval,
                "alerts_on": alerts_on,
                "created_at": created_at,
            }
        )
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if description is not UNSET:
            field_dict["description"] = description
        if is_down is not UNSET:
            field_dict["is_down"] = is_down
        if is_verified is not UNSET:
            field_dict["is_verified"] = is_verified
        if last_fetch_at is not UNSET:
            field_dict["last_fetch_at"] = last_fetch_at
        if last_down_at is not UNSET:
            field_dict["last_down_at"] = last_down_at
        if last_up_time is not UNSET:
            field_dict["last_up_time"] = last_up_time
        if incidents_count is not UNSET:
            field_dict["incidents_count"] = incidents_count
        if opened_incident_id is not UNSET:
            field_dict["opened_incident_id"] = opened_incident_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        uri = d.pop("uri")

        name = d.pop("name")

        monitor_type = MonitorTypeEnum(d.pop("monitor_type"))

        paused = d.pop("paused")

        fetch_interval = d.pop("fetch_interval")

        alerts_on = d.pop("alerts_on")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

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

        def _parse_timeout(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        timeout = _parse_timeout(d.pop("timeout", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_is_down(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_down = _parse_is_down(d.pop("is_down", UNSET))

        def _parse_is_verified(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_verified = _parse_is_verified(d.pop("is_verified", UNSET))

        def _parse_last_fetch_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_fetch_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_fetch_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_fetch_at = _parse_last_fetch_at(d.pop("last_fetch_at", UNSET))

        def _parse_last_down_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_down_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_down_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_down_at = _parse_last_down_at(d.pop("last_down_at", UNSET))

        def _parse_last_up_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_up_time_type_0 = datetime.datetime.fromisoformat(data)

                return last_up_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_up_time = _parse_last_up_time(d.pop("last_up_time", UNSET))

        def _parse_incidents_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        incidents_count = _parse_incidents_count(d.pop("incidents_count", UNSET))

        def _parse_opened_incident_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                opened_incident_id_type_0 = UUID(data)

                return opened_incident_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        opened_incident_id = _parse_opened_incident_id(d.pop("opened_incident_id", UNSET))

        monitor_public_schema = cls(
            id=id,
            uri=uri,
            name=name,
            monitor_type=monitor_type,
            paused=paused,
            fetch_interval=fetch_interval,
            alerts_on=alerts_on,
            created_at=created_at,
            group_id=group_id,
            timeout=timeout,
            description=description,
            is_down=is_down,
            is_verified=is_verified,
            last_fetch_at=last_fetch_at,
            last_down_at=last_down_at,
            last_up_time=last_up_time,
            incidents_count=incidents_count,
            opened_incident_id=opened_incident_id,
        )

        monitor_public_schema.additional_properties = d
        return monitor_public_schema

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
