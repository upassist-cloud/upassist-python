from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ErrorAppSchema")


@_attrs_define
class ErrorAppSchema:
    """
    Attributes:
        id (UUID):
        name (str):
        slug (str):
        secret_token (str):
        sentry_id (int):
        events_retention_days (int):
        issue_count (int):
        stored_event_count (int):
        paused (bool):
        alerts_on (bool):
        created_at (datetime.datetime):
        platform (str | Unset):  Default: 'python'.
        group_id (None | Unset | UUID):
        max_events (int | None | Unset):
        alert_suppressed_environments (list[str] | None | Unset):
        dsn (None | str | Unset):
        unresolved_count (int | Unset):  Default: 0.
        events_24h (int | Unset):  Default: 0.
        last_event_at (datetime.datetime | None | Unset):
        trend_7d (list[list[datetime.datetime | int]] | None | Unset):
    """

    id: UUID
    name: str
    slug: str
    secret_token: str
    sentry_id: int
    events_retention_days: int
    issue_count: int
    stored_event_count: int
    paused: bool
    alerts_on: bool
    created_at: datetime.datetime
    platform: str | Unset = "python"
    group_id: None | Unset | UUID = UNSET
    max_events: int | None | Unset = UNSET
    alert_suppressed_environments: list[str] | None | Unset = UNSET
    dsn: None | str | Unset = UNSET
    unresolved_count: int | Unset = 0
    events_24h: int | Unset = 0
    last_event_at: datetime.datetime | None | Unset = UNSET
    trend_7d: list[list[datetime.datetime | int]] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        slug = self.slug

        secret_token = self.secret_token

        sentry_id = self.sentry_id

        events_retention_days = self.events_retention_days

        issue_count = self.issue_count

        stored_event_count = self.stored_event_count

        paused = self.paused

        alerts_on = self.alerts_on

        created_at = self.created_at.isoformat()

        platform = self.platform

        group_id: None | str | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        elif isinstance(self.group_id, UUID):
            group_id = str(self.group_id)
        else:
            group_id = self.group_id

        max_events: int | None | Unset
        if isinstance(self.max_events, Unset):
            max_events = UNSET
        else:
            max_events = self.max_events

        alert_suppressed_environments: list[str] | None | Unset
        if isinstance(self.alert_suppressed_environments, Unset):
            alert_suppressed_environments = UNSET
        elif isinstance(self.alert_suppressed_environments, list):
            alert_suppressed_environments = self.alert_suppressed_environments

        else:
            alert_suppressed_environments = self.alert_suppressed_environments

        dsn: None | str | Unset
        if isinstance(self.dsn, Unset):
            dsn = UNSET
        else:
            dsn = self.dsn

        unresolved_count = self.unresolved_count

        events_24h = self.events_24h

        last_event_at: None | str | Unset
        if isinstance(self.last_event_at, Unset):
            last_event_at = UNSET
        elif isinstance(self.last_event_at, datetime.datetime):
            last_event_at = self.last_event_at.isoformat()
        else:
            last_event_at = self.last_event_at

        trend_7d: list[list[int | str]] | None | Unset
        if isinstance(self.trend_7d, Unset):
            trend_7d = UNSET
        elif isinstance(self.trend_7d, list):
            trend_7d = []
            for trend_7d_type_0_item_data in self.trend_7d:
                trend_7d_type_0_item = []
                for trend_7d_type_0_item_item_data in trend_7d_type_0_item_data:
                    trend_7d_type_0_item_item: int | str
                    if isinstance(trend_7d_type_0_item_item_data, datetime.datetime):
                        trend_7d_type_0_item_item = trend_7d_type_0_item_item_data.isoformat()
                    else:
                        trend_7d_type_0_item_item = trend_7d_type_0_item_item_data
                    trend_7d_type_0_item.append(trend_7d_type_0_item_item)

                trend_7d.append(trend_7d_type_0_item)

        else:
            trend_7d = self.trend_7d

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "secret_token": secret_token,
                "sentry_id": sentry_id,
                "events_retention_days": events_retention_days,
                "issue_count": issue_count,
                "stored_event_count": stored_event_count,
                "paused": paused,
                "alerts_on": alerts_on,
                "created_at": created_at,
            }
        )
        if platform is not UNSET:
            field_dict["platform"] = platform
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if max_events is not UNSET:
            field_dict["max_events"] = max_events
        if alert_suppressed_environments is not UNSET:
            field_dict["alert_suppressed_environments"] = alert_suppressed_environments
        if dsn is not UNSET:
            field_dict["dsn"] = dsn
        if unresolved_count is not UNSET:
            field_dict["unresolved_count"] = unresolved_count
        if events_24h is not UNSET:
            field_dict["events_24h"] = events_24h
        if last_event_at is not UNSET:
            field_dict["last_event_at"] = last_event_at
        if trend_7d is not UNSET:
            field_dict["trend_7d"] = trend_7d

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        slug = d.pop("slug")

        secret_token = d.pop("secret_token")

        sentry_id = d.pop("sentry_id")

        events_retention_days = d.pop("events_retention_days")

        issue_count = d.pop("issue_count")

        stored_event_count = d.pop("stored_event_count")

        paused = d.pop("paused")

        alerts_on = d.pop("alerts_on")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        platform = d.pop("platform", UNSET)

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

        def _parse_max_events(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_events = _parse_max_events(d.pop("max_events", UNSET))

        def _parse_alert_suppressed_environments(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                alert_suppressed_environments_type_0 = cast(list[str], data)

                return alert_suppressed_environments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        alert_suppressed_environments = _parse_alert_suppressed_environments(
            d.pop("alert_suppressed_environments", UNSET)
        )

        def _parse_dsn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dsn = _parse_dsn(d.pop("dsn", UNSET))

        unresolved_count = d.pop("unresolved_count", UNSET)

        events_24h = d.pop("events_24h", UNSET)

        def _parse_last_event_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_event_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_event_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_event_at = _parse_last_event_at(d.pop("last_event_at", UNSET))

        def _parse_trend_7d(data: object) -> list[list[datetime.datetime | int]] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                trend_7d_type_0 = []
                _trend_7d_type_0 = data
                for trend_7d_type_0_item_data in _trend_7d_type_0:
                    trend_7d_type_0_item = []
                    _trend_7d_type_0_item = trend_7d_type_0_item_data
                    for trend_7d_type_0_item_item_data in _trend_7d_type_0_item:

                        def _parse_trend_7d_type_0_item_item(data: object) -> datetime.datetime | int:
                            try:
                                if not isinstance(data, str):
                                    raise TypeError()
                                trend_7d_type_0_item_item_type_0 = datetime.datetime.fromisoformat(data)

                                return trend_7d_type_0_item_item_type_0
                            except (TypeError, ValueError, AttributeError, KeyError):
                                pass
                            return cast(datetime.datetime | int, data)

                        trend_7d_type_0_item_item = _parse_trend_7d_type_0_item_item(trend_7d_type_0_item_item_data)

                        trend_7d_type_0_item.append(trend_7d_type_0_item_item)

                    trend_7d_type_0.append(trend_7d_type_0_item)

                return trend_7d_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[list[datetime.datetime | int]] | None | Unset, data)

        trend_7d = _parse_trend_7d(d.pop("trend_7d", UNSET))

        error_app_schema = cls(
            id=id,
            name=name,
            slug=slug,
            secret_token=secret_token,
            sentry_id=sentry_id,
            events_retention_days=events_retention_days,
            issue_count=issue_count,
            stored_event_count=stored_event_count,
            paused=paused,
            alerts_on=alerts_on,
            created_at=created_at,
            platform=platform,
            group_id=group_id,
            max_events=max_events,
            alert_suppressed_environments=alert_suppressed_environments,
            dsn=dsn,
            unresolved_count=unresolved_count,
            events_24h=events_24h,
            last_event_at=last_event_at,
            trend_7d=trend_7d,
        )

        error_app_schema.additional_properties = d
        return error_app_schema

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
