from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RumSiteEventSchema")


@_attrs_define
class RumSiteEventSchema:
    """
    Attributes:
        session_id (UUID):
        client_key (str):
        event_name (str):
        environment (None | str | Unset):
        url (None | str | Unset):
        user_agent (None | str | Unset):
        os (None | str | Unset):
        device (None | str | Unset):
        browser (None | str | Unset):
        is_bot (bool | Unset):  Default: False.
        referrer (None | str | Unset):
        utm_source (None | str | Unset):
        utm_campaign (None | str | Unset):
        utm_medium (None | str | Unset):
        utm_content (None | str | Unset):
        utm_term (None | str | Unset):
        language (None | str | Unset):
        timezone (None | str | Unset):
        screen_width (int | None | Unset):
        page_load_dns (int | None | Unset):
        page_load_connect (int | None | Unset):
        page_load_ssl (int | None | Unset):
        page_load_ttfb (int | None | Unset):
        page_load_download (int | None | Unset):
        page_load_dom_content_loaded (int | None | Unset):
        page_load_render (int | None | Unset):
        page_load_total (int | None | Unset):
        page_load_transfer_size (int | None | Unset):
        connection_type (None | str | Unset):
        value (None | str | Unset):
        web_vital_cls (float | int | None | Unset):
        web_vital_fid (float | int | None | Unset):
        web_vital_lcp (float | int | None | Unset):
        error_type (None | str | Unset):
        message (None | str | Unset):
        lineno (int | None | Unset):
        colno (int | None | Unset):
        filename (None | str | Unset):
    """

    session_id: UUID
    client_key: str
    event_name: str
    environment: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    user_agent: None | str | Unset = UNSET
    os: None | str | Unset = UNSET
    device: None | str | Unset = UNSET
    browser: None | str | Unset = UNSET
    is_bot: bool | Unset = False
    referrer: None | str | Unset = UNSET
    utm_source: None | str | Unset = UNSET
    utm_campaign: None | str | Unset = UNSET
    utm_medium: None | str | Unset = UNSET
    utm_content: None | str | Unset = UNSET
    utm_term: None | str | Unset = UNSET
    language: None | str | Unset = UNSET
    timezone: None | str | Unset = UNSET
    screen_width: int | None | Unset = UNSET
    page_load_dns: int | None | Unset = UNSET
    page_load_connect: int | None | Unset = UNSET
    page_load_ssl: int | None | Unset = UNSET
    page_load_ttfb: int | None | Unset = UNSET
    page_load_download: int | None | Unset = UNSET
    page_load_dom_content_loaded: int | None | Unset = UNSET
    page_load_render: int | None | Unset = UNSET
    page_load_total: int | None | Unset = UNSET
    page_load_transfer_size: int | None | Unset = UNSET
    connection_type: None | str | Unset = UNSET
    value: None | str | Unset = UNSET
    web_vital_cls: float | int | None | Unset = UNSET
    web_vital_fid: float | int | None | Unset = UNSET
    web_vital_lcp: float | int | None | Unset = UNSET
    error_type: None | str | Unset = UNSET
    message: None | str | Unset = UNSET
    lineno: int | None | Unset = UNSET
    colno: int | None | Unset = UNSET
    filename: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        session_id = str(self.session_id)

        client_key = self.client_key

        event_name = self.event_name

        environment: None | str | Unset
        if isinstance(self.environment, Unset):
            environment = UNSET
        else:
            environment = self.environment

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        user_agent: None | str | Unset
        if isinstance(self.user_agent, Unset):
            user_agent = UNSET
        else:
            user_agent = self.user_agent

        os: None | str | Unset
        if isinstance(self.os, Unset):
            os = UNSET
        else:
            os = self.os

        device: None | str | Unset
        if isinstance(self.device, Unset):
            device = UNSET
        else:
            device = self.device

        browser: None | str | Unset
        if isinstance(self.browser, Unset):
            browser = UNSET
        else:
            browser = self.browser

        is_bot = self.is_bot

        referrer: None | str | Unset
        if isinstance(self.referrer, Unset):
            referrer = UNSET
        else:
            referrer = self.referrer

        utm_source: None | str | Unset
        if isinstance(self.utm_source, Unset):
            utm_source = UNSET
        else:
            utm_source = self.utm_source

        utm_campaign: None | str | Unset
        if isinstance(self.utm_campaign, Unset):
            utm_campaign = UNSET
        else:
            utm_campaign = self.utm_campaign

        utm_medium: None | str | Unset
        if isinstance(self.utm_medium, Unset):
            utm_medium = UNSET
        else:
            utm_medium = self.utm_medium

        utm_content: None | str | Unset
        if isinstance(self.utm_content, Unset):
            utm_content = UNSET
        else:
            utm_content = self.utm_content

        utm_term: None | str | Unset
        if isinstance(self.utm_term, Unset):
            utm_term = UNSET
        else:
            utm_term = self.utm_term

        language: None | str | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        timezone: None | str | Unset
        if isinstance(self.timezone, Unset):
            timezone = UNSET
        else:
            timezone = self.timezone

        screen_width: int | None | Unset
        if isinstance(self.screen_width, Unset):
            screen_width = UNSET
        else:
            screen_width = self.screen_width

        page_load_dns: int | None | Unset
        if isinstance(self.page_load_dns, Unset):
            page_load_dns = UNSET
        else:
            page_load_dns = self.page_load_dns

        page_load_connect: int | None | Unset
        if isinstance(self.page_load_connect, Unset):
            page_load_connect = UNSET
        else:
            page_load_connect = self.page_load_connect

        page_load_ssl: int | None | Unset
        if isinstance(self.page_load_ssl, Unset):
            page_load_ssl = UNSET
        else:
            page_load_ssl = self.page_load_ssl

        page_load_ttfb: int | None | Unset
        if isinstance(self.page_load_ttfb, Unset):
            page_load_ttfb = UNSET
        else:
            page_load_ttfb = self.page_load_ttfb

        page_load_download: int | None | Unset
        if isinstance(self.page_load_download, Unset):
            page_load_download = UNSET
        else:
            page_load_download = self.page_load_download

        page_load_dom_content_loaded: int | None | Unset
        if isinstance(self.page_load_dom_content_loaded, Unset):
            page_load_dom_content_loaded = UNSET
        else:
            page_load_dom_content_loaded = self.page_load_dom_content_loaded

        page_load_render: int | None | Unset
        if isinstance(self.page_load_render, Unset):
            page_load_render = UNSET
        else:
            page_load_render = self.page_load_render

        page_load_total: int | None | Unset
        if isinstance(self.page_load_total, Unset):
            page_load_total = UNSET
        else:
            page_load_total = self.page_load_total

        page_load_transfer_size: int | None | Unset
        if isinstance(self.page_load_transfer_size, Unset):
            page_load_transfer_size = UNSET
        else:
            page_load_transfer_size = self.page_load_transfer_size

        connection_type: None | str | Unset
        if isinstance(self.connection_type, Unset):
            connection_type = UNSET
        else:
            connection_type = self.connection_type

        value: None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        web_vital_cls: float | int | None | Unset
        if isinstance(self.web_vital_cls, Unset):
            web_vital_cls = UNSET
        else:
            web_vital_cls = self.web_vital_cls

        web_vital_fid: float | int | None | Unset
        if isinstance(self.web_vital_fid, Unset):
            web_vital_fid = UNSET
        else:
            web_vital_fid = self.web_vital_fid

        web_vital_lcp: float | int | None | Unset
        if isinstance(self.web_vital_lcp, Unset):
            web_vital_lcp = UNSET
        else:
            web_vital_lcp = self.web_vital_lcp

        error_type: None | str | Unset
        if isinstance(self.error_type, Unset):
            error_type = UNSET
        else:
            error_type = self.error_type

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        lineno: int | None | Unset
        if isinstance(self.lineno, Unset):
            lineno = UNSET
        else:
            lineno = self.lineno

        colno: int | None | Unset
        if isinstance(self.colno, Unset):
            colno = UNSET
        else:
            colno = self.colno

        filename: None | str | Unset
        if isinstance(self.filename, Unset):
            filename = UNSET
        else:
            filename = self.filename

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "session_id": session_id,
                "client_key": client_key,
                "event_name": event_name,
            }
        )
        if environment is not UNSET:
            field_dict["environment"] = environment
        if url is not UNSET:
            field_dict["url"] = url
        if user_agent is not UNSET:
            field_dict["user_agent"] = user_agent
        if os is not UNSET:
            field_dict["os"] = os
        if device is not UNSET:
            field_dict["device"] = device
        if browser is not UNSET:
            field_dict["browser"] = browser
        if is_bot is not UNSET:
            field_dict["is_bot"] = is_bot
        if referrer is not UNSET:
            field_dict["referrer"] = referrer
        if utm_source is not UNSET:
            field_dict["utm_source"] = utm_source
        if utm_campaign is not UNSET:
            field_dict["utm_campaign"] = utm_campaign
        if utm_medium is not UNSET:
            field_dict["utm_medium"] = utm_medium
        if utm_content is not UNSET:
            field_dict["utm_content"] = utm_content
        if utm_term is not UNSET:
            field_dict["utm_term"] = utm_term
        if language is not UNSET:
            field_dict["language"] = language
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if screen_width is not UNSET:
            field_dict["screen_width"] = screen_width
        if page_load_dns is not UNSET:
            field_dict["page_load_dns"] = page_load_dns
        if page_load_connect is not UNSET:
            field_dict["page_load_connect"] = page_load_connect
        if page_load_ssl is not UNSET:
            field_dict["page_load_ssl"] = page_load_ssl
        if page_load_ttfb is not UNSET:
            field_dict["page_load_ttfb"] = page_load_ttfb
        if page_load_download is not UNSET:
            field_dict["page_load_download"] = page_load_download
        if page_load_dom_content_loaded is not UNSET:
            field_dict["page_load_dom_content_loaded"] = page_load_dom_content_loaded
        if page_load_render is not UNSET:
            field_dict["page_load_render"] = page_load_render
        if page_load_total is not UNSET:
            field_dict["page_load_total"] = page_load_total
        if page_load_transfer_size is not UNSET:
            field_dict["page_load_transfer_size"] = page_load_transfer_size
        if connection_type is not UNSET:
            field_dict["connection_type"] = connection_type
        if value is not UNSET:
            field_dict["value"] = value
        if web_vital_cls is not UNSET:
            field_dict["web_vital_cls"] = web_vital_cls
        if web_vital_fid is not UNSET:
            field_dict["web_vital_fid"] = web_vital_fid
        if web_vital_lcp is not UNSET:
            field_dict["web_vital_lcp"] = web_vital_lcp
        if error_type is not UNSET:
            field_dict["error_type"] = error_type
        if message is not UNSET:
            field_dict["message"] = message
        if lineno is not UNSET:
            field_dict["lineno"] = lineno
        if colno is not UNSET:
            field_dict["colno"] = colno
        if filename is not UNSET:
            field_dict["filename"] = filename

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        session_id = UUID(d.pop("session_id"))

        client_key = d.pop("client_key")

        event_name = d.pop("event_name")

        def _parse_environment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        environment = _parse_environment(d.pop("environment", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_user_agent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_agent = _parse_user_agent(d.pop("user_agent", UNSET))

        def _parse_os(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        os = _parse_os(d.pop("os", UNSET))

        def _parse_device(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device = _parse_device(d.pop("device", UNSET))

        def _parse_browser(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        browser = _parse_browser(d.pop("browser", UNSET))

        is_bot = d.pop("is_bot", UNSET)

        def _parse_referrer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        referrer = _parse_referrer(d.pop("referrer", UNSET))

        def _parse_utm_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        utm_source = _parse_utm_source(d.pop("utm_source", UNSET))

        def _parse_utm_campaign(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        utm_campaign = _parse_utm_campaign(d.pop("utm_campaign", UNSET))

        def _parse_utm_medium(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        utm_medium = _parse_utm_medium(d.pop("utm_medium", UNSET))

        def _parse_utm_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        utm_content = _parse_utm_content(d.pop("utm_content", UNSET))

        def _parse_utm_term(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        utm_term = _parse_utm_term(d.pop("utm_term", UNSET))

        def _parse_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language = _parse_language(d.pop("language", UNSET))

        def _parse_timezone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        timezone = _parse_timezone(d.pop("timezone", UNSET))

        def _parse_screen_width(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        screen_width = _parse_screen_width(d.pop("screen_width", UNSET))

        def _parse_page_load_dns(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        page_load_dns = _parse_page_load_dns(d.pop("page_load_dns", UNSET))

        def _parse_page_load_connect(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        page_load_connect = _parse_page_load_connect(d.pop("page_load_connect", UNSET))

        def _parse_page_load_ssl(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        page_load_ssl = _parse_page_load_ssl(d.pop("page_load_ssl", UNSET))

        def _parse_page_load_ttfb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        page_load_ttfb = _parse_page_load_ttfb(d.pop("page_load_ttfb", UNSET))

        def _parse_page_load_download(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        page_load_download = _parse_page_load_download(d.pop("page_load_download", UNSET))

        def _parse_page_load_dom_content_loaded(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        page_load_dom_content_loaded = _parse_page_load_dom_content_loaded(d.pop("page_load_dom_content_loaded", UNSET))

        def _parse_page_load_render(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        page_load_render = _parse_page_load_render(d.pop("page_load_render", UNSET))

        def _parse_page_load_total(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        page_load_total = _parse_page_load_total(d.pop("page_load_total", UNSET))

        def _parse_page_load_transfer_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        page_load_transfer_size = _parse_page_load_transfer_size(d.pop("page_load_transfer_size", UNSET))

        def _parse_connection_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        connection_type = _parse_connection_type(d.pop("connection_type", UNSET))

        def _parse_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        def _parse_web_vital_cls(data: object) -> float | int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | int | None | Unset, data)

        web_vital_cls = _parse_web_vital_cls(d.pop("web_vital_cls", UNSET))

        def _parse_web_vital_fid(data: object) -> float | int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | int | None | Unset, data)

        web_vital_fid = _parse_web_vital_fid(d.pop("web_vital_fid", UNSET))

        def _parse_web_vital_lcp(data: object) -> float | int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | int | None | Unset, data)

        web_vital_lcp = _parse_web_vital_lcp(d.pop("web_vital_lcp", UNSET))

        def _parse_error_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_type = _parse_error_type(d.pop("error_type", UNSET))

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_lineno(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lineno = _parse_lineno(d.pop("lineno", UNSET))

        def _parse_colno(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        colno = _parse_colno(d.pop("colno", UNSET))

        def _parse_filename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filename = _parse_filename(d.pop("filename", UNSET))

        rum_site_event_schema = cls(
            session_id=session_id,
            client_key=client_key,
            event_name=event_name,
            environment=environment,
            url=url,
            user_agent=user_agent,
            os=os,
            device=device,
            browser=browser,
            is_bot=is_bot,
            referrer=referrer,
            utm_source=utm_source,
            utm_campaign=utm_campaign,
            utm_medium=utm_medium,
            utm_content=utm_content,
            utm_term=utm_term,
            language=language,
            timezone=timezone,
            screen_width=screen_width,
            page_load_dns=page_load_dns,
            page_load_connect=page_load_connect,
            page_load_ssl=page_load_ssl,
            page_load_ttfb=page_load_ttfb,
            page_load_download=page_load_download,
            page_load_dom_content_loaded=page_load_dom_content_loaded,
            page_load_render=page_load_render,
            page_load_total=page_load_total,
            page_load_transfer_size=page_load_transfer_size,
            connection_type=connection_type,
            value=value,
            web_vital_cls=web_vital_cls,
            web_vital_fid=web_vital_fid,
            web_vital_lcp=web_vital_lcp,
            error_type=error_type,
            message=message,
            lineno=lineno,
            colno=colno,
            filename=filename,
        )

        rum_site_event_schema.additional_properties = d
        return rum_site_event_schema

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
