from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metric_series_schema_tags_type_0 import MetricSeriesSchemaTagsType0


T = TypeVar("T", bound="MetricSeriesSchema")


@_attrs_define
class MetricSeriesSchema:
    """
    Attributes:
        name (str):
        namespace (None | str | Unset):
        kind (None | str | Unset):
        tags (MetricSeriesSchemaTagsType0 | None | Unset):
        series_id (int | None | Unset):
    """

    name: str
    namespace: None | str | Unset = UNSET
    kind: None | str | Unset = UNSET
    tags: MetricSeriesSchemaTagsType0 | None | Unset = UNSET
    series_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.metric_series_schema_tags_type_0 import MetricSeriesSchemaTagsType0  # noqa: PLC0415

        name = self.name

        namespace: None | str | Unset
        if isinstance(self.namespace, Unset):
            namespace = UNSET
        else:
            namespace = self.namespace

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        tags: dict[str, Any] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, MetricSeriesSchemaTagsType0):
            tags = self.tags.to_dict()
        else:
            tags = self.tags

        series_id: int | None | Unset
        if isinstance(self.series_id, Unset):
            series_id = UNSET
        else:
            series_id = self.series_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if kind is not UNSET:
            field_dict["kind"] = kind
        if tags is not UNSET:
            field_dict["tags"] = tags
        if series_id is not UNSET:
            field_dict["series_id"] = series_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metric_series_schema_tags_type_0 import MetricSeriesSchemaTagsType0  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_namespace(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        namespace = _parse_namespace(d.pop("namespace", UNSET))

        def _parse_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))

        def _parse_tags(data: object) -> MetricSeriesSchemaTagsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tags_type_0 = MetricSeriesSchemaTagsType0.from_dict(data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MetricSeriesSchemaTagsType0 | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_series_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        series_id = _parse_series_id(d.pop("series_id", UNSET))

        metric_series_schema = cls(
            name=name,
            namespace=namespace,
            kind=kind,
            tags=tags,
            series_id=series_id,
        )

        metric_series_schema.additional_properties = d
        return metric_series_schema

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
