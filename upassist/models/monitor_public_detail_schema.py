from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_strategy_enum import IncidentStrategyEnum
from ..models.monitor_type_enum import MonitorTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.location_schema import LocationSchema
    from ..models.monitor_public_detail_schema_meta_type_0 import MonitorPublicDetailSchemaMetaType0
    from ..models.monitor_public_detail_schema_settings_type_0 import MonitorPublicDetailSchemaSettingsType0
    from ..models.tag_schema import TagSchema


T = TypeVar("T", bound="MonitorPublicDetailSchema")


@_attrs_define
class MonitorPublicDetailSchema:
    """
    Attributes:
        id (UUID):
        uri (str):
        name (str):
        monitor_type (MonitorTypeEnum):
        paused (bool):
        fetch_interval (int):
        alerts_on (bool):
        created_at (datetime.datetime):
        group_id (None | Unset | UUID):
        timeout (int | None | Unset):
        description (None | str | Unset):
        is_down (bool | None | Unset):
        is_verified (bool | None | Unset):
        last_fetch_at (datetime.datetime | None | Unset):
        last_down_at (datetime.datetime | None | Unset):
        last_up_time (datetime.datetime | None | Unset):
        incidents_count (int | None | Unset):
        opened_incident_id (None | Unset | UUID):
        settings (MonitorPublicDetailSchemaSettingsType0 | None | Unset):
        realert_period (int | None | Unset):
        confirmation_period (int | None | Unset):
        recovery_period (int | None | Unset):
        open_incident_strategy (IncidentStrategyEnum | None | Unset):
        close_incident_strategy (IncidentStrategyEnum | None | Unset):
        meta (MonitorPublicDetailSchemaMetaType0 | None | Unset):
        locations (list[LocationSchema] | None | Unset):
        tags (list[TagSchema] | None | Unset):
    """

    id: UUID
    uri: str
    name: str
    monitor_type: MonitorTypeEnum
    paused: bool
    fetch_interval: int
    alerts_on: bool
    created_at: datetime.datetime
    group_id: None | Unset | UUID = UNSET
    timeout: int | None | Unset = UNSET
    description: None | str | Unset = UNSET
    is_down: bool | None | Unset = UNSET
    is_verified: bool | None | Unset = UNSET
    last_fetch_at: datetime.datetime | None | Unset = UNSET
    last_down_at: datetime.datetime | None | Unset = UNSET
    last_up_time: datetime.datetime | None | Unset = UNSET
    incidents_count: int | None | Unset = UNSET
    opened_incident_id: None | Unset | UUID = UNSET
    settings: MonitorPublicDetailSchemaSettingsType0 | None | Unset = UNSET
    realert_period: int | None | Unset = UNSET
    confirmation_period: int | None | Unset = UNSET
    recovery_period: int | None | Unset = UNSET
    open_incident_strategy: IncidentStrategyEnum | None | Unset = UNSET
    close_incident_strategy: IncidentStrategyEnum | None | Unset = UNSET
    meta: MonitorPublicDetailSchemaMetaType0 | None | Unset = UNSET
    locations: list[LocationSchema] | None | Unset = UNSET
    tags: list[TagSchema] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.monitor_public_detail_schema_meta_type_0 import (
            MonitorPublicDetailSchemaMetaType0,  # noqa: PLC0415
        )
        from ..models.monitor_public_detail_schema_settings_type_0 import (
            MonitorPublicDetailSchemaSettingsType0,  # noqa: PLC0415
        )

        id = str(self.id)

        uri = self.uri

        name = self.name

        monitor_type = self.monitor_type.value

        paused = self.paused

        fetch_interval = self.fetch_interval

        alerts_on = self.alerts_on

        created_at = self.created_at.isoformat()

        group_id: None | str | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        elif isinstance(self.group_id, UUID):
            group_id = str(self.group_id)
        else:
            group_id = self.group_id

        timeout: int | None | Unset
        if isinstance(self.timeout, Unset):
            timeout = UNSET
        else:
            timeout = self.timeout

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        is_down: bool | None | Unset
        if isinstance(self.is_down, Unset):
            is_down = UNSET
        else:
            is_down = self.is_down

        is_verified: bool | None | Unset
        if isinstance(self.is_verified, Unset):
            is_verified = UNSET
        else:
            is_verified = self.is_verified

        last_fetch_at: None | str | Unset
        if isinstance(self.last_fetch_at, Unset):
            last_fetch_at = UNSET
        elif isinstance(self.last_fetch_at, datetime.datetime):
            last_fetch_at = self.last_fetch_at.isoformat()
        else:
            last_fetch_at = self.last_fetch_at

        last_down_at: None | str | Unset
        if isinstance(self.last_down_at, Unset):
            last_down_at = UNSET
        elif isinstance(self.last_down_at, datetime.datetime):
            last_down_at = self.last_down_at.isoformat()
        else:
            last_down_at = self.last_down_at

        last_up_time: None | str | Unset
        if isinstance(self.last_up_time, Unset):
            last_up_time = UNSET
        elif isinstance(self.last_up_time, datetime.datetime):
            last_up_time = self.last_up_time.isoformat()
        else:
            last_up_time = self.last_up_time

        incidents_count: int | None | Unset
        if isinstance(self.incidents_count, Unset):
            incidents_count = UNSET
        else:
            incidents_count = self.incidents_count

        opened_incident_id: None | str | Unset
        if isinstance(self.opened_incident_id, Unset):
            opened_incident_id = UNSET
        elif isinstance(self.opened_incident_id, UUID):
            opened_incident_id = str(self.opened_incident_id)
        else:
            opened_incident_id = self.opened_incident_id

        settings: dict[str, Any] | None | Unset
        if isinstance(self.settings, Unset):
            settings = UNSET
        elif isinstance(self.settings, MonitorPublicDetailSchemaSettingsType0):
            settings = self.settings.to_dict()
        else:
            settings = self.settings

        realert_period: int | None | Unset
        if isinstance(self.realert_period, Unset):
            realert_period = UNSET
        else:
            realert_period = self.realert_period

        confirmation_period: int | None | Unset
        if isinstance(self.confirmation_period, Unset):
            confirmation_period = UNSET
        else:
            confirmation_period = self.confirmation_period

        recovery_period: int | None | Unset
        if isinstance(self.recovery_period, Unset):
            recovery_period = UNSET
        else:
            recovery_period = self.recovery_period

        open_incident_strategy: None | str | Unset
        if isinstance(self.open_incident_strategy, Unset):
            open_incident_strategy = UNSET
        elif isinstance(self.open_incident_strategy, IncidentStrategyEnum):
            open_incident_strategy = self.open_incident_strategy.value
        else:
            open_incident_strategy = self.open_incident_strategy

        close_incident_strategy: None | str | Unset
        if isinstance(self.close_incident_strategy, Unset):
            close_incident_strategy = UNSET
        elif isinstance(self.close_incident_strategy, IncidentStrategyEnum):
            close_incident_strategy = self.close_incident_strategy.value
        else:
            close_incident_strategy = self.close_incident_strategy

        meta: dict[str, Any] | None | Unset
        if isinstance(self.meta, Unset):
            meta = UNSET
        elif isinstance(self.meta, MonitorPublicDetailSchemaMetaType0):
            meta = self.meta.to_dict()
        else:
            meta = self.meta

        locations: list[dict[str, Any]] | None | Unset
        if isinstance(self.locations, Unset):
            locations = UNSET
        elif isinstance(self.locations, list):
            locations = []
            for locations_type_0_item_data in self.locations:
                locations_type_0_item = locations_type_0_item_data.to_dict()
                locations.append(locations_type_0_item)

        else:
            locations = self.locations

        tags: list[dict[str, Any]] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = []
            for tags_type_0_item_data in self.tags:
                tags_type_0_item = tags_type_0_item_data.to_dict()
                tags.append(tags_type_0_item)

        else:
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "uri": uri,
                "name": name,
                "monitor_type": monitor_type,
                "paused": paused,
                "fetch_interval": fetch_interval,
                "alerts_on": alerts_on,
                "created_at": created_at,
            }
        )
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if description is not UNSET:
            field_dict["description"] = description
        if is_down is not UNSET:
            field_dict["is_down"] = is_down
        if is_verified is not UNSET:
            field_dict["is_verified"] = is_verified
        if last_fetch_at is not UNSET:
            field_dict["last_fetch_at"] = last_fetch_at
        if last_down_at is not UNSET:
            field_dict["last_down_at"] = last_down_at
        if last_up_time is not UNSET:
            field_dict["last_up_time"] = last_up_time
        if incidents_count is not UNSET:
            field_dict["incidents_count"] = incidents_count
        if opened_incident_id is not UNSET:
            field_dict["opened_incident_id"] = opened_incident_id
        if settings is not UNSET:
            field_dict["settings"] = settings
        if realert_period is not UNSET:
            field_dict["realert_period"] = realert_period
        if confirmation_period is not UNSET:
            field_dict["confirmation_period"] = confirmation_period
        if recovery_period is not UNSET:
            field_dict["recovery_period"] = recovery_period
        if open_incident_strategy is not UNSET:
            field_dict["open_incident_strategy"] = open_incident_strategy
        if close_incident_strategy is not UNSET:
            field_dict["close_incident_strategy"] = close_incident_strategy
        if meta is not UNSET:
            field_dict["meta"] = meta
        if locations is not UNSET:
            field_dict["locations"] = locations
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location_schema import LocationSchema  # noqa: PLC0415
        from ..models.monitor_public_detail_schema_meta_type_0 import (
            MonitorPublicDetailSchemaMetaType0,  # noqa: PLC0415
        )
        from ..models.monitor_public_detail_schema_settings_type_0 import (
            MonitorPublicDetailSchemaSettingsType0,  # noqa: PLC0415
        )
        from ..models.tag_schema import TagSchema  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        uri = d.pop("uri")

        name = d.pop("name")

        monitor_type = MonitorTypeEnum(d.pop("monitor_type"))

        paused = d.pop("paused")

        fetch_interval = d.pop("fetch_interval")

        alerts_on = d.pop("alerts_on")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

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

        def _parse_timeout(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        timeout = _parse_timeout(d.pop("timeout", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_is_down(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_down = _parse_is_down(d.pop("is_down", UNSET))

        def _parse_is_verified(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_verified = _parse_is_verified(d.pop("is_verified", UNSET))

        def _parse_last_fetch_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_fetch_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_fetch_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_fetch_at = _parse_last_fetch_at(d.pop("last_fetch_at", UNSET))

        def _parse_last_down_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_down_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_down_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_down_at = _parse_last_down_at(d.pop("last_down_at", UNSET))

        def _parse_last_up_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_up_time_type_0 = datetime.datetime.fromisoformat(data)

                return last_up_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_up_time = _parse_last_up_time(d.pop("last_up_time", UNSET))

        def _parse_incidents_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        incidents_count = _parse_incidents_count(d.pop("incidents_count", UNSET))

        def _parse_opened_incident_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                opened_incident_id_type_0 = UUID(data)

                return opened_incident_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        opened_incident_id = _parse_opened_incident_id(d.pop("opened_incident_id", UNSET))

        def _parse_settings(data: object) -> MonitorPublicDetailSchemaSettingsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                settings_type_0 = MonitorPublicDetailSchemaSettingsType0.from_dict(data)

                return settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MonitorPublicDetailSchemaSettingsType0 | None | Unset, data)

        settings = _parse_settings(d.pop("settings", UNSET))

        def _parse_realert_period(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        realert_period = _parse_realert_period(d.pop("realert_period", UNSET))

        def _parse_confirmation_period(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        confirmation_period = _parse_confirmation_period(d.pop("confirmation_period", UNSET))

        def _parse_recovery_period(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        recovery_period = _parse_recovery_period(d.pop("recovery_period", UNSET))

        def _parse_open_incident_strategy(data: object) -> IncidentStrategyEnum | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                open_incident_strategy_type_0 = IncidentStrategyEnum(data)

                return open_incident_strategy_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IncidentStrategyEnum | None | Unset, data)

        open_incident_strategy = _parse_open_incident_strategy(d.pop("open_incident_strategy", UNSET))

        def _parse_close_incident_strategy(data: object) -> IncidentStrategyEnum | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                close_incident_strategy_type_0 = IncidentStrategyEnum(data)

                return close_incident_strategy_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IncidentStrategyEnum | None | Unset, data)

        close_incident_strategy = _parse_close_incident_strategy(d.pop("close_incident_strategy", UNSET))

        def _parse_meta(data: object) -> MonitorPublicDetailSchemaMetaType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = MonitorPublicDetailSchemaMetaType0.from_dict(data)

                return meta_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MonitorPublicDetailSchemaMetaType0 | None | Unset, data)

        meta = _parse_meta(d.pop("meta", UNSET))

        def _parse_locations(data: object) -> list[LocationSchema] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                locations_type_0 = []
                _locations_type_0 = data
                for locations_type_0_item_data in _locations_type_0:
                    locations_type_0_item = LocationSchema.from_dict(locations_type_0_item_data)

                    locations_type_0.append(locations_type_0_item)

                return locations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LocationSchema] | None | Unset, data)

        locations = _parse_locations(d.pop("locations", UNSET))

        def _parse_tags(data: object) -> list[TagSchema] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = []
                _tags_type_0 = data
                for tags_type_0_item_data in _tags_type_0:
                    tags_type_0_item = TagSchema.from_dict(tags_type_0_item_data)

                    tags_type_0.append(tags_type_0_item)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TagSchema] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        monitor_public_detail_schema = cls(
            id=id,
            uri=uri,
            name=name,
            monitor_type=monitor_type,
            paused=paused,
            fetch_interval=fetch_interval,
            alerts_on=alerts_on,
            created_at=created_at,
            group_id=group_id,
            timeout=timeout,
            description=description,
            is_down=is_down,
            is_verified=is_verified,
            last_fetch_at=last_fetch_at,
            last_down_at=last_down_at,
            last_up_time=last_up_time,
            incidents_count=incidents_count,
            opened_incident_id=opened_incident_id,
            settings=settings,
            realert_period=realert_period,
            confirmation_period=confirmation_period,
            recovery_period=recovery_period,
            open_incident_strategy=open_incident_strategy,
            close_incident_strategy=close_incident_strategy,
            meta=meta,
            locations=locations,
            tags=tags,
        )

        monitor_public_detail_schema.additional_properties = d
        return monitor_public_detail_schema

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
