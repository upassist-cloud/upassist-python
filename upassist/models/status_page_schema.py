from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.layout_enum import LayoutEnum
from ..models.theme_enum import ThemeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusPageSchema")


@_attrs_define
class StatusPageSchema:
    """
    Attributes:
        id (UUID):
        project_id (UUID):
        name (str):
        subdomain (str): status.upassist.cloud custom subdomain
        days_display (int): Display last n days history
        layout (LayoutEnum):
        theme (ThemeEnum):
        password_on (bool): Is password required to enter status page
        status_path (str): Custom path to `Status` tab
        incidents_path (str): Custom path to `Previous incidents` tab
        maintenance_path (str): Custom path to `Maintenance` tab
        hide_from_search_engines (bool):
        incident_minimum_length (int): Display incident with length more than n seconds, `0` to display incidents
        users_reports_subscription (bool):
        automatic_reports (bool):
        published (bool): Is status page available for clients at all
        timezone (Any): Status page datetime timezone
        embedded_announcement_active (bool):
        group_id (None | Unset | UUID):
        custom_domain (None | str | Unset): Custom client subdomain
        company_url (None | str | Unset): Url for page logo
        support_url (None | str | Unset): Url for `Get in touch` button, blank to remove button
        announcement (None | str | Unset): Announcement
        logo (None | str | Unset): Custom page logo
        google_tag_id (None | str | Unset):
        custom_css (None | str | Unset):
        custom_js (None | str | Unset):
        embedded_announcement_url (None | str | Unset):
        embedded_announcement_css (None | str | Unset):
    """

    id: UUID
    project_id: UUID
    name: str
    subdomain: str
    days_display: int
    layout: LayoutEnum
    theme: ThemeEnum
    password_on: bool
    status_path: str
    incidents_path: str
    maintenance_path: str
    hide_from_search_engines: bool
    incident_minimum_length: int
    users_reports_subscription: bool
    automatic_reports: bool
    published: bool
    timezone: Any
    embedded_announcement_active: bool
    group_id: None | Unset | UUID = UNSET
    custom_domain: None | str | Unset = UNSET
    company_url: None | str | Unset = UNSET
    support_url: None | str | Unset = UNSET
    announcement: None | str | Unset = UNSET
    logo: None | str | Unset = UNSET
    google_tag_id: None | str | Unset = UNSET
    custom_css: None | str | Unset = UNSET
    custom_js: None | str | Unset = UNSET
    embedded_announcement_url: None | str | Unset = UNSET
    embedded_announcement_css: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        project_id = str(self.project_id)

        name = self.name

        subdomain = self.subdomain

        days_display = self.days_display

        layout = self.layout.value

        theme = self.theme.value

        password_on = self.password_on

        status_path = self.status_path

        incidents_path = self.incidents_path

        maintenance_path = self.maintenance_path

        hide_from_search_engines = self.hide_from_search_engines

        incident_minimum_length = self.incident_minimum_length

        users_reports_subscription = self.users_reports_subscription

        automatic_reports = self.automatic_reports

        published = self.published

        timezone = self.timezone

        embedded_announcement_active = self.embedded_announcement_active

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

        logo: None | str | Unset
        if isinstance(self.logo, Unset):
            logo = UNSET
        else:
            logo = self.logo

        google_tag_id: None | str | Unset
        if isinstance(self.google_tag_id, Unset):
            google_tag_id = UNSET
        else:
            google_tag_id = self.google_tag_id

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
                "id": id,
                "project_id": project_id,
                "name": name,
                "subdomain": subdomain,
                "days_display": days_display,
                "layout": layout,
                "theme": theme,
                "password_on": password_on,
                "status_path": status_path,
                "incidents_path": incidents_path,
                "maintenance_path": maintenance_path,
                "hide_from_search_engines": hide_from_search_engines,
                "incident_minimum_length": incident_minimum_length,
                "users_reports_subscription": users_reports_subscription,
                "automatic_reports": automatic_reports,
                "published": published,
                "timezone": timezone,
                "embedded_announcement_active": embedded_announcement_active,
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
        if logo is not UNSET:
            field_dict["logo"] = logo
        if google_tag_id is not UNSET:
            field_dict["google_tag_id"] = google_tag_id
        if custom_css is not UNSET:
            field_dict["custom_css"] = custom_css
        if custom_js is not UNSET:
            field_dict["custom_js"] = custom_js
        if embedded_announcement_url is not UNSET:
            field_dict["embedded_announcement_url"] = embedded_announcement_url
        if embedded_announcement_css is not UNSET:
            field_dict["embedded_announcement_css"] = embedded_announcement_css

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        project_id = UUID(d.pop("project_id"))

        name = d.pop("name")

        subdomain = d.pop("subdomain")

        days_display = d.pop("days_display")

        layout = LayoutEnum(d.pop("layout"))

        theme = ThemeEnum(d.pop("theme"))

        password_on = d.pop("password_on")

        status_path = d.pop("status_path")

        incidents_path = d.pop("incidents_path")

        maintenance_path = d.pop("maintenance_path")

        hide_from_search_engines = d.pop("hide_from_search_engines")

        incident_minimum_length = d.pop("incident_minimum_length")

        users_reports_subscription = d.pop("users_reports_subscription")

        automatic_reports = d.pop("automatic_reports")

        published = d.pop("published")

        timezone = d.pop("timezone")

        embedded_announcement_active = d.pop("embedded_announcement_active")

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

        def _parse_logo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo = _parse_logo(d.pop("logo", UNSET))

        def _parse_google_tag_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        google_tag_id = _parse_google_tag_id(d.pop("google_tag_id", UNSET))

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

        status_page_schema = cls(
            id=id,
            project_id=project_id,
            name=name,
            subdomain=subdomain,
            days_display=days_display,
            layout=layout,
            theme=theme,
            password_on=password_on,
            status_path=status_path,
            incidents_path=incidents_path,
            maintenance_path=maintenance_path,
            hide_from_search_engines=hide_from_search_engines,
            incident_minimum_length=incident_minimum_length,
            users_reports_subscription=users_reports_subscription,
            automatic_reports=automatic_reports,
            published=published,
            timezone=timezone,
            embedded_announcement_active=embedded_announcement_active,
            group_id=group_id,
            custom_domain=custom_domain,
            company_url=company_url,
            support_url=support_url,
            announcement=announcement,
            logo=logo,
            google_tag_id=google_tag_id,
            custom_css=custom_css,
            custom_js=custom_js,
            embedded_announcement_url=embedded_announcement_url,
            embedded_announcement_css=embedded_announcement_css,
        )

        status_page_schema.additional_properties = d
        return status_page_schema

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
