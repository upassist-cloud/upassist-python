from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.scanning_type_enum import ScanningTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.radar_settings_update_schema_cookies_type_0 import RadarSettingsUpdateSchemaCookiesType0


T = TypeVar("T", bound="RadarSettingsUpdateSchema")


@_attrs_define
class RadarSettingsUpdateSchema:
    """
    Attributes:
        scanning_type (ScanningTypeEnum):
        max_redirects (int | Unset):  Default: 5.
        user_agent (None | str | Unset):
        pages_interval (float | Unset):  Default: 0.05.
        resources_interval (float | Unset):  Default: 0.05.
        use_cookies (bool | Unset):  Default: False.
        cookies (None | RadarSettingsUpdateSchemaCookiesType0 | Unset):
        cut_scripts_tags (bool | Unset):  Default: False.
        track_title (bool | Unset):  Default: True.
        track_description (bool | Unset):  Default: True.
        track_h1 (bool | Unset):  Default: True.
        track_content (bool | Unset):  Default: True.
        regexp (None | str | Unset):
        text_only (bool | Unset):  Default: False.
        check_interval (int | Unset):  Default: 86400.
    """

    scanning_type: ScanningTypeEnum
    max_redirects: int | Unset = 5
    user_agent: None | str | Unset = UNSET
    pages_interval: float | Unset = 0.05
    resources_interval: float | Unset = 0.05
    use_cookies: bool | Unset = False
    cookies: None | RadarSettingsUpdateSchemaCookiesType0 | Unset = UNSET
    cut_scripts_tags: bool | Unset = False
    track_title: bool | Unset = True
    track_description: bool | Unset = True
    track_h1: bool | Unset = True
    track_content: bool | Unset = True
    regexp: None | str | Unset = UNSET
    text_only: bool | Unset = False
    check_interval: int | Unset = 86400
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.radar_settings_update_schema_cookies_type_0 import (
            RadarSettingsUpdateSchemaCookiesType0,  # noqa: PLC0415
        )

        scanning_type = self.scanning_type.value

        max_redirects = self.max_redirects

        user_agent: None | str | Unset
        if isinstance(self.user_agent, Unset):
            user_agent = UNSET
        else:
            user_agent = self.user_agent

        pages_interval = self.pages_interval

        resources_interval = self.resources_interval

        use_cookies = self.use_cookies

        cookies: dict[str, Any] | None | Unset
        if isinstance(self.cookies, Unset):
            cookies = UNSET
        elif isinstance(self.cookies, RadarSettingsUpdateSchemaCookiesType0):
            cookies = self.cookies.to_dict()
        else:
            cookies = self.cookies

        cut_scripts_tags = self.cut_scripts_tags

        track_title = self.track_title

        track_description = self.track_description

        track_h1 = self.track_h1

        track_content = self.track_content

        regexp: None | str | Unset
        if isinstance(self.regexp, Unset):
            regexp = UNSET
        else:
            regexp = self.regexp

        text_only = self.text_only

        check_interval = self.check_interval

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scanning_type": scanning_type,
            }
        )
        if max_redirects is not UNSET:
            field_dict["max_redirects"] = max_redirects
        if user_agent is not UNSET:
            field_dict["user_agent"] = user_agent
        if pages_interval is not UNSET:
            field_dict["pages_interval"] = pages_interval
        if resources_interval is not UNSET:
            field_dict["resources_interval"] = resources_interval
        if use_cookies is not UNSET:
            field_dict["use_cookies"] = use_cookies
        if cookies is not UNSET:
            field_dict["cookies"] = cookies
        if cut_scripts_tags is not UNSET:
            field_dict["cut_scripts_tags"] = cut_scripts_tags
        if track_title is not UNSET:
            field_dict["track_title"] = track_title
        if track_description is not UNSET:
            field_dict["track_description"] = track_description
        if track_h1 is not UNSET:
            field_dict["track_h1"] = track_h1
        if track_content is not UNSET:
            field_dict["track_content"] = track_content
        if regexp is not UNSET:
            field_dict["regexp"] = regexp
        if text_only is not UNSET:
            field_dict["text_only"] = text_only
        if check_interval is not UNSET:
            field_dict["check_interval"] = check_interval

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.radar_settings_update_schema_cookies_type_0 import (
            RadarSettingsUpdateSchemaCookiesType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        scanning_type = ScanningTypeEnum(d.pop("scanning_type"))

        max_redirects = d.pop("max_redirects", UNSET)

        def _parse_user_agent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_agent = _parse_user_agent(d.pop("user_agent", UNSET))

        pages_interval = d.pop("pages_interval", UNSET)

        resources_interval = d.pop("resources_interval", UNSET)

        use_cookies = d.pop("use_cookies", UNSET)

        def _parse_cookies(data: object) -> None | RadarSettingsUpdateSchemaCookiesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cookies_type_0 = RadarSettingsUpdateSchemaCookiesType0.from_dict(data)

                return cookies_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RadarSettingsUpdateSchemaCookiesType0 | Unset, data)

        cookies = _parse_cookies(d.pop("cookies", UNSET))

        cut_scripts_tags = d.pop("cut_scripts_tags", UNSET)

        track_title = d.pop("track_title", UNSET)

        track_description = d.pop("track_description", UNSET)

        track_h1 = d.pop("track_h1", UNSET)

        track_content = d.pop("track_content", UNSET)

        def _parse_regexp(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        regexp = _parse_regexp(d.pop("regexp", UNSET))

        text_only = d.pop("text_only", UNSET)

        check_interval = d.pop("check_interval", UNSET)

        radar_settings_update_schema = cls(
            scanning_type=scanning_type,
            max_redirects=max_redirects,
            user_agent=user_agent,
            pages_interval=pages_interval,
            resources_interval=resources_interval,
            use_cookies=use_cookies,
            cookies=cookies,
            cut_scripts_tags=cut_scripts_tags,
            track_title=track_title,
            track_description=track_description,
            track_h1=track_h1,
            track_content=track_content,
            regexp=regexp,
            text_only=text_only,
            check_interval=check_interval,
        )

        radar_settings_update_schema.additional_properties = d
        return radar_settings_update_schema

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
