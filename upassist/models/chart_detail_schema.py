from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.axis_scale_enum import AxisScaleEnum
from ..models.chart_type_enum import ChartTypeEnum
from ..models.legend_position_enum import LegendPositionEnum
from ..models.treat_missing_values_enum import TreatMissingValuesEnum
from ..models.units_enum import UnitsEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chart_detail_schema_series_colors_type_0 import ChartDetailSchemaSeriesColorsType0
    from ..models.chart_query_schema import ChartQuerySchema


T = TypeVar("T", bound="ChartDetailSchema")


@_attrs_define
class ChartDetailSchema:
    """
    Attributes:
        id (UUID):
        section_id (UUID):
        name (str):
        chart_type (ChartTypeEnum):
        order (int):
        decimal_places (int):
        units (UnitsEnum):
        queries (list[ChartQuerySchema]):
        x (int):
        y (int):
        w (int):
        h (int):
        description (None | str | Unset):
        treat_missing_values (None | TreatMissingValuesEnum | Unset): For LINE chart_type
        y_axis_min (int | None | Unset):
        y_axis_max (int | None | Unset):
        min_value (int | None | Unset): For GAUGE chart_type
        max_value (int | None | Unset): For GAUGE chart_type
        y_axis_scale (AxisScaleEnum | None | Unset): For LINE, BAR, SCATTER chart_type
        legend_position (LegendPositionEnum | None | Unset): For LINE, BAR, PIE, SCATTER chart_type
        series_colors (ChartDetailSchemaSeriesColorsType0 | None | Unset):
    """

    id: UUID
    section_id: UUID
    name: str
    chart_type: ChartTypeEnum
    order: int
    decimal_places: int
    units: UnitsEnum
    queries: list[ChartQuerySchema]
    x: int
    y: int
    w: int
    h: int
    description: None | str | Unset = UNSET
    treat_missing_values: None | TreatMissingValuesEnum | Unset = UNSET
    y_axis_min: int | None | Unset = UNSET
    y_axis_max: int | None | Unset = UNSET
    min_value: int | None | Unset = UNSET
    max_value: int | None | Unset = UNSET
    y_axis_scale: AxisScaleEnum | None | Unset = UNSET
    legend_position: LegendPositionEnum | None | Unset = UNSET
    series_colors: ChartDetailSchemaSeriesColorsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.chart_detail_schema_series_colors_type_0 import (
            ChartDetailSchemaSeriesColorsType0,  # noqa: PLC0415
        )

        id = str(self.id)

        section_id = str(self.section_id)

        name = self.name

        chart_type = self.chart_type.value

        order = self.order

        decimal_places = self.decimal_places

        units = self.units.value

        queries = []
        for queries_item_data in self.queries:
            queries_item = queries_item_data.to_dict()
            queries.append(queries_item)

        x = self.x

        y = self.y

        w = self.w

        h = self.h

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        treat_missing_values: None | str | Unset
        if isinstance(self.treat_missing_values, Unset):
            treat_missing_values = UNSET
        elif isinstance(self.treat_missing_values, TreatMissingValuesEnum):
            treat_missing_values = self.treat_missing_values.value
        else:
            treat_missing_values = self.treat_missing_values

        y_axis_min: int | None | Unset
        if isinstance(self.y_axis_min, Unset):
            y_axis_min = UNSET
        else:
            y_axis_min = self.y_axis_min

        y_axis_max: int | None | Unset
        if isinstance(self.y_axis_max, Unset):
            y_axis_max = UNSET
        else:
            y_axis_max = self.y_axis_max

        min_value: int | None | Unset
        if isinstance(self.min_value, Unset):
            min_value = UNSET
        else:
            min_value = self.min_value

        max_value: int | None | Unset
        if isinstance(self.max_value, Unset):
            max_value = UNSET
        else:
            max_value = self.max_value

        y_axis_scale: None | str | Unset
        if isinstance(self.y_axis_scale, Unset):
            y_axis_scale = UNSET
        elif isinstance(self.y_axis_scale, AxisScaleEnum):
            y_axis_scale = self.y_axis_scale.value
        else:
            y_axis_scale = self.y_axis_scale

        legend_position: None | str | Unset
        if isinstance(self.legend_position, Unset):
            legend_position = UNSET
        elif isinstance(self.legend_position, LegendPositionEnum):
            legend_position = self.legend_position.value
        else:
            legend_position = self.legend_position

        series_colors: dict[str, Any] | None | Unset
        if isinstance(self.series_colors, Unset):
            series_colors = UNSET
        elif isinstance(self.series_colors, ChartDetailSchemaSeriesColorsType0):
            series_colors = self.series_colors.to_dict()
        else:
            series_colors = self.series_colors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "section_id": section_id,
                "name": name,
                "chart_type": chart_type,
                "order": order,
                "decimal_places": decimal_places,
                "units": units,
                "queries": queries,
                "x": x,
                "y": y,
                "w": w,
                "h": h,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if treat_missing_values is not UNSET:
            field_dict["treat_missing_values"] = treat_missing_values
        if y_axis_min is not UNSET:
            field_dict["y_axis_min"] = y_axis_min
        if y_axis_max is not UNSET:
            field_dict["y_axis_max"] = y_axis_max
        if min_value is not UNSET:
            field_dict["min_value"] = min_value
        if max_value is not UNSET:
            field_dict["max_value"] = max_value
        if y_axis_scale is not UNSET:
            field_dict["y_axis_scale"] = y_axis_scale
        if legend_position is not UNSET:
            field_dict["legend_position"] = legend_position
        if series_colors is not UNSET:
            field_dict["series_colors"] = series_colors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chart_detail_schema_series_colors_type_0 import (
            ChartDetailSchemaSeriesColorsType0,  # noqa: PLC0415
        )
        from ..models.chart_query_schema import ChartQuerySchema  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        section_id = UUID(d.pop("section_id"))

        name = d.pop("name")

        chart_type = ChartTypeEnum(d.pop("chart_type"))

        order = d.pop("order")

        decimal_places = d.pop("decimal_places")

        units = UnitsEnum(d.pop("units"))

        queries = []
        _queries = d.pop("queries")
        for queries_item_data in _queries:
            queries_item = ChartQuerySchema.from_dict(queries_item_data)

            queries.append(queries_item)

        x = d.pop("x")

        y = d.pop("y")

        w = d.pop("w")

        h = d.pop("h")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_treat_missing_values(data: object) -> None | TreatMissingValuesEnum | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                treat_missing_values_type_0 = TreatMissingValuesEnum(data)

                return treat_missing_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TreatMissingValuesEnum | Unset, data)

        treat_missing_values = _parse_treat_missing_values(d.pop("treat_missing_values", UNSET))

        def _parse_y_axis_min(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        y_axis_min = _parse_y_axis_min(d.pop("y_axis_min", UNSET))

        def _parse_y_axis_max(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        y_axis_max = _parse_y_axis_max(d.pop("y_axis_max", UNSET))

        def _parse_min_value(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_value = _parse_min_value(d.pop("min_value", UNSET))

        def _parse_max_value(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_value = _parse_max_value(d.pop("max_value", UNSET))

        def _parse_y_axis_scale(data: object) -> AxisScaleEnum | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                y_axis_scale_type_0 = AxisScaleEnum(data)

                return y_axis_scale_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AxisScaleEnum | None | Unset, data)

        y_axis_scale = _parse_y_axis_scale(d.pop("y_axis_scale", UNSET))

        def _parse_legend_position(data: object) -> LegendPositionEnum | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                legend_position_type_0 = LegendPositionEnum(data)

                return legend_position_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LegendPositionEnum | None | Unset, data)

        legend_position = _parse_legend_position(d.pop("legend_position", UNSET))

        def _parse_series_colors(data: object) -> ChartDetailSchemaSeriesColorsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                series_colors_type_0 = ChartDetailSchemaSeriesColorsType0.from_dict(data)

                return series_colors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ChartDetailSchemaSeriesColorsType0 | None | Unset, data)

        series_colors = _parse_series_colors(d.pop("series_colors", UNSET))

        chart_detail_schema = cls(
            id=id,
            section_id=section_id,
            name=name,
            chart_type=chart_type,
            order=order,
            decimal_places=decimal_places,
            units=units,
            queries=queries,
            x=x,
            y=y,
            w=w,
            h=h,
            description=description,
            treat_missing_values=treat_missing_values,
            y_axis_min=y_axis_min,
            y_axis_max=y_axis_max,
            min_value=min_value,
            max_value=max_value,
            y_axis_scale=y_axis_scale,
            legend_position=legend_position,
            series_colors=series_colors,
        )

        chart_detail_schema.additional_properties = d
        return chart_detail_schema

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
