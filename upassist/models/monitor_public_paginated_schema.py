from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor_public_schema import MonitorPublicSchema


T = TypeVar("T", bound="MonitorPublicPaginatedSchema")


@_attrs_define
class MonitorPublicPaginatedSchema:
    """
    Attributes:
        data (list[MonitorPublicSchema]):
        pages_count (int): Count of pages
        count (int): Count of data rows by given parameters
        total_count (int): Count of all data rows
        per_page (int | Unset): Count of data per page Default: 50.
        page (int | Unset): Current page number Default: 1.
        next_page (int | None | Unset): Next page number, nullable if not exists.
        prev_page (int | None | Unset): Previous page number, nullable if not exists.
    """

    data: list[MonitorPublicSchema]
    pages_count: int
    count: int
    total_count: int
    per_page: int | Unset = 50
    page: int | Unset = 1
    next_page: int | None | Unset = UNSET
    prev_page: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        pages_count = self.pages_count

        count = self.count

        total_count = self.total_count

        per_page = self.per_page

        page = self.page

        next_page: int | None | Unset
        if isinstance(self.next_page, Unset):
            next_page = UNSET
        else:
            next_page = self.next_page

        prev_page: int | None | Unset
        if isinstance(self.prev_page, Unset):
            prev_page = UNSET
        else:
            prev_page = self.prev_page

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "pages_count": pages_count,
                "count": count,
                "total_count": total_count,
            }
        )
        if per_page is not UNSET:
            field_dict["per_page"] = per_page
        if page is not UNSET:
            field_dict["page"] = page
        if next_page is not UNSET:
            field_dict["next_page"] = next_page
        if prev_page is not UNSET:
            field_dict["prev_page"] = prev_page

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitor_public_schema import MonitorPublicSchema  # noqa: PLC0415

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = MonitorPublicSchema.from_dict(data_item_data)

            data.append(data_item)

        pages_count = d.pop("pages_count")

        count = d.pop("count")

        total_count = d.pop("total_count")

        per_page = d.pop("per_page", UNSET)

        page = d.pop("page", UNSET)

        def _parse_next_page(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        next_page = _parse_next_page(d.pop("next_page", UNSET))

        def _parse_prev_page(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        prev_page = _parse_prev_page(d.pop("prev_page", UNSET))

        monitor_public_paginated_schema = cls(
            data=data,
            pages_count=pages_count,
            count=count,
            total_count=total_count,
            per_page=per_page,
            page=page,
            next_page=next_page,
            prev_page=prev_page,
        )

        monitor_public_paginated_schema.additional_properties = d
        return monitor_public_paginated_schema

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
