from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chart_query_type_enum import ChartQueryTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chart_query_schema_builder_config_type_0 import ChartQuerySchemaBuilderConfigType0


T = TypeVar("T", bound="ChartQuerySchema")


@_attrs_define
class ChartQuerySchema:
    """
    Attributes:
        id (UUID):
        query_type (ChartQueryTypeEnum):
        sql_query (str):
        builder_config (ChartQuerySchemaBuilderConfigType0 | None | Unset):
        static_text (None | str | Unset):
        where_condition (None | str | Unset):
        where (list[str] | None | Unset):
        group_by (list[str] | None | Unset):
        having (list[str] | None | Unset):
        order_by (list[str] | None | Unset):
    """

    id: UUID
    query_type: ChartQueryTypeEnum
    sql_query: str
    builder_config: ChartQuerySchemaBuilderConfigType0 | None | Unset = UNSET
    static_text: None | str | Unset = UNSET
    where_condition: None | str | Unset = UNSET
    where: list[str] | None | Unset = UNSET
    group_by: list[str] | None | Unset = UNSET
    having: list[str] | None | Unset = UNSET
    order_by: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.chart_query_schema_builder_config_type_0 import (
            ChartQuerySchemaBuilderConfigType0,  # noqa: PLC0415
        )

        id = str(self.id)

        query_type = self.query_type.value

        sql_query = self.sql_query

        builder_config: dict[str, Any] | None | Unset
        if isinstance(self.builder_config, Unset):
            builder_config = UNSET
        elif isinstance(self.builder_config, ChartQuerySchemaBuilderConfigType0):
            builder_config = self.builder_config.to_dict()
        else:
            builder_config = self.builder_config

        static_text: None | str | Unset
        if isinstance(self.static_text, Unset):
            static_text = UNSET
        else:
            static_text = self.static_text

        where_condition: None | str | Unset
        if isinstance(self.where_condition, Unset):
            where_condition = UNSET
        else:
            where_condition = self.where_condition

        where: list[str] | None | Unset
        if isinstance(self.where, Unset):
            where = UNSET
        elif isinstance(self.where, list):
            where = self.where

        else:
            where = self.where

        group_by: list[str] | None | Unset
        if isinstance(self.group_by, Unset):
            group_by = UNSET
        elif isinstance(self.group_by, list):
            group_by = self.group_by

        else:
            group_by = self.group_by

        having: list[str] | None | Unset
        if isinstance(self.having, Unset):
            having = UNSET
        elif isinstance(self.having, list):
            having = self.having

        else:
            having = self.having

        order_by: list[str] | None | Unset
        if isinstance(self.order_by, Unset):
            order_by = UNSET
        elif isinstance(self.order_by, list):
            order_by = self.order_by

        else:
            order_by = self.order_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "query_type": query_type,
                "sql_query": sql_query,
            }
        )
        if builder_config is not UNSET:
            field_dict["builder_config"] = builder_config
        if static_text is not UNSET:
            field_dict["static_text"] = static_text
        if where_condition is not UNSET:
            field_dict["where_condition"] = where_condition
        if where is not UNSET:
            field_dict["where"] = where
        if group_by is not UNSET:
            field_dict["group_by"] = group_by
        if having is not UNSET:
            field_dict["having"] = having
        if order_by is not UNSET:
            field_dict["order_by"] = order_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chart_query_schema_builder_config_type_0 import (
            ChartQuerySchemaBuilderConfigType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        query_type = ChartQueryTypeEnum(d.pop("query_type"))

        sql_query = d.pop("sql_query")

        def _parse_builder_config(data: object) -> ChartQuerySchemaBuilderConfigType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                builder_config_type_0 = ChartQuerySchemaBuilderConfigType0.from_dict(data)

                return builder_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ChartQuerySchemaBuilderConfigType0 | None | Unset, data)

        builder_config = _parse_builder_config(d.pop("builder_config", UNSET))

        def _parse_static_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        static_text = _parse_static_text(d.pop("static_text", UNSET))

        def _parse_where_condition(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        where_condition = _parse_where_condition(d.pop("where_condition", UNSET))

        def _parse_where(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                where_type_0 = cast(list[str], data)

                return where_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        where = _parse_where(d.pop("where", UNSET))

        def _parse_group_by(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                group_by_type_0 = cast(list[str], data)

                return group_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        group_by = _parse_group_by(d.pop("group_by", UNSET))

        def _parse_having(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                having_type_0 = cast(list[str], data)

                return having_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        having = _parse_having(d.pop("having", UNSET))

        def _parse_order_by(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                order_by_type_0 = cast(list[str], data)

                return order_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        order_by = _parse_order_by(d.pop("order_by", UNSET))

        chart_query_schema = cls(
            id=id,
            query_type=query_type,
            sql_query=sql_query,
            builder_config=builder_config,
            static_text=static_text,
            where_condition=where_condition,
            where=where,
            group_by=group_by,
            having=having,
            order_by=order_by,
        )

        chart_query_schema.additional_properties = d
        return chart_query_schema

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
