from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentStatsSchema")


@_attrs_define
class IncidentStatsSchema:
    """
    Attributes:
        from_date (datetime.date):
        to_date (datetime.date):
        from_datetime (datetime.datetime):
        to_datetime (datetime.datetime):
        uptime_percents (float):
        sum_ (int | None | Unset):
        avg (int | None | Unset):
        max_ (int | None | Unset):
        count (int | None | Unset):
        period_alias (None | str | Unset):
    """

    from_date: datetime.date
    to_date: datetime.date
    from_datetime: datetime.datetime
    to_datetime: datetime.datetime
    uptime_percents: float
    sum_: int | None | Unset = UNSET
    avg: int | None | Unset = UNSET
    max_: int | None | Unset = UNSET
    count: int | None | Unset = UNSET
    period_alias: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_date = self.from_date.isoformat()

        to_date = self.to_date.isoformat()

        from_datetime = self.from_datetime.isoformat()

        to_datetime = self.to_datetime.isoformat()

        uptime_percents = self.uptime_percents

        sum_: int | None | Unset
        if isinstance(self.sum_, Unset):
            sum_ = UNSET
        else:
            sum_ = self.sum_

        avg: int | None | Unset
        if isinstance(self.avg, Unset):
            avg = UNSET
        else:
            avg = self.avg

        max_: int | None | Unset
        if isinstance(self.max_, Unset):
            max_ = UNSET
        else:
            max_ = self.max_

        count: int | None | Unset
        if isinstance(self.count, Unset):
            count = UNSET
        else:
            count = self.count

        period_alias: None | str | Unset
        if isinstance(self.period_alias, Unset):
            period_alias = UNSET
        else:
            period_alias = self.period_alias

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from_date": from_date,
                "to_date": to_date,
                "from_datetime": from_datetime,
                "to_datetime": to_datetime,
                "uptime_percents": uptime_percents,
            }
        )
        if sum_ is not UNSET:
            field_dict["sum"] = sum_
        if avg is not UNSET:
            field_dict["avg"] = avg
        if max_ is not UNSET:
            field_dict["max"] = max_
        if count is not UNSET:
            field_dict["count"] = count
        if period_alias is not UNSET:
            field_dict["period_alias"] = period_alias

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_date = datetime.date.fromisoformat(d.pop("from_date"))

        to_date = datetime.date.fromisoformat(d.pop("to_date"))

        from_datetime = datetime.datetime.fromisoformat(d.pop("from_datetime"))

        to_datetime = datetime.datetime.fromisoformat(d.pop("to_datetime"))

        uptime_percents = d.pop("uptime_percents")

        def _parse_sum_(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sum_ = _parse_sum_(d.pop("sum", UNSET))

        def _parse_avg(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        avg = _parse_avg(d.pop("avg", UNSET))

        def _parse_max_(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_ = _parse_max_(d.pop("max", UNSET))

        def _parse_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        count = _parse_count(d.pop("count", UNSET))

        def _parse_period_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        period_alias = _parse_period_alias(d.pop("period_alias", UNSET))

        incident_stats_schema = cls(
            from_date=from_date,
            to_date=to_date,
            from_datetime=from_datetime,
            to_datetime=to_datetime,
            uptime_percents=uptime_percents,
            sum_=sum_,
            avg=avg,
            max_=max_,
            count=count,
            period_alias=period_alias,
        )

        incident_stats_schema.additional_properties = d
        return incident_stats_schema

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
