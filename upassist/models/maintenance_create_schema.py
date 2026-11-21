from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.maintenance_resource_create_schema import MaintenanceResourceCreateSchema


T = TypeVar("T", bound="MaintenanceCreateSchema")


@_attrs_define
class MaintenanceCreateSchema:
    """
    Attributes:
        name (str):
        started_at (datetime.datetime):
        finished_at (datetime.datetime):
        resources (list[MaintenanceResourceCreateSchema]):
        repeat (bool):
        description (None | str | Unset):
        status_pages_ids (list[UUID] | None | Unset):
        every_period (int | None | Unset):
        repeat_until (datetime.datetime | None | Unset):
    """

    name: str
    started_at: datetime.datetime
    finished_at: datetime.datetime
    resources: list[MaintenanceResourceCreateSchema]
    repeat: bool
    description: None | str | Unset = UNSET
    status_pages_ids: list[UUID] | None | Unset = UNSET
    every_period: int | None | Unset = UNSET
    repeat_until: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        started_at = self.started_at.isoformat()

        finished_at = self.finished_at.isoformat()

        resources = []
        for resources_item_data in self.resources:
            resources_item = resources_item_data.to_dict()
            resources.append(resources_item)

        repeat = self.repeat

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        status_pages_ids: list[str] | None | Unset
        if isinstance(self.status_pages_ids, Unset):
            status_pages_ids = UNSET
        elif isinstance(self.status_pages_ids, list):
            status_pages_ids = []
            for status_pages_ids_type_0_item_data in self.status_pages_ids:
                status_pages_ids_type_0_item = str(status_pages_ids_type_0_item_data)
                status_pages_ids.append(status_pages_ids_type_0_item)

        else:
            status_pages_ids = self.status_pages_ids

        every_period: int | None | Unset
        if isinstance(self.every_period, Unset):
            every_period = UNSET
        else:
            every_period = self.every_period

        repeat_until: None | str | Unset
        if isinstance(self.repeat_until, Unset):
            repeat_until = UNSET
        elif isinstance(self.repeat_until, datetime.datetime):
            repeat_until = self.repeat_until.isoformat()
        else:
            repeat_until = self.repeat_until

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "started_at": started_at,
                "finished_at": finished_at,
                "resources": resources,
                "repeat": repeat,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if status_pages_ids is not UNSET:
            field_dict["status_pages_ids"] = status_pages_ids
        if every_period is not UNSET:
            field_dict["every_period"] = every_period
        if repeat_until is not UNSET:
            field_dict["repeat_until"] = repeat_until

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.maintenance_resource_create_schema import MaintenanceResourceCreateSchema  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        started_at = datetime.datetime.fromisoformat(d.pop("started_at"))

        finished_at = datetime.datetime.fromisoformat(d.pop("finished_at"))

        resources = []
        _resources = d.pop("resources")
        for resources_item_data in _resources:
            resources_item = MaintenanceResourceCreateSchema.from_dict(resources_item_data)

            resources.append(resources_item)

        repeat = d.pop("repeat")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_status_pages_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                status_pages_ids_type_0 = []
                _status_pages_ids_type_0 = data
                for status_pages_ids_type_0_item_data in _status_pages_ids_type_0:
                    status_pages_ids_type_0_item = UUID(status_pages_ids_type_0_item_data)

                    status_pages_ids_type_0.append(status_pages_ids_type_0_item)

                return status_pages_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        status_pages_ids = _parse_status_pages_ids(d.pop("status_pages_ids", UNSET))

        def _parse_every_period(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        every_period = _parse_every_period(d.pop("every_period", UNSET))

        def _parse_repeat_until(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                repeat_until_type_0 = datetime.datetime.fromisoformat(data)

                return repeat_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        repeat_until = _parse_repeat_until(d.pop("repeat_until", UNSET))

        maintenance_create_schema = cls(
            name=name,
            started_at=started_at,
            finished_at=finished_at,
            resources=resources,
            repeat=repeat,
            description=description,
            status_pages_ids=status_pages_ids,
            every_period=every_period,
            repeat_until=repeat_until,
        )

        maintenance_create_schema.additional_properties = d
        return maintenance_create_schema

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
