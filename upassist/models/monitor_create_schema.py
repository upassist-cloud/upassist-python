from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_strategy_enum import IncidentStrategyEnum
from ..models.monitor_type_enum import MonitorTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.endpoint_settings_create_schema import EndpointSettingsCreateSchema
    from ..models.monitor_create_schema_meta_type_0 import MonitorCreateSchemaMetaType0
    from ..models.ping_settings_create_schema import PingSettingsCreateSchema


T = TypeVar("T", bound="MonitorCreateSchema")


@_attrs_define
class MonitorCreateSchema:
    """
    Attributes:
        monitor_type (MonitorTypeEnum):
        uri (str): URL for ENDPOINT type, HOST/HOST+PORT/IP/IP+PORT for PING type
        settings (EndpointSettingsCreateSchema | PingSettingsCreateSchema):
        locations_ids (list[int]):
        group_id (None | Unset | UUID):
        name (None | str | Unset): Visible name of monitor, sets by default to shorten uri
        description (None | str | Unset):
        paused (bool | Unset):  Default: False.
        fetch_interval (int | Unset):  Default: 180.
        timeout (int | Unset):  Default: 8.
        alerts_on (bool | Unset):  Default: True.
        realert_period (int | None | Unset):  Default: 28800.
        open_incident_strategy (IncidentStrategyEnum | None | Unset):  Default: IncidentStrategyEnum.PERIOD.
        confirmation_period (int | None | Unset):
        close_incident_strategy (IncidentStrategyEnum | None | Unset):  Default: IncidentStrategyEnum.PERIOD.
        recovery_period (int | None | Unset):
        meta (MonitorCreateSchemaMetaType0 | None | Unset):
    """

    monitor_type: MonitorTypeEnum
    uri: str
    settings: EndpointSettingsCreateSchema | PingSettingsCreateSchema
    locations_ids: list[int]
    group_id: None | Unset | UUID = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    paused: bool | Unset = False
    fetch_interval: int | Unset = 180
    timeout: int | Unset = 8
    alerts_on: bool | Unset = True
    realert_period: int | None | Unset = 28800
    open_incident_strategy: IncidentStrategyEnum | None | Unset = IncidentStrategyEnum.PERIOD
    confirmation_period: int | None | Unset = UNSET
    close_incident_strategy: IncidentStrategyEnum | None | Unset = IncidentStrategyEnum.PERIOD
    recovery_period: int | None | Unset = UNSET
    meta: MonitorCreateSchemaMetaType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.endpoint_settings_create_schema import EndpointSettingsCreateSchema  # noqa: PLC0415
        from ..models.monitor_create_schema_meta_type_0 import MonitorCreateSchemaMetaType0  # noqa: PLC0415

        monitor_type = self.monitor_type.value

        uri = self.uri

        settings: dict[str, Any]
        if isinstance(self.settings, EndpointSettingsCreateSchema):
            settings = self.settings.to_dict()
        else:
            settings = self.settings.to_dict()

        locations_ids = self.locations_ids

        group_id: None | str | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        elif isinstance(self.group_id, UUID):
            group_id = str(self.group_id)
        else:
            group_id = self.group_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        paused = self.paused

        fetch_interval = self.fetch_interval

        timeout = self.timeout

        alerts_on = self.alerts_on

        realert_period: int | None | Unset
        if isinstance(self.realert_period, Unset):
            realert_period = UNSET
        else:
            realert_period = self.realert_period

        open_incident_strategy: None | str | Unset
        if isinstance(self.open_incident_strategy, Unset):
            open_incident_strategy = UNSET
        elif isinstance(self.open_incident_strategy, IncidentStrategyEnum):
            open_incident_strategy = self.open_incident_strategy.value
        else:
            open_incident_strategy = self.open_incident_strategy

        confirmation_period: int | None | Unset
        if isinstance(self.confirmation_period, Unset):
            confirmation_period = UNSET
        else:
            confirmation_period = self.confirmation_period

        close_incident_strategy: None | str | Unset
        if isinstance(self.close_incident_strategy, Unset):
            close_incident_strategy = UNSET
        elif isinstance(self.close_incident_strategy, IncidentStrategyEnum):
            close_incident_strategy = self.close_incident_strategy.value
        else:
            close_incident_strategy = self.close_incident_strategy

        recovery_period: int | None | Unset
        if isinstance(self.recovery_period, Unset):
            recovery_period = UNSET
        else:
            recovery_period = self.recovery_period

        meta: dict[str, Any] | None | Unset
        if isinstance(self.meta, Unset):
            meta = UNSET
        elif isinstance(self.meta, MonitorCreateSchemaMetaType0):
            meta = self.meta.to_dict()
        else:
            meta = self.meta

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "monitor_type": monitor_type,
                "uri": uri,
                "settings": settings,
                "locations_ids": locations_ids,
            }
        )
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if paused is not UNSET:
            field_dict["paused"] = paused
        if fetch_interval is not UNSET:
            field_dict["fetch_interval"] = fetch_interval
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if alerts_on is not UNSET:
            field_dict["alerts_on"] = alerts_on
        if realert_period is not UNSET:
            field_dict["realert_period"] = realert_period
        if open_incident_strategy is not UNSET:
            field_dict["open_incident_strategy"] = open_incident_strategy
        if confirmation_period is not UNSET:
            field_dict["confirmation_period"] = confirmation_period
        if close_incident_strategy is not UNSET:
            field_dict["close_incident_strategy"] = close_incident_strategy
        if recovery_period is not UNSET:
            field_dict["recovery_period"] = recovery_period
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.endpoint_settings_create_schema import EndpointSettingsCreateSchema  # noqa: PLC0415
        from ..models.monitor_create_schema_meta_type_0 import MonitorCreateSchemaMetaType0  # noqa: PLC0415
        from ..models.ping_settings_create_schema import PingSettingsCreateSchema  # noqa: PLC0415

        d = dict(src_dict)
        monitor_type = MonitorTypeEnum(d.pop("monitor_type"))

        uri = d.pop("uri")

        def _parse_settings(data: object) -> EndpointSettingsCreateSchema | PingSettingsCreateSchema:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                settings_type_0 = EndpointSettingsCreateSchema.from_dict(data)

                return settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            settings_type_1 = PingSettingsCreateSchema.from_dict(data)

            return settings_type_1

        settings = _parse_settings(d.pop("settings"))

        locations_ids = cast(list[int], d.pop("locations_ids"))

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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        paused = d.pop("paused", UNSET)

        fetch_interval = d.pop("fetch_interval", UNSET)

        timeout = d.pop("timeout", UNSET)

        alerts_on = d.pop("alerts_on", UNSET)

        def _parse_realert_period(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        realert_period = _parse_realert_period(d.pop("realert_period", UNSET))

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

        def _parse_confirmation_period(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        confirmation_period = _parse_confirmation_period(d.pop("confirmation_period", UNSET))

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

        def _parse_recovery_period(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        recovery_period = _parse_recovery_period(d.pop("recovery_period", UNSET))

        def _parse_meta(data: object) -> MonitorCreateSchemaMetaType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = MonitorCreateSchemaMetaType0.from_dict(data)

                return meta_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MonitorCreateSchemaMetaType0 | None | Unset, data)

        meta = _parse_meta(d.pop("meta", UNSET))

        monitor_create_schema = cls(
            monitor_type=monitor_type,
            uri=uri,
            settings=settings,
            locations_ids=locations_ids,
            group_id=group_id,
            name=name,
            description=description,
            paused=paused,
            fetch_interval=fetch_interval,
            timeout=timeout,
            alerts_on=alerts_on,
            realert_period=realert_period,
            open_incident_strategy=open_incident_strategy,
            confirmation_period=confirmation_period,
            close_incident_strategy=close_incident_strategy,
            recovery_period=recovery_period,
            meta=meta,
        )

        monitor_create_schema.additional_properties = d
        return monitor_create_schema

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
