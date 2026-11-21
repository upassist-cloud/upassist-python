from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.platform_schema import PlatformSchema


T = TypeVar("T", bound="SourceListSchema")


@_attrs_define
class SourceListSchema:
    """
    Attributes:
        id (UUID):
        name (str):
        logs_retention_days (int):
        metrics_retention_days (int):
        platform (PlatformSchema):
        group_id (None | Unset | UUID):
        default_dashboard_id (None | Unset | UUID):
        has_logs (bool | Unset):  Default: False.
        has_metrics (bool | Unset):  Default: False.
        logs_last_at (None | str | Unset):
        metrics_last_at (None | str | Unset):
        logs_events_24h (int | Unset):  Default: 0.
        logs_bytes_24h (int | Unset):  Default: 0.
        logs_bytes_total (int | Unset):  Default: 0.
        metrics_points_24h (int | Unset):  Default: 0.
        metrics_active_series_24h (int | Unset):  Default: 0.
        metrics_bytes_total (int | Unset):  Default: 0.
    """

    id: UUID
    name: str
    logs_retention_days: int
    metrics_retention_days: int
    platform: PlatformSchema
    group_id: None | Unset | UUID = UNSET
    default_dashboard_id: None | Unset | UUID = UNSET
    has_logs: bool | Unset = False
    has_metrics: bool | Unset = False
    logs_last_at: None | str | Unset = UNSET
    metrics_last_at: None | str | Unset = UNSET
    logs_events_24h: int | Unset = 0
    logs_bytes_24h: int | Unset = 0
    logs_bytes_total: int | Unset = 0
    metrics_points_24h: int | Unset = 0
    metrics_active_series_24h: int | Unset = 0
    metrics_bytes_total: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        logs_retention_days = self.logs_retention_days

        metrics_retention_days = self.metrics_retention_days

        platform = self.platform.to_dict()

        group_id: None | str | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        elif isinstance(self.group_id, UUID):
            group_id = str(self.group_id)
        else:
            group_id = self.group_id

        default_dashboard_id: None | str | Unset
        if isinstance(self.default_dashboard_id, Unset):
            default_dashboard_id = UNSET
        elif isinstance(self.default_dashboard_id, UUID):
            default_dashboard_id = str(self.default_dashboard_id)
        else:
            default_dashboard_id = self.default_dashboard_id

        has_logs = self.has_logs

        has_metrics = self.has_metrics

        logs_last_at: None | str | Unset
        if isinstance(self.logs_last_at, Unset):
            logs_last_at = UNSET
        else:
            logs_last_at = self.logs_last_at

        metrics_last_at: None | str | Unset
        if isinstance(self.metrics_last_at, Unset):
            metrics_last_at = UNSET
        else:
            metrics_last_at = self.metrics_last_at

        logs_events_24h = self.logs_events_24h

        logs_bytes_24h = self.logs_bytes_24h

        logs_bytes_total = self.logs_bytes_total

        metrics_points_24h = self.metrics_points_24h

        metrics_active_series_24h = self.metrics_active_series_24h

        metrics_bytes_total = self.metrics_bytes_total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "logs_retention_days": logs_retention_days,
                "metrics_retention_days": metrics_retention_days,
                "platform": platform,
            }
        )
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if default_dashboard_id is not UNSET:
            field_dict["default_dashboard_id"] = default_dashboard_id
        if has_logs is not UNSET:
            field_dict["has_logs"] = has_logs
        if has_metrics is not UNSET:
            field_dict["has_metrics"] = has_metrics
        if logs_last_at is not UNSET:
            field_dict["logs_last_at"] = logs_last_at
        if metrics_last_at is not UNSET:
            field_dict["metrics_last_at"] = metrics_last_at
        if logs_events_24h is not UNSET:
            field_dict["logs_events_24h"] = logs_events_24h
        if logs_bytes_24h is not UNSET:
            field_dict["logs_bytes_24h"] = logs_bytes_24h
        if logs_bytes_total is not UNSET:
            field_dict["logs_bytes_total"] = logs_bytes_total
        if metrics_points_24h is not UNSET:
            field_dict["metrics_points_24h"] = metrics_points_24h
        if metrics_active_series_24h is not UNSET:
            field_dict["metrics_active_series_24h"] = metrics_active_series_24h
        if metrics_bytes_total is not UNSET:
            field_dict["metrics_bytes_total"] = metrics_bytes_total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.platform_schema import PlatformSchema  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        logs_retention_days = d.pop("logs_retention_days")

        metrics_retention_days = d.pop("metrics_retention_days")

        platform = PlatformSchema.from_dict(d.pop("platform"))

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

        def _parse_default_dashboard_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                default_dashboard_id_type_0 = UUID(data)

                return default_dashboard_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        default_dashboard_id = _parse_default_dashboard_id(d.pop("default_dashboard_id", UNSET))

        has_logs = d.pop("has_logs", UNSET)

        has_metrics = d.pop("has_metrics", UNSET)

        def _parse_logs_last_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logs_last_at = _parse_logs_last_at(d.pop("logs_last_at", UNSET))

        def _parse_metrics_last_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        metrics_last_at = _parse_metrics_last_at(d.pop("metrics_last_at", UNSET))

        logs_events_24h = d.pop("logs_events_24h", UNSET)

        logs_bytes_24h = d.pop("logs_bytes_24h", UNSET)

        logs_bytes_total = d.pop("logs_bytes_total", UNSET)

        metrics_points_24h = d.pop("metrics_points_24h", UNSET)

        metrics_active_series_24h = d.pop("metrics_active_series_24h", UNSET)

        metrics_bytes_total = d.pop("metrics_bytes_total", UNSET)

        source_list_schema = cls(
            id=id,
            name=name,
            logs_retention_days=logs_retention_days,
            metrics_retention_days=metrics_retention_days,
            platform=platform,
            group_id=group_id,
            default_dashboard_id=default_dashboard_id,
            has_logs=has_logs,
            has_metrics=has_metrics,
            logs_last_at=logs_last_at,
            metrics_last_at=metrics_last_at,
            logs_events_24h=logs_events_24h,
            logs_bytes_24h=logs_bytes_24h,
            logs_bytes_total=logs_bytes_total,
            metrics_points_24h=metrics_points_24h,
            metrics_active_series_24h=metrics_active_series_24h,
            metrics_bytes_total=metrics_bytes_total,
        )

        source_list_schema.additional_properties = d
        return source_list_schema

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
