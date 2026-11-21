from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.source_list_schema import SourceListSchema


T = TypeVar("T", bound="DashboardListSchema")


@_attrs_define
class DashboardListSchema:
    """
    Attributes:
        id (UUID):
        name (str):
        fetch_interval (int):
        charts_count (int):
        source (SourceListSchema):
        group_id (None | Unset | UUID):
        date_from (None | str | Unset):  Default: 'now-24h'.
        date_to (None | str | Unset):  Default: 'now'.
    """

    id: UUID
    name: str
    fetch_interval: int
    charts_count: int
    source: SourceListSchema
    group_id: None | Unset | UUID = UNSET
    date_from: None | str | Unset = "now-24h"
    date_to: None | str | Unset = "now"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        fetch_interval = self.fetch_interval

        charts_count = self.charts_count

        source = self.source.to_dict()

        group_id: None | str | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        elif isinstance(self.group_id, UUID):
            group_id = str(self.group_id)
        else:
            group_id = self.group_id

        date_from: None | str | Unset
        if isinstance(self.date_from, Unset):
            date_from = UNSET
        else:
            date_from = self.date_from

        date_to: None | str | Unset
        if isinstance(self.date_to, Unset):
            date_to = UNSET
        else:
            date_to = self.date_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "fetch_interval": fetch_interval,
                "charts_count": charts_count,
                "source": source,
            }
        )
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if date_from is not UNSET:
            field_dict["date_from"] = date_from
        if date_to is not UNSET:
            field_dict["date_to"] = date_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.source_list_schema import SourceListSchema  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        fetch_interval = d.pop("fetch_interval")

        charts_count = d.pop("charts_count")

        source = SourceListSchema.from_dict(d.pop("source"))

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

        def _parse_date_from(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_from = _parse_date_from(d.pop("date_from", UNSET))

        def _parse_date_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_to = _parse_date_to(d.pop("date_to", UNSET))

        dashboard_list_schema = cls(
            id=id,
            name=name,
            fetch_interval=fetch_interval,
            charts_count=charts_count,
            source=source,
            group_id=group_id,
            date_from=date_from,
            date_to=date_to,
        )

        dashboard_list_schema.additional_properties = d
        return dashboard_list_schema

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
