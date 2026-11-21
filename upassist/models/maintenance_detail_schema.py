from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.maintenance_detail_status_page_schema import MaintenanceDetailStatusPageSchema
    from ..models.maintenance_resource_schema import MaintenanceResourceSchema


T = TypeVar("T", bound="MaintenanceDetailSchema")


@_attrs_define
class MaintenanceDetailSchema:
    """
    Attributes:
        id (UUID):
        name (str):
        started_at (datetime.datetime):
        finished_at (datetime.datetime):
        resources (list[MaintenanceResourceSchema]):
        status_pages (list[MaintenanceDetailStatusPageSchema]):
        description (None | str | Unset):
        resources_count (int | Unset):  Default: 0.
    """

    id: UUID
    name: str
    started_at: datetime.datetime
    finished_at: datetime.datetime
    resources: list[MaintenanceResourceSchema]
    status_pages: list[MaintenanceDetailStatusPageSchema]
    description: None | str | Unset = UNSET
    resources_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        started_at = self.started_at.isoformat()

        finished_at = self.finished_at.isoformat()

        resources = []
        for resources_item_data in self.resources:
            resources_item = resources_item_data.to_dict()
            resources.append(resources_item)

        status_pages = []
        for status_pages_item_data in self.status_pages:
            status_pages_item = status_pages_item_data.to_dict()
            status_pages.append(status_pages_item)

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        resources_count = self.resources_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "started_at": started_at,
                "finished_at": finished_at,
                "resources": resources,
                "status_pages": status_pages,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if resources_count is not UNSET:
            field_dict["resources_count"] = resources_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.maintenance_detail_status_page_schema import MaintenanceDetailStatusPageSchema  # noqa: PLC0415
        from ..models.maintenance_resource_schema import MaintenanceResourceSchema  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        started_at = datetime.datetime.fromisoformat(d.pop("started_at"))

        finished_at = datetime.datetime.fromisoformat(d.pop("finished_at"))

        resources = []
        _resources = d.pop("resources")
        for resources_item_data in _resources:
            resources_item = MaintenanceResourceSchema.from_dict(resources_item_data)

            resources.append(resources_item)

        status_pages = []
        _status_pages = d.pop("status_pages")
        for status_pages_item_data in _status_pages:
            status_pages_item = MaintenanceDetailStatusPageSchema.from_dict(status_pages_item_data)

            status_pages.append(status_pages_item)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        resources_count = d.pop("resources_count", UNSET)

        maintenance_detail_schema = cls(
            id=id,
            name=name,
            started_at=started_at,
            finished_at=finished_at,
            resources=resources,
            status_pages=status_pages,
            description=description,
            resources_count=resources_count,
        )

        maintenance_detail_schema.additional_properties = d
        return maintenance_detail_schema

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
