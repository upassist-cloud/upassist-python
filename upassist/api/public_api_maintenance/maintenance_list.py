from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.maintenance_paginated_schema import MaintenancePaginatedSchema
from ...models.maintenance_timeline_type_enum import MaintenanceTimelineTypeEnum
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    q: None | str | Unset = UNSET,
    timeline_type: MaintenanceTimelineTypeEnum | None | Unset = UNSET,
    status_page_id: None | Unset | UUID = UNSET,
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

    json_timeline_type: None | str | Unset
    if isinstance(timeline_type, Unset):
        json_timeline_type = UNSET
    elif isinstance(timeline_type, MaintenanceTimelineTypeEnum):
        json_timeline_type = timeline_type.value
    else:
        json_timeline_type = timeline_type
    params["timeline_type"] = json_timeline_type

    json_status_page_id: None | str | Unset
    if isinstance(status_page_id, Unset):
        json_status_page_id = UNSET
    elif isinstance(status_page_id, UUID):
        json_status_page_id = str(status_page_id)
    else:
        json_status_page_id = status_page_id
    params["status_page_id"] = json_status_page_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/maintenance",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | MaintenancePaginatedSchema | None:
    if response.status_code == 200:
        response_200 = MaintenancePaginatedSchema.from_dict(response.json())

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
) -> Response[Error | MaintenancePaginatedSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    q: None | str | Unset = UNSET,
    timeline_type: MaintenanceTimelineTypeEnum | None | Unset = UNSET,
    status_page_id: None | Unset | UUID = UNSET,
) -> Response[Error | MaintenancePaginatedSchema]:
    """ListMaintenance

    Args:
        page (int | Unset): Data page number Default: 1.
        per_page (int | Unset): Amount of results per page Default: 20.
        q (None | str | Unset):
        timeline_type (MaintenanceTimelineTypeEnum | None | Unset):
        status_page_id (None | Unset | UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MaintenancePaginatedSchema]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        q=q,
        timeline_type=timeline_type,
        status_page_id=status_page_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    q: None | str | Unset = UNSET,
    timeline_type: MaintenanceTimelineTypeEnum | None | Unset = UNSET,
    status_page_id: None | Unset | UUID = UNSET,
) -> Error | MaintenancePaginatedSchema | None:
    """ListMaintenance

    Args:
        page (int | Unset): Data page number Default: 1.
        per_page (int | Unset): Amount of results per page Default: 20.
        q (None | str | Unset):
        timeline_type (MaintenanceTimelineTypeEnum | None | Unset):
        status_page_id (None | Unset | UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MaintenancePaginatedSchema
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        q=q,
        timeline_type=timeline_type,
        status_page_id=status_page_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    q: None | str | Unset = UNSET,
    timeline_type: MaintenanceTimelineTypeEnum | None | Unset = UNSET,
    status_page_id: None | Unset | UUID = UNSET,
) -> Response[Error | MaintenancePaginatedSchema]:
    """ListMaintenance

    Args:
        page (int | Unset): Data page number Default: 1.
        per_page (int | Unset): Amount of results per page Default: 20.
        q (None | str | Unset):
        timeline_type (MaintenanceTimelineTypeEnum | None | Unset):
        status_page_id (None | Unset | UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MaintenancePaginatedSchema]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        q=q,
        timeline_type=timeline_type,
        status_page_id=status_page_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    q: None | str | Unset = UNSET,
    timeline_type: MaintenanceTimelineTypeEnum | None | Unset = UNSET,
    status_page_id: None | Unset | UUID = UNSET,
) -> Error | MaintenancePaginatedSchema | None:
    """ListMaintenance

    Args:
        page (int | Unset): Data page number Default: 1.
        per_page (int | Unset): Amount of results per page Default: 20.
        q (None | str | Unset):
        timeline_type (MaintenanceTimelineTypeEnum | None | Unset):
        status_page_id (None | Unset | UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MaintenancePaginatedSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            q=q,
            timeline_type=timeline_type,
            status_page_id=status_page_id,
        )
    ).parsed
