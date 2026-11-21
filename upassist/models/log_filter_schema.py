from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.log_filter_condition_schema import LogFilterConditionSchema


T = TypeVar("T", bound="LogFilterSchema")


@_attrs_define
class LogFilterSchema:
    """
    Attributes:
        sources_ids (list[UUID] | None | Unset):
        pattern (None | str | Unset):
        query (None | str | Unset):
        search_text (None | str | Unset):
        from_datetime (datetime.datetime | None | Unset):
        to_datetime (datetime.datetime | None | Unset):
        conditions (list[LogFilterConditionSchema] | None | Unset):
    """

    sources_ids: list[UUID] | None | Unset = UNSET
    pattern: None | str | Unset = UNSET
    query: None | str | Unset = UNSET
    search_text: None | str | Unset = UNSET
    from_datetime: datetime.datetime | None | Unset = UNSET
    to_datetime: datetime.datetime | None | Unset = UNSET
    conditions: list[LogFilterConditionSchema] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sources_ids: list[str] | None | Unset
        if isinstance(self.sources_ids, Unset):
            sources_ids = UNSET
        elif isinstance(self.sources_ids, list):
            sources_ids = []
            for sources_ids_type_0_item_data in self.sources_ids:
                sources_ids_type_0_item = str(sources_ids_type_0_item_data)
                sources_ids.append(sources_ids_type_0_item)

        else:
            sources_ids = self.sources_ids

        pattern: None | str | Unset
        if isinstance(self.pattern, Unset):
            pattern = UNSET
        else:
            pattern = self.pattern

        query: None | str | Unset
        if isinstance(self.query, Unset):
            query = UNSET
        else:
            query = self.query

        search_text: None | str | Unset
        if isinstance(self.search_text, Unset):
            search_text = UNSET
        else:
            search_text = self.search_text

        from_datetime: None | str | Unset
        if isinstance(self.from_datetime, Unset):
            from_datetime = UNSET
        elif isinstance(self.from_datetime, datetime.datetime):
            from_datetime = self.from_datetime.isoformat()
        else:
            from_datetime = self.from_datetime

        to_datetime: None | str | Unset
        if isinstance(self.to_datetime, Unset):
            to_datetime = UNSET
        elif isinstance(self.to_datetime, datetime.datetime):
            to_datetime = self.to_datetime.isoformat()
        else:
            to_datetime = self.to_datetime

        conditions: list[dict[str, Any]] | None | Unset
        if isinstance(self.conditions, Unset):
            conditions = UNSET
        elif isinstance(self.conditions, list):
            conditions = []
            for conditions_type_0_item_data in self.conditions:
                conditions_type_0_item = conditions_type_0_item_data.to_dict()
                conditions.append(conditions_type_0_item)

        else:
            conditions = self.conditions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sources_ids is not UNSET:
            field_dict["sources_ids"] = sources_ids
        if pattern is not UNSET:
            field_dict["pattern"] = pattern
        if query is not UNSET:
            field_dict["query"] = query
        if search_text is not UNSET:
            field_dict["search_text"] = search_text
        if from_datetime is not UNSET:
            field_dict["from_datetime"] = from_datetime
        if to_datetime is not UNSET:
            field_dict["to_datetime"] = to_datetime
        if conditions is not UNSET:
            field_dict["conditions"] = conditions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.log_filter_condition_schema import LogFilterConditionSchema  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_sources_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sources_ids_type_0 = []
                _sources_ids_type_0 = data
                for sources_ids_type_0_item_data in _sources_ids_type_0:
                    sources_ids_type_0_item = UUID(sources_ids_type_0_item_data)

                    sources_ids_type_0.append(sources_ids_type_0_item)

                return sources_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        sources_ids = _parse_sources_ids(d.pop("sources_ids", UNSET))

        def _parse_pattern(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pattern = _parse_pattern(d.pop("pattern", UNSET))

        def _parse_query(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        query = _parse_query(d.pop("query", UNSET))

        def _parse_search_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        search_text = _parse_search_text(d.pop("search_text", UNSET))

        def _parse_from_datetime(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                from_datetime_type_0 = datetime.datetime.fromisoformat(data)

                return from_datetime_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        from_datetime = _parse_from_datetime(d.pop("from_datetime", UNSET))

        def _parse_to_datetime(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                to_datetime_type_0 = datetime.datetime.fromisoformat(data)

                return to_datetime_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        to_datetime = _parse_to_datetime(d.pop("to_datetime", UNSET))

        def _parse_conditions(data: object) -> list[LogFilterConditionSchema] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                conditions_type_0 = []
                _conditions_type_0 = data
                for conditions_type_0_item_data in _conditions_type_0:
                    conditions_type_0_item = LogFilterConditionSchema.from_dict(conditions_type_0_item_data)

                    conditions_type_0.append(conditions_type_0_item)

                return conditions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LogFilterConditionSchema] | None | Unset, data)

        conditions = _parse_conditions(d.pop("conditions", UNSET))

        log_filter_schema = cls(
            sources_ids=sources_ids,
            pattern=pattern,
            query=query,
            search_text=search_text,
            from_datetime=from_datetime,
            to_datetime=to_datetime,
            conditions=conditions,
        )

        log_filter_schema.additional_properties = d
        return log_filter_schema

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
