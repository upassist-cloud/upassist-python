from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.layout_enum import LayoutEnum
from ..models.theme_enum import ThemeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.status_page_section_create_schema import StatusPageSectionCreateSchema


T = TypeVar("T", bound="StatusPageCreateSchema")


@_attrs_define
class StatusPageCreateSchema:
    """
    Attributes:
        name (str):
        subdomain (str):
        sections (list[StatusPageSectionCreateSchema]):
        group_id (None | Unset | UUID):
        custom_domain (None | str | Unset):
        company_url (None | str | Unset):
        support_url (None | str | Unset):
        announcement (None | str | Unset):
        days_display (int | Unset):  Default: 90.
        layout (LayoutEnum | Unset):
        theme (ThemeEnum | Unset):
        status_path (str | Unset):  Default: '/'.
        incidents_path (str | Unset):  Default: '/incidents/'.
        maintenance_path (str | Unset):  Default: '/maintenance/'.
        timezone (Any | Unset):  Default: 'Europe/Belfast'.
        password_on (bool | Unset):  Default: False.
        password (None | str | Unset):
        google_tag_id (None | str | Unset):
        hide_from_search_engines (bool | Unset):  Default: False.
        incident_minimum_length (int | Unset):  Default: 0.
        users_reports_subscription (bool | Unset):  Default: False.
        automatic_reports (bool | Unset):  Default: False.
        published (bool | Unset):  Default: True.
        custom_css (None | str | Unset):
        custom_js (None | str | Unset):
        embedded_announcement_active (bool | Unset):  Default: True.
        embedded_announcement_url (None | str | Unset):
        embedded_announcement_css (None | str | Unset):
    """

    name: str
    subdomain: str
    sections: list[StatusPageSectionCreateSchema]
    group_id: None | Unset | UUID = UNSET
    custom_domain: None | str | Unset = UNSET
    company_url: None | str | Unset = UNSET
    support_url: None | str | Unset = UNSET
    announcement: None | str | Unset = UNSET
    days_display: int | Unset = 90
    layout: LayoutEnum | Unset = UNSET
    theme: ThemeEnum | Unset = UNSET
    status_path: str | Unset = "/"
    incidents_path: str | Unset = "/incidents/"
    maintenance_path: str | Unset = "/maintenance/"
    timezone: Any | Unset = "Europe/Belfast"
    password_on: bool | Unset = False
    password: None | str | Unset = UNSET
    google_tag_id: None | str | Unset = UNSET
    hide_from_search_engines: bool | Unset = False
    incident_minimum_length: int | Unset = 0
    users_reports_subscription: bool | Unset = False
    automatic_reports: bool | Unset = False
    published: bool | Unset = True
    custom_css: None | str | Unset = UNSET
    custom_js: None | str | Unset = UNSET
    embedded_announcement_active: bool | Unset = True
    embedded_announcement_url: None | str | Unset = UNSET
    embedded_announcement_css: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        subdomain = self.subdomain

        sections = []
        for sections_item_data in self.sections:
            sections_item = sections_item_data.to_dict()
            sections.append(sections_item)

        group_id: None | str | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        elif isinstance(self.group_id, UUID):
            group_id = str(self.group_id)
        else:
            group_id = self.group_id

        custom_domain: None | str | Unset
        if isinstance(self.custom_domain, Unset):
            custom_domain = UNSET
        else:
            custom_domain = self.custom_domain

        company_url: None | str | Unset
        if isinstance(self.company_url, Unset):
            company_url = UNSET
        else:
            company_url = self.company_url

        support_url: None | str | Unset
        if isinstance(self.support_url, Unset):
            support_url = UNSET
        else:
            support_url = self.support_url

        announcement: None | str | Unset
        if isinstance(self.announcement, Unset):
            announcement = UNSET
        else:
            announcement = self.announcement

        days_display = self.days_display

        layout: str | Unset = UNSET
        if not isinstance(self.layout, Unset):
            layout = self.layout.value

        theme: str | Unset = UNSET
        if not isinstance(self.theme, Unset):
            theme = self.theme.value

        status_path = self.status_path

        incidents_path = self.incidents_path

        maintenance_path = self.maintenance_path

        timezone = self.timezone

        password_on = self.password_on

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        google_tag_id: None | str | Unset
        if isinstance(self.google_tag_id, Unset):
            google_tag_id = UNSET
        else:
            google_tag_id = self.google_tag_id

        hide_from_search_engines = self.hide_from_search_engines

        incident_minimum_length = self.incident_minimum_length

        users_reports_subscription = self.users_reports_subscription

        automatic_reports = self.automatic_reports

        published = self.published

        custom_css: None | str | Unset
        if isinstance(self.custom_css, Unset):
            custom_css = UNSET
        else:
            custom_css = self.custom_css

        custom_js: None | str | Unset
        if isinstance(self.custom_js, Unset):
            custom_js = UNSET
        else:
            custom_js = self.custom_js

        embedded_announcement_active = self.embedded_announcement_active

        embedded_announcement_url: None | str | Unset
        if isinstance(self.embedded_announcement_url, Unset):
            embedded_announcement_url = UNSET
        else:
            embedded_announcement_url = self.embedded_announcement_url

        embedded_announcement_css: None | str | Unset
        if isinstance(self.embedded_announcement_css, Unset):
            embedded_announcement_css = UNSET
        else:
            embedded_announcement_css = self.embedded_announcement_css

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "subdomain": subdomain,
                "sections": sections,
            }
        )
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if custom_domain is not UNSET:
            field_dict["custom_domain"] = custom_domain
        if company_url is not UNSET:
            field_dict["company_url"] = company_url
        if support_url is not UNSET:
            field_dict["support_url"] = support_url
        if announcement is not UNSET:
            field_dict["announcement"] = announcement
        if days_display is not UNSET:
            field_dict["days_display"] = days_display
        if layout is not UNSET:
            field_dict["layout"] = layout
        if theme is not UNSET:
            field_dict["theme"] = theme
        if status_path is not UNSET:
            field_dict["status_path"] = status_path
        if incidents_path is not UNSET:
            field_dict["incidents_path"] = incidents_path
        if maintenance_path is not UNSET:
            field_dict["maintenance_path"] = maintenance_path
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if password_on is not UNSET:
            field_dict["password_on"] = password_on
        if password is not UNSET:
            field_dict["password"] = password
        if google_tag_id is not UNSET:
            field_dict["google_tag_id"] = google_tag_id
        if hide_from_search_engines is not UNSET:
            field_dict["hide_from_search_engines"] = hide_from_search_engines
        if incident_minimum_length is not UNSET:
            field_dict["incident_minimum_length"] = incident_minimum_length
        if users_reports_subscription is not UNSET:
            field_dict["users_reports_subscription"] = users_reports_subscription
        if automatic_reports is not UNSET:
            field_dict["automatic_reports"] = automatic_reports
        if published is not UNSET:
            field_dict["published"] = published
        if custom_css is not UNSET:
            field_dict["custom_css"] = custom_css
        if custom_js is not UNSET:
            field_dict["custom_js"] = custom_js
        if embedded_announcement_active is not UNSET:
            field_dict["embedded_announcement_active"] = embedded_announcement_active
        if embedded_announcement_url is not UNSET:
            field_dict["embedded_announcement_url"] = embedded_announcement_url
        if embedded_announcement_css is not UNSET:
            field_dict["embedded_announcement_css"] = embedded_announcement_css

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.status_page_section_create_schema import StatusPageSectionCreateSchema  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        subdomain = d.pop("subdomain")

        sections = []
        _sections = d.pop("sections")
        for sections_item_data in _sections:
            sections_item = StatusPageSectionCreateSchema.from_dict(sections_item_data)

            sections.append(sections_item)

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

        def _parse_custom_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_domain = _parse_custom_domain(d.pop("custom_domain", UNSET))

        def _parse_company_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_url = _parse_company_url(d.pop("company_url", UNSET))

        def _parse_support_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_url = _parse_support_url(d.pop("support_url", UNSET))

        def _parse_announcement(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        announcement = _parse_announcement(d.pop("announcement", UNSET))

        days_display = d.pop("days_display", UNSET)

        _layout = d.pop("layout", UNSET)
        layout: LayoutEnum | Unset
        if isinstance(_layout, Unset):
            layout = UNSET
        else:
            layout = LayoutEnum(_layout)

        _theme = d.pop("theme", UNSET)
        theme: ThemeEnum | Unset
        if isinstance(_theme, Unset):
            theme = UNSET
        else:
            theme = ThemeEnum(_theme)

        status_path = d.pop("status_path", UNSET)

        incidents_path = d.pop("incidents_path", UNSET)

        maintenance_path = d.pop("maintenance_path", UNSET)

        timezone = d.pop("timezone", UNSET)

        password_on = d.pop("password_on", UNSET)

        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))

        def _parse_google_tag_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        google_tag_id = _parse_google_tag_id(d.pop("google_tag_id", UNSET))

        hide_from_search_engines = d.pop("hide_from_search_engines", UNSET)

        incident_minimum_length = d.pop("incident_minimum_length", UNSET)

        users_reports_subscription = d.pop("users_reports_subscription", UNSET)

        automatic_reports = d.pop("automatic_reports", UNSET)

        published = d.pop("published", UNSET)

        def _parse_custom_css(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_css = _parse_custom_css(d.pop("custom_css", UNSET))

        def _parse_custom_js(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_js = _parse_custom_js(d.pop("custom_js", UNSET))

        embedded_announcement_active = d.pop("embedded_announcement_active", UNSET)

        def _parse_embedded_announcement_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        embedded_announcement_url = _parse_embedded_announcement_url(d.pop("embedded_announcement_url", UNSET))

        def _parse_embedded_announcement_css(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        embedded_announcement_css = _parse_embedded_announcement_css(d.pop("embedded_announcement_css", UNSET))

        status_page_create_schema = cls(
            name=name,
            subdomain=subdomain,
            sections=sections,
            group_id=group_id,
            custom_domain=custom_domain,
            company_url=company_url,
            support_url=support_url,
            announcement=announcement,
            days_display=days_display,
            layout=layout,
            theme=theme,
            status_path=status_path,
            incidents_path=incidents_path,
            maintenance_path=maintenance_path,
            timezone=timezone,
            password_on=password_on,
            password=password,
            google_tag_id=google_tag_id,
            hide_from_search_engines=hide_from_search_engines,
            incident_minimum_length=incident_minimum_length,
            users_reports_subscription=users_reports_subscription,
            automatic_reports=automatic_reports,
            published=published,
            custom_css=custom_css,
            custom_js=custom_js,
            embedded_announcement_active=embedded_announcement_active,
            embedded_announcement_url=embedded_announcement_url,
            embedded_announcement_css=embedded_announcement_css,
        )

        status_page_create_schema.additional_properties = d
        return status_page_create_schema

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
