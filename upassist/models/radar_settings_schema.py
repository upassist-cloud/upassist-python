from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.scanning_type_enum import ScanningTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.radar_settings_schema_cookies_type_0 import RadarSettingsSchemaCookiesType0


T = TypeVar("T", bound="RadarSettingsSchema")


@_attrs_define
class RadarSettingsSchema:
    """
    Attributes:
        id (UUID):
        max_redirects (int):
        pages_interval (float):
        resources_interval (float):
        use_cookies (bool):
        cut_scripts_tags (bool):
        track_title (bool):
        track_description (bool):
        track_h1 (bool):
        track_content (bool):
        scanning_type (ScanningTypeEnum):
        text_only (bool):
        check_interval (int):
        user_agent (None | str | Unset):
        cookies (None | RadarSettingsSchemaCookiesType0 | Unset):
        regexp (None | str | Unset):
    """

    id: UUID
    max_redirects: int
    pages_interval: float
    resources_interval: float
    use_cookies: bool
    cut_scripts_tags: bool
    track_title: bool
    track_description: bool
    track_h1: bool
    track_content: bool
    scanning_type: ScanningTypeEnum
    text_only: bool
    check_interval: int
    user_agent: None | str | Unset = UNSET
    cookies: None | RadarSettingsSchemaCookiesType0 | Unset = UNSET
    regexp: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.radar_settings_schema_cookies_type_0 import RadarSettingsSchemaCookiesType0  # noqa: PLC0415

        id = str(self.id)

        max_redirects = self.max_redirects

        pages_interval = self.pages_interval

        resources_interval = self.resources_interval

        use_cookies = self.use_cookies

        cut_scripts_tags = self.cut_scripts_tags

        track_title = self.track_title

        track_description = self.track_description

        track_h1 = self.track_h1

        track_content = self.track_content

        scanning_type = self.scanning_type.value

        text_only = self.text_only

        check_interval = self.check_interval

        user_agent: None | str | Unset
        if isinstance(self.user_agent, Unset):
            user_agent = UNSET
        else:
            user_agent = self.user_agent

        cookies: dict[str, Any] | None | Unset
        if isinstance(self.cookies, Unset):
            cookies = UNSET
        elif isinstance(self.cookies, RadarSettingsSchemaCookiesType0):
            cookies = self.cookies.to_dict()
        else:
            cookies = self.cookies

        regexp: None | str | Unset
        if isinstance(self.regexp, Unset):
            regexp = UNSET
        else:
            regexp = self.regexp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "max_redirects": max_redirects,
                "pages_interval": pages_interval,
                "resources_interval": resources_interval,
                "use_cookies": use_cookies,
                "cut_scripts_tags": cut_scripts_tags,
                "track_title": track_title,
                "track_description": track_description,
                "track_h1": track_h1,
                "track_content": track_content,
                "scanning_type": scanning_type,
                "text_only": text_only,
                "check_interval": check_interval,
            }
        )
        if user_agent is not UNSET:
            field_dict["user_agent"] = user_agent
        if cookies is not UNSET:
            field_dict["cookies"] = cookies
        if regexp is not UNSET:
            field_dict["regexp"] = regexp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.radar_settings_schema_cookies_type_0 import RadarSettingsSchemaCookiesType0  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        max_redirects = d.pop("max_redirects")

        pages_interval = d.pop("pages_interval")

        resources_interval = d.pop("resources_interval")

        use_cookies = d.pop("use_cookies")

        cut_scripts_tags = d.pop("cut_scripts_tags")

        track_title = d.pop("track_title")

        track_description = d.pop("track_description")

        track_h1 = d.pop("track_h1")

        track_content = d.pop("track_content")

        scanning_type = ScanningTypeEnum(d.pop("scanning_type"))

        text_only = d.pop("text_only")

        check_interval = d.pop("check_interval")

        def _parse_user_agent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_agent = _parse_user_agent(d.pop("user_agent", UNSET))

        def _parse_cookies(data: object) -> None | RadarSettingsSchemaCookiesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cookies_type_0 = RadarSettingsSchemaCookiesType0.from_dict(data)

                return cookies_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RadarSettingsSchemaCookiesType0 | Unset, data)

        cookies = _parse_cookies(d.pop("cookies", UNSET))

        def _parse_regexp(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        regexp = _parse_regexp(d.pop("regexp", UNSET))

        radar_settings_schema = cls(
            id=id,
            max_redirects=max_redirects,
            pages_interval=pages_interval,
            resources_interval=resources_interval,
            use_cookies=use_cookies,
            cut_scripts_tags=cut_scripts_tags,
            track_title=track_title,
            track_description=track_description,
            track_h1=track_h1,
            track_content=track_content,
            scanning_type=scanning_type,
            text_only=text_only,
            check_interval=check_interval,
            user_agent=user_agent,
            cookies=cookies,
            regexp=regexp,
        )

        radar_settings_schema.additional_properties = d
        return radar_settings_schema

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
