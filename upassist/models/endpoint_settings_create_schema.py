from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.request_method_enum import RequestMethodEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.endpoint_settings_create_schema_request_body_type_0 import (
        EndpointSettingsCreateSchemaRequestBodyType0,
    )
    from ..models.endpoint_settings_create_schema_request_headers_type_0 import (
        EndpointSettingsCreateSchemaRequestHeadersType0,
    )


T = TypeVar("T", bound="EndpointSettingsCreateSchema")


@_attrs_define
class EndpointSettingsCreateSchema:
    """
    Attributes:
        expected_status_codes (list[int] | None | Unset):
        request_method (RequestMethodEnum | Unset):
        request_querystring (None | str | Unset):
        request_headers (EndpointSettingsCreateSchemaRequestHeadersType0 | None | Unset):
        request_body (EndpointSettingsCreateSchemaRequestBodyType0 | list[Any] | None | Unset):
        request_allow_redirects (bool | Unset):  Default: False.
        request_max_redirects (int | Unset):  Default: 3.
        basic_auth_login (None | str | Unset):
        basic_auth_password (None | str | Unset):
        ssl_verification_on (bool | Unset):  Default: True.
        ssl_expiration_alert_before (int | None | Unset):
        ssl_expiration_realert_before (int | None | Unset):
        domain_expiration_alert_before (int | None | Unset):
        domain_expiration_realert_before (int | None | Unset):
    """

    expected_status_codes: list[int] | None | Unset = UNSET
    request_method: RequestMethodEnum | Unset = UNSET
    request_querystring: None | str | Unset = UNSET
    request_headers: EndpointSettingsCreateSchemaRequestHeadersType0 | None | Unset = UNSET
    request_body: EndpointSettingsCreateSchemaRequestBodyType0 | list[Any] | None | Unset = UNSET
    request_allow_redirects: bool | Unset = False
    request_max_redirects: int | Unset = 3
    basic_auth_login: None | str | Unset = UNSET
    basic_auth_password: None | str | Unset = UNSET
    ssl_verification_on: bool | Unset = True
    ssl_expiration_alert_before: int | None | Unset = UNSET
    ssl_expiration_realert_before: int | None | Unset = UNSET
    domain_expiration_alert_before: int | None | Unset = UNSET
    domain_expiration_realert_before: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.endpoint_settings_create_schema_request_body_type_0 import (
            EndpointSettingsCreateSchemaRequestBodyType0,  # noqa: PLC0415
        )
        from ..models.endpoint_settings_create_schema_request_headers_type_0 import (
            EndpointSettingsCreateSchemaRequestHeadersType0,  # noqa: PLC0415
        )

        expected_status_codes: list[int] | None | Unset
        if isinstance(self.expected_status_codes, Unset):
            expected_status_codes = UNSET
        elif isinstance(self.expected_status_codes, list):
            expected_status_codes = self.expected_status_codes

        else:
            expected_status_codes = self.expected_status_codes

        request_method: str | Unset = UNSET
        if not isinstance(self.request_method, Unset):
            request_method = self.request_method.value

        request_querystring: None | str | Unset
        if isinstance(self.request_querystring, Unset):
            request_querystring = UNSET
        else:
            request_querystring = self.request_querystring

        request_headers: dict[str, Any] | None | Unset
        if isinstance(self.request_headers, Unset):
            request_headers = UNSET
        elif isinstance(self.request_headers, EndpointSettingsCreateSchemaRequestHeadersType0):
            request_headers = self.request_headers.to_dict()
        else:
            request_headers = self.request_headers

        request_body: dict[str, Any] | list[Any] | None | Unset
        if isinstance(self.request_body, Unset):
            request_body = UNSET
        elif isinstance(self.request_body, EndpointSettingsCreateSchemaRequestBodyType0):
            request_body = self.request_body.to_dict()
        elif isinstance(self.request_body, list):
            request_body = self.request_body

        else:
            request_body = self.request_body

        request_allow_redirects = self.request_allow_redirects

        request_max_redirects = self.request_max_redirects

        basic_auth_login: None | str | Unset
        if isinstance(self.basic_auth_login, Unset):
            basic_auth_login = UNSET
        else:
            basic_auth_login = self.basic_auth_login

        basic_auth_password: None | str | Unset
        if isinstance(self.basic_auth_password, Unset):
            basic_auth_password = UNSET
        else:
            basic_auth_password = self.basic_auth_password

        ssl_verification_on = self.ssl_verification_on

        ssl_expiration_alert_before: int | None | Unset
        if isinstance(self.ssl_expiration_alert_before, Unset):
            ssl_expiration_alert_before = UNSET
        else:
            ssl_expiration_alert_before = self.ssl_expiration_alert_before

        ssl_expiration_realert_before: int | None | Unset
        if isinstance(self.ssl_expiration_realert_before, Unset):
            ssl_expiration_realert_before = UNSET
        else:
            ssl_expiration_realert_before = self.ssl_expiration_realert_before

        domain_expiration_alert_before: int | None | Unset
        if isinstance(self.domain_expiration_alert_before, Unset):
            domain_expiration_alert_before = UNSET
        else:
            domain_expiration_alert_before = self.domain_expiration_alert_before

        domain_expiration_realert_before: int | None | Unset
        if isinstance(self.domain_expiration_realert_before, Unset):
            domain_expiration_realert_before = UNSET
        else:
            domain_expiration_realert_before = self.domain_expiration_realert_before

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expected_status_codes is not UNSET:
            field_dict["expected_status_codes"] = expected_status_codes
        if request_method is not UNSET:
            field_dict["request_method"] = request_method
        if request_querystring is not UNSET:
            field_dict["request_querystring"] = request_querystring
        if request_headers is not UNSET:
            field_dict["request_headers"] = request_headers
        if request_body is not UNSET:
            field_dict["request_body"] = request_body
        if request_allow_redirects is not UNSET:
            field_dict["request_allow_redirects"] = request_allow_redirects
        if request_max_redirects is not UNSET:
            field_dict["request_max_redirects"] = request_max_redirects
        if basic_auth_login is not UNSET:
            field_dict["basic_auth_login"] = basic_auth_login
        if basic_auth_password is not UNSET:
            field_dict["basic_auth_password"] = basic_auth_password
        if ssl_verification_on is not UNSET:
            field_dict["ssl_verification_on"] = ssl_verification_on
        if ssl_expiration_alert_before is not UNSET:
            field_dict["ssl_expiration_alert_before"] = ssl_expiration_alert_before
        if ssl_expiration_realert_before is not UNSET:
            field_dict["ssl_expiration_realert_before"] = ssl_expiration_realert_before
        if domain_expiration_alert_before is not UNSET:
            field_dict["domain_expiration_alert_before"] = domain_expiration_alert_before
        if domain_expiration_realert_before is not UNSET:
            field_dict["domain_expiration_realert_before"] = domain_expiration_realert_before

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.endpoint_settings_create_schema_request_body_type_0 import (
            EndpointSettingsCreateSchemaRequestBodyType0,  # noqa: PLC0415
        )
        from ..models.endpoint_settings_create_schema_request_headers_type_0 import (
            EndpointSettingsCreateSchemaRequestHeadersType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_expected_status_codes(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                expected_status_codes_type_0 = cast(list[int], data)

                return expected_status_codes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        expected_status_codes = _parse_expected_status_codes(d.pop("expected_status_codes", UNSET))

        _request_method = d.pop("request_method", UNSET)
        request_method: RequestMethodEnum | Unset
        if isinstance(_request_method, Unset):
            request_method = UNSET
        else:
            request_method = RequestMethodEnum(_request_method)

        def _parse_request_querystring(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        request_querystring = _parse_request_querystring(d.pop("request_querystring", UNSET))

        def _parse_request_headers(data: object) -> EndpointSettingsCreateSchemaRequestHeadersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                request_headers_type_0 = EndpointSettingsCreateSchemaRequestHeadersType0.from_dict(data)

                return request_headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EndpointSettingsCreateSchemaRequestHeadersType0 | None | Unset, data)

        request_headers = _parse_request_headers(d.pop("request_headers", UNSET))

        def _parse_request_body(
            data: object,
        ) -> EndpointSettingsCreateSchemaRequestBodyType0 | list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                request_body_type_0 = EndpointSettingsCreateSchemaRequestBodyType0.from_dict(data)

                return request_body_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                request_body_type_1 = cast(list[Any], data)

                return request_body_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EndpointSettingsCreateSchemaRequestBodyType0 | list[Any] | None | Unset, data)

        request_body = _parse_request_body(d.pop("request_body", UNSET))

        request_allow_redirects = d.pop("request_allow_redirects", UNSET)

        request_max_redirects = d.pop("request_max_redirects", UNSET)

        def _parse_basic_auth_login(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        basic_auth_login = _parse_basic_auth_login(d.pop("basic_auth_login", UNSET))

        def _parse_basic_auth_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        basic_auth_password = _parse_basic_auth_password(d.pop("basic_auth_password", UNSET))

        ssl_verification_on = d.pop("ssl_verification_on", UNSET)

        def _parse_ssl_expiration_alert_before(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ssl_expiration_alert_before = _parse_ssl_expiration_alert_before(d.pop("ssl_expiration_alert_before", UNSET))

        def _parse_ssl_expiration_realert_before(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ssl_expiration_realert_before = _parse_ssl_expiration_realert_before(
            d.pop("ssl_expiration_realert_before", UNSET)
        )

        def _parse_domain_expiration_alert_before(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        domain_expiration_alert_before = _parse_domain_expiration_alert_before(
            d.pop("domain_expiration_alert_before", UNSET)
        )

        def _parse_domain_expiration_realert_before(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        domain_expiration_realert_before = _parse_domain_expiration_realert_before(
            d.pop("domain_expiration_realert_before", UNSET)
        )

        endpoint_settings_create_schema = cls(
            expected_status_codes=expected_status_codes,
            request_method=request_method,
            request_querystring=request_querystring,
            request_headers=request_headers,
            request_body=request_body,
            request_allow_redirects=request_allow_redirects,
            request_max_redirects=request_max_redirects,
            basic_auth_login=basic_auth_login,
            basic_auth_password=basic_auth_password,
            ssl_verification_on=ssl_verification_on,
            ssl_expiration_alert_before=ssl_expiration_alert_before,
            ssl_expiration_realert_before=ssl_expiration_realert_before,
            domain_expiration_alert_before=domain_expiration_alert_before,
            domain_expiration_realert_before=domain_expiration_realert_before,
        )

        endpoint_settings_create_schema.additional_properties = d
        return endpoint_settings_create_schema

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
