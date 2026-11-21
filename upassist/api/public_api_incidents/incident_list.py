from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.incident_public_paginated_schema import IncidentPublicPaginatedSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: None | str | Unset = UNSET,
    group_id: None | Unset | UUID = UNSET,
    heartbeat_id: None | Unset | UUID = UNSET,
    monitor_id: None | Unset | UUID = UNSET,
    site_alert_id: None | Unset | UUID = UNSET,
    is_finished: bool | None | Unset = UNSET,
    is_acknowledged: bool | None | Unset = UNSET,
    has_comments: bool | None | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_q: None | str | Unset
    if isinstance(q, Unset):
        json_q = UNSET
    else:
        json_q = q
    params["q"] = json_q

    json_group_id: None | str | Unset
    if isinstance(group_id, Unset):
        json_group_id = UNSET
    elif isinstance(group_id, UUID):
        json_group_id = str(group_id)
    else:
        json_group_id = group_id
    params["group_id"] = json_group_id

    json_heartbeat_id: None | str | Unset
    if isinstance(heartbeat_id, Unset):
        json_heartbeat_id = UNSET
    elif isinstance(heartbeat_id, UUID):
        json_heartbeat_id = str(heartbeat_id)
    else:
        json_heartbeat_id = heartbeat_id
    params["heartbeat_id"] = json_heartbeat_id

    json_monitor_id: None | str | Unset
    if isinstance(monitor_id, Unset):
        json_monitor_id = UNSET
    elif isinstance(monitor_id, UUID):
        json_monitor_id = str(monitor_id)
    else:
        json_monitor_id = monitor_id
    params["monitor_id"] = json_monitor_id

    json_site_alert_id: None | str | Unset
    if isinstance(site_alert_id, Unset):
        json_site_alert_id = UNSET
    elif isinstance(site_alert_id, UUID):
        json_site_alert_id = str(site_alert_id)
    else:
        json_site_alert_id = site_alert_id
    params["site_alert_id"] = json_site_alert_id

    json_is_finished: bool | None | Unset
    if isinstance(is_finished, Unset):
        json_is_finished = UNSET
    else:
        json_is_finished = is_finished
    params["is_finished"] = json_is_finished

    json_is_acknowledged: bool | None | Unset
    if isinstance(is_acknowledged, Unset):
        json_is_acknowledged = UNSET
    else:
        json_is_acknowledged = is_acknowledged
    params["is_acknowledged"] = json_is_acknowledged

    json_has_comments: bool | None | Unset
    if isinstance(has_comments, Unset):
        json_has_comments = UNSET
    else:
        json_has_comments = has_comments
    params["has_comments"] = json_has_comments

    params["page"] = page

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/incidents",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | IncidentPublicPaginatedSchema | None:
    if response.status_code == 200:
        response_200 = IncidentPublicPaginatedSchema.from_dict(response.json())

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
) -> Response[Error | IncidentPublicPaginatedSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    q: None | str | Unset = UNSET,
    group_id: None | Unset | UUID = UNSET,
    heartbeat_id: None | Unset | UUID = UNSET,
    monitor_id: None | Unset | UUID = UNSET,
    site_alert_id: None | Unset | UUID = UNSET,
    is_finished: bool | None | Unset = UNSET,
    is_acknowledged: bool | None | Unset = UNSET,
    has_comments: bool | None | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
) -> Response[Error | IncidentPublicPaginatedSchema]:
    """ListIncidents

    Args:
        q (None | str | Unset):
        group_id (None | Unset | UUID):
        heartbeat_id (None | Unset | UUID):
        monitor_id (None | Unset | UUID):
        site_alert_id (None | Unset | UUID):
        is_finished (bool | None | Unset):
        is_acknowledged (bool | None | Unset):
        has_comments (bool | None | Unset):
        page (int | Unset): Data page number Default: 1.
        per_page (int | Unset): Amount of results per page Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | IncidentPublicPaginatedSchema]
    """

    kwargs = _get_kwargs(
        q=q,
        group_id=group_id,
        heartbeat_id=heartbeat_id,
        monitor_id=monitor_id,
        site_alert_id=site_alert_id,
        is_finished=is_finished,
        is_acknowledged=is_acknowledged,
        has_comments=has_comments,
        page=page,
        per_page=per_page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    q: None | str | Unset = UNSET,
    group_id: None | Unset | UUID = UNSET,
    heartbeat_id: None | Unset | UUID = UNSET,
    monitor_id: None | Unset | UUID = UNSET,
    site_alert_id: None | Unset | UUID = UNSET,
    is_finished: bool | None | Unset = UNSET,
    is_acknowledged: bool | None | Unset = UNSET,
    has_comments: bool | None | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
) -> Error | IncidentPublicPaginatedSchema | None:
    """ListIncidents

    Args:
        q (None | str | Unset):
        group_id (None | Unset | UUID):
        heartbeat_id (None | Unset | UUID):
        monitor_id (None | Unset | UUID):
        site_alert_id (None | Unset | UUID):
        is_finished (bool | None | Unset):
        is_acknowledged (bool | None | Unset):
        has_comments (bool | None | Unset):
        page (int | Unset): Data page number Default: 1.
        per_page (int | Unset): Amount of results per page Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | IncidentPublicPaginatedSchema
    """

    return sync_detailed(
        client=client,
        q=q,
        group_id=group_id,
        heartbeat_id=heartbeat_id,
        monitor_id=monitor_id,
        site_alert_id=site_alert_id,
        is_finished=is_finished,
        is_acknowledged=is_acknowledged,
        has_comments=has_comments,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    q: None | str | Unset = UNSET,
    group_id: None | Unset | UUID = UNSET,
    heartbeat_id: None | Unset | UUID = UNSET,
    monitor_id: None | Unset | UUID = UNSET,
    site_alert_id: None | Unset | UUID = UNSET,
    is_finished: bool | None | Unset = UNSET,
    is_acknowledged: bool | None | Unset = UNSET,
    has_comments: bool | None | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
) -> Response[Error | IncidentPublicPaginatedSchema]:
    """ListIncidents

    Args:
        q (None | str | Unset):
        group_id (None | Unset | UUID):
        heartbeat_id (None | Unset | UUID):
        monitor_id (None | Unset | UUID):
        site_alert_id (None | Unset | UUID):
        is_finished (bool | None | Unset):
        is_acknowledged (bool | None | Unset):
        has_comments (bool | None | Unset):
        page (int | Unset): Data page number Default: 1.
        per_page (int | Unset): Amount of results per page Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | IncidentPublicPaginatedSchema]
    """

    kwargs = _get_kwargs(
        q=q,
        group_id=group_id,
        heartbeat_id=heartbeat_id,
        monitor_id=monitor_id,
        site_alert_id=site_alert_id,
        is_finished=is_finished,
        is_acknowledged=is_acknowledged,
        has_comments=has_comments,
        page=page,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    q: None | str | Unset = UNSET,
    group_id: None | Unset | UUID = UNSET,
    heartbeat_id: None | Unset | UUID = UNSET,
    monitor_id: None | Unset | UUID = UNSET,
    site_alert_id: None | Unset | UUID = UNSET,
    is_finished: bool | None | Unset = UNSET,
    is_acknowledged: bool | None | Unset = UNSET,
    has_comments: bool | None | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
) -> Error | IncidentPublicPaginatedSchema | None:
    """ListIncidents

    Args:
        q (None | str | Unset):
        group_id (None | Unset | UUID):
        heartbeat_id (None | Unset | UUID):
        monitor_id (None | Unset | UUID):
        site_alert_id (None | Unset | UUID):
        is_finished (bool | None | Unset):
        is_acknowledged (bool | None | Unset):
        has_comments (bool | None | Unset):
        page (int | Unset): Data page number Default: 1.
        per_page (int | Unset): Amount of results per page Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | IncidentPublicPaginatedSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            group_id=group_id,
            heartbeat_id=heartbeat_id,
            monitor_id=monitor_id,
            site_alert_id=site_alert_id,
            is_finished=is_finished,
            is_acknowledged=is_acknowledged,
            has_comments=has_comments,
            page=page,
            per_page=per_page,
        )
    ).parsed
