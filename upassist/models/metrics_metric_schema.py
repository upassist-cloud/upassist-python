from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metrics_counter_schema import MetricsCounterSchema
    from ..models.metrics_gauge_schema import MetricsGaugeSchema
    from ..models.metrics_metric_schema_tags_type_0 import MetricsMetricSchemaTagsType0


T = TypeVar("T", bound="MetricsMetricSchema")


@_attrs_define
class MetricsMetricSchema:
    """
    Attributes:
        name (str):
        namespace (None | str | Unset):
        tags (MetricsMetricSchemaTagsType0 | None | Unset):
        kind (None | str | Unset):
        timestamp (datetime.datetime | None | Unset):
        dt (datetime.datetime | None | Unset):
        counter (MetricsCounterSchema | None | Unset):
        gauge (MetricsGaugeSchema | None | Unset):
    """

    name: str
    namespace: None | str | Unset = UNSET
    tags: MetricsMetricSchemaTagsType0 | None | Unset = UNSET
    kind: None | str | Unset = UNSET
    timestamp: datetime.datetime | None | Unset = UNSET
    dt: datetime.datetime | None | Unset = UNSET
    counter: MetricsCounterSchema | None | Unset = UNSET
    gauge: MetricsGaugeSchema | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.metrics_counter_schema import MetricsCounterSchema  # noqa: PLC0415
        from ..models.metrics_gauge_schema import MetricsGaugeSchema  # noqa: PLC0415
        from ..models.metrics_metric_schema_tags_type_0 import MetricsMetricSchemaTagsType0  # noqa: PLC0415

        name = self.name

        namespace: None | str | Unset
        if isinstance(self.namespace, Unset):
            namespace = UNSET
        else:
            namespace = self.namespace

        tags: dict[str, Any] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, MetricsMetricSchemaTagsType0):
            tags = self.tags.to_dict()
        else:
            tags = self.tags

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        timestamp: None | str | Unset
        if isinstance(self.timestamp, Unset):
            timestamp = UNSET
        elif isinstance(self.timestamp, datetime.datetime):
            timestamp = self.timestamp.isoformat()
        else:
            timestamp = self.timestamp

        dt: None | str | Unset
        if isinstance(self.dt, Unset):
            dt = UNSET
        elif isinstance(self.dt, datetime.datetime):
            dt = self.dt.isoformat()
        else:
            dt = self.dt

        counter: dict[str, Any] | None | Unset
        if isinstance(self.counter, Unset):
            counter = UNSET
        elif isinstance(self.counter, MetricsCounterSchema):
            counter = self.counter.to_dict()
        else:
            counter = self.counter

        gauge: dict[str, Any] | None | Unset
        if isinstance(self.gauge, Unset):
            gauge = UNSET
        elif isinstance(self.gauge, MetricsGaugeSchema):
            gauge = self.gauge.to_dict()
        else:
            gauge = self.gauge

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if tags is not UNSET:
            field_dict["tags"] = tags
        if kind is not UNSET:
            field_dict["kind"] = kind
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if dt is not UNSET:
            field_dict["dt"] = dt
        if counter is not UNSET:
            field_dict["counter"] = counter
        if gauge is not UNSET:
            field_dict["gauge"] = gauge

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metrics_counter_schema import MetricsCounterSchema  # noqa: PLC0415
        from ..models.metrics_gauge_schema import MetricsGaugeSchema  # noqa: PLC0415
        from ..models.metrics_metric_schema_tags_type_0 import MetricsMetricSchemaTagsType0  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_namespace(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        namespace = _parse_namespace(d.pop("namespace", UNSET))

        def _parse_tags(data: object) -> MetricsMetricSchemaTagsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tags_type_0 = MetricsMetricSchemaTagsType0.from_dict(data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MetricsMetricSchemaTagsType0 | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))

        def _parse_timestamp(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                timestamp_type_0 = datetime.datetime.fromisoformat(data)

                return timestamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        timestamp = _parse_timestamp(d.pop("timestamp", UNSET))

        def _parse_dt(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dt_type_0 = datetime.datetime.fromisoformat(data)

                return dt_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        dt = _parse_dt(d.pop("dt", UNSET))

        def _parse_counter(data: object) -> MetricsCounterSchema | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                counter_type_0 = MetricsCounterSchema.from_dict(data)

                return counter_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MetricsCounterSchema | None | Unset, data)

        counter = _parse_counter(d.pop("counter", UNSET))

        def _parse_gauge(data: object) -> MetricsGaugeSchema | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                gauge_type_0 = MetricsGaugeSchema.from_dict(data)

                return gauge_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MetricsGaugeSchema | None | Unset, data)

        gauge = _parse_gauge(d.pop("gauge", UNSET))

        metrics_metric_schema = cls(
            name=name,
            namespace=namespace,
            tags=tags,
            kind=kind,
            timestamp=timestamp,
            dt=dt,
            counter=counter,
            gauge=gauge,
        )

        metrics_metric_schema.additional_properties = d
        return metrics_metric_schema

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
