from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SiteSchema")


@_attrs_define
class SiteSchema:
    """
    Attributes:
        id (UUID):
        name (str):
        secret_token (str):
        public_access (bool):
        report_key (str):
        sample_rate (float):
        filter_localhost (bool):
        filter_bots (bool):
        collect_web_events (bool):
        collect_errors (bool):
        collect_extensions (bool):
        group_id (None | Unset | UUID):
        allowed_origins (list[str] | None | Unset):
        blocked_ips (list[str] | None | Unset):
        blocked_paths (list[str] | None | Unset):
        blocked_countries (list[str] | None | Unset):
    """

    id: UUID
    name: str
    secret_token: str
    public_access: bool
    report_key: str
    sample_rate: float
    filter_localhost: bool
    filter_bots: bool
    collect_web_events: bool
    collect_errors: bool
    collect_extensions: bool
    group_id: None | Unset | UUID = UNSET
    allowed_origins: list[str] | None | Unset = UNSET
    blocked_ips: list[str] | None | Unset = UNSET
    blocked_paths: list[str] | None | Unset = UNSET
    blocked_countries: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        secret_token = self.secret_token

        public_access = self.public_access

        report_key = self.report_key

        sample_rate = self.sample_rate

        filter_localhost = self.filter_localhost

        filter_bots = self.filter_bots

        collect_web_events = self.collect_web_events

        collect_errors = self.collect_errors

        collect_extensions = self.collect_extensions

        group_id: None | str | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        elif isinstance(self.group_id, UUID):
            group_id = str(self.group_id)
        else:
            group_id = self.group_id

        allowed_origins: list[str] | None | Unset
        if isinstance(self.allowed_origins, Unset):
            allowed_origins = UNSET
        elif isinstance(self.allowed_origins, list):
            allowed_origins = self.allowed_origins

        else:
            allowed_origins = self.allowed_origins

        blocked_ips: list[str] | None | Unset
        if isinstance(self.blocked_ips, Unset):
            blocked_ips = UNSET
        elif isinstance(self.blocked_ips, list):
            blocked_ips = []
            for blocked_ips_type_0_item_data in self.blocked_ips:
                blocked_ips_type_0_item: str
                blocked_ips_type_0_item = blocked_ips_type_0_item_data
                blocked_ips.append(blocked_ips_type_0_item)

        else:
            blocked_ips = self.blocked_ips

        blocked_paths: list[str] | None | Unset
        if isinstance(self.blocked_paths, Unset):
            blocked_paths = UNSET
        elif isinstance(self.blocked_paths, list):
            blocked_paths = self.blocked_paths

        else:
            blocked_paths = self.blocked_paths

        blocked_countries: list[str] | None | Unset
        if isinstance(self.blocked_countries, Unset):
            blocked_countries = UNSET
        elif isinstance(self.blocked_countries, list):
            blocked_countries = self.blocked_countries

        else:
            blocked_countries = self.blocked_countries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "secret_token": secret_token,
                "public_access": public_access,
                "report_key": report_key,
                "sample_rate": sample_rate,
                "filter_localhost": filter_localhost,
                "filter_bots": filter_bots,
                "collect_web_events": collect_web_events,
                "collect_errors": collect_errors,
                "collect_extensions": collect_extensions,
            }
        )
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if allowed_origins is not UNSET:
            field_dict["allowed_origins"] = allowed_origins
        if blocked_ips is not UNSET:
            field_dict["blocked_ips"] = blocked_ips
        if blocked_paths is not UNSET:
            field_dict["blocked_paths"] = blocked_paths
        if blocked_countries is not UNSET:
            field_dict["blocked_countries"] = blocked_countries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        secret_token = d.pop("secret_token")

        public_access = d.pop("public_access")

        report_key = d.pop("report_key")

        sample_rate = d.pop("sample_rate")

        filter_localhost = d.pop("filter_localhost")

        filter_bots = d.pop("filter_bots")

        collect_web_events = d.pop("collect_web_events")

        collect_errors = d.pop("collect_errors")

        collect_extensions = d.pop("collect_extensions")

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

        def _parse_allowed_origins(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_origins_type_0 = cast(list[str], data)

                return allowed_origins_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        allowed_origins = _parse_allowed_origins(d.pop("allowed_origins", UNSET))

        def _parse_blocked_ips(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                blocked_ips_type_0 = []
                _blocked_ips_type_0 = data
                for blocked_ips_type_0_item_data in _blocked_ips_type_0:

                    def _parse_blocked_ips_type_0_item(data: object) -> str:
                        return cast(str, data)

                    blocked_ips_type_0_item = _parse_blocked_ips_type_0_item(blocked_ips_type_0_item_data)

                    blocked_ips_type_0.append(blocked_ips_type_0_item)

                return blocked_ips_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        blocked_ips = _parse_blocked_ips(d.pop("blocked_ips", UNSET))

        def _parse_blocked_paths(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                blocked_paths_type_0 = cast(list[str], data)

                return blocked_paths_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        blocked_paths = _parse_blocked_paths(d.pop("blocked_paths", UNSET))

        def _parse_blocked_countries(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                blocked_countries_type_0 = cast(list[str], data)

                return blocked_countries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        blocked_countries = _parse_blocked_countries(d.pop("blocked_countries", UNSET))

        site_schema = cls(
            id=id,
            name=name,
            secret_token=secret_token,
            public_access=public_access,
            report_key=report_key,
            sample_rate=sample_rate,
            filter_localhost=filter_localhost,
            filter_bots=filter_bots,
            collect_web_events=collect_web_events,
            collect_errors=collect_errors,
            collect_extensions=collect_extensions,
            group_id=group_id,
            allowed_origins=allowed_origins,
            blocked_ips=blocked_ips,
            blocked_paths=blocked_paths,
            blocked_countries=blocked_countries,
        )

        site_schema.additional_properties = d
        return site_schema

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
