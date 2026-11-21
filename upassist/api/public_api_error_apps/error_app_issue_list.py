from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.error_issue_paginated_schema import ErrorIssuePaginatedSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    error_app_id: UUID,
    *,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    q: None | str | Unset = UNSET,
    is_resolved: bool | None | Unset = UNSET,
    is_muted: bool | None | Unset = UNSET,
    environment: None | str | Unset = UNSET,
    level: None | str | Unset = UNSET,
    period: None | str | Unset = UNSET,
    sort: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    json_q: None | str | Unset
    if isinstance(q, Unset):
        json_q = UNSET
    else:
        json_q = q
    params["q"] = json_q

    json_is_resolved: bool | None | Unset
    if isinstance(is_resolved, Unset):
        json_is_resolved = UNSET
    else:
        json_is_resolved = is_resolved
    params["is_resolved"] = json_is_resolved

    json_is_muted: bool | None | Unset
    if isinstance(is_muted, Unset):
        json_is_muted = UNSET
    else:
        json_is_muted = is_muted
    params["is_muted"] = json_is_muted

    json_environment: None | str | Unset
    if isinstance(environment, Unset):
        json_environment = UNSET
    else:
        json_environment = environment
    params["environment"] = json_environment

    json_level: None | str | Unset
    if isinstance(level, Unset):
        json_level = UNSET
    else:
        json_level = level
    params["level"] = json_level

    json_period: None | str | Unset
    if isinstance(period, Unset):
        json_period = UNSET
    else:
        json_period = period
    params["period"] = json_period

    json_sort: None | str | Unset
    if isinstance(sort, Unset):
        json_sort = UNSET
    else:
        json_sort = sort
    params["sort"] = json_sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/error-apps/{error_app_id}/issues".format(
            error_app_id=quote(str(error_app_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | ErrorIssuePaginatedSchema | None:
    if response.status_code == 200:
        response_200 = ErrorIssuePaginatedSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | ErrorIssuePaginatedSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    error_app_id: UUID,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    q: None | str | Unset = UNSET,
    is_resolved: bool | None | Unset = UNSET,
    is_muted: bool | None | Unset = UNSET,
    environment: None | str | Unset = UNSET,
    level: None | str | Unset = UNSET,
    period: None | str | Unset = UNSET,
    sort: None | str | Unset = UNSET,
) -> Response[Error | ErrorIssuePaginatedSchema]:
    """ListIssues

    Args:
        error_app_id (UUID):
        page (int | Unset): Data page number Default: 1.
        per_page (int | Unset): Amount of results per page Default: 20.
        q (None | str | Unset):
        is_resolved (bool | None | Unset):
        is_muted (bool | None | Unset):
        environment (None | str | Unset):
        level (None | str | Unset):
        period (None | str | Unset):
        sort (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ErrorIssuePaginatedSchema]
    """

    kwargs = _get_kwargs(
        error_app_id=error_app_id,
        page=page,
        per_page=per_page,
        q=q,
        is_resolved=is_resolved,
        is_muted=is_muted,
        environment=environment,
        level=level,
        period=period,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    error_app_id: UUID,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    q: None | str | Unset = UNSET,
    is_resolved: bool | None | Unset = UNSET,
    is_muted: bool | None | Unset = UNSET,
    environment: None | str | Unset = UNSET,
    level: None | str | Unset = UNSET,
    period: None | str | Unset = UNSET,
    sort: None | str | Unset = UNSET,
) -> Error | ErrorIssuePaginatedSchema | None:
    """ListIssues

    Args:
        error_app_id (UUID):
        page (int | Unset): Data page number Default: 1.
        per_page (int | Unset): Amount of results per page Default: 20.
        q (None | str | Unset):
        is_resolved (bool | None | Unset):
        is_muted (bool | None | Unset):
        environment (None | str | Unset):
        level (None | str | Unset):
        period (None | str | Unset):
        sort (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ErrorIssuePaginatedSchema
    """

    return sync_detailed(
        error_app_id=error_app_id,
        client=client,
        page=page,
        per_page=per_page,
        q=q,
        is_resolved=is_resolved,
        is_muted=is_muted,
        environment=environment,
        level=level,
        period=period,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    error_app_id: UUID,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    q: None | str | Unset = UNSET,
    is_resolved: bool | None | Unset = UNSET,
    is_muted: bool | None | Unset = UNSET,
    environment: None | str | Unset = UNSET,
    level: None | str | Unset = UNSET,
    period: None | str | Unset = UNSET,
    sort: None | str | Unset = UNSET,
) -> Response[Error | ErrorIssuePaginatedSchema]:
    """ListIssues

    Args:
        error_app_id (UUID):
        page (int | Unset): Data page number Default: 1.
        per_page (int | Unset): Amount of results per page Default: 20.
        q (None | str | Unset):
        is_resolved (bool | None | Unset):
        is_muted (bool | None | Unset):
        environment (None | str | Unset):
        level (None | str | Unset):
        period (None | str | Unset):
        sort (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ErrorIssuePaginatedSchema]
    """

    kwargs = _get_kwargs(
        error_app_id=error_app_id,
        page=page,
        per_page=per_page,
        q=q,
        is_resolved=is_resolved,
        is_muted=is_muted,
        environment=environment,
        level=level,
        period=period,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    error_app_id: UUID,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    q: None | str | Unset = UNSET,
    is_resolved: bool | None | Unset = UNSET,
    is_muted: bool | None | Unset = UNSET,
    environment: None | str | Unset = UNSET,
    level: None | str | Unset = UNSET,
    period: None | str | Unset = UNSET,
    sort: None | str | Unset = UNSET,
) -> Error | ErrorIssuePaginatedSchema | None:
    """ListIssues

    Args:
        error_app_id (UUID):
        page (int | Unset): Data page number Default: 1.
        per_page (int | Unset): Amount of results per page Default: 20.
        q (None | str | Unset):
        is_resolved (bool | None | Unset):
        is_muted (bool | None | Unset):
        environment (None | str | Unset):
        level (None | str | Unset):
        period (None | str | Unset):
        sort (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ErrorIssuePaginatedSchema
    """

    return (
        await asyncio_detailed(
            error_app_id=error_app_id,
            client=client,
            page=page,
            per_page=per_page,
            q=q,
            is_resolved=is_resolved,
            is_muted=is_muted,
            environment=environment,
            level=level,
            period=period,
            sort=sort,
        )
    ).parsed
