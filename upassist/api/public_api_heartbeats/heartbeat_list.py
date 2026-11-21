from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.heartbeat_paginated_schema import HeartbeatPaginatedSchema
from ...models.heartbeat_sorting_enum import HeartbeatSortingEnum
from ...models.sorting_ordering_enum import SortingOrderingEnum
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    q: None | str | Unset = UNSET,
    group_id: None | Unset | UUID = UNSET,
    tag_ids: list[UUID] | None | Unset = UNSET,
    sort_by: HeartbeatSortingEnum | None | Unset = UNSET,
    ordering: None | SortingOrderingEnum | Unset = UNSET,
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

    json_group_id: None | str | Unset
    if isinstance(group_id, Unset):
        json_group_id = UNSET
    elif isinstance(group_id, UUID):
        json_group_id = str(group_id)
    else:
        json_group_id = group_id
    params["group_id"] = json_group_id

    json_tag_ids: list[str] | None | Unset
    if isinstance(tag_ids, Unset):
        json_tag_ids = UNSET
    elif isinstance(tag_ids, list):
        json_tag_ids = []
        for tag_ids_type_0_item_data in tag_ids:
            tag_ids_type_0_item = str(tag_ids_type_0_item_data)
            json_tag_ids.append(tag_ids_type_0_item)

    else:
        json_tag_ids = tag_ids
    params["tag_ids"] = json_tag_ids

    json_sort_by: None | str | Unset
    if isinstance(sort_by, Unset):
        json_sort_by = UNSET
    elif isinstance(sort_by, HeartbeatSortingEnum):
        json_sort_by = sort_by.value
    else:
        json_sort_by = sort_by
    params["sort_by"] = json_sort_by

    json_ordering: None | str | Unset
    if isinstance(ordering, Unset):
        json_ordering = UNSET
    elif isinstance(ordering, SortingOrderingEnum):
        json_ordering = ordering.value
    else:
        json_ordering = ordering
    params["ordering"] = json_ordering

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/heartbeats",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | HeartbeatPaginatedSchema | None:
    if response.status_code == 200:
        response_200 = HeartbeatPaginatedSchema.from_dict(response.json())

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
) -> Response[Error | HeartbeatPaginatedSchema]:
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
    group_id: None | Unset | UUID = UNSET,
    tag_ids: list[UUID] | None | Unset = UNSET,
    sort_by: HeartbeatSortingEnum | None | Unset = UNSET,
    ordering: None | SortingOrderingEnum | Unset = UNSET,
) -> Response[Error | HeartbeatPaginatedSchema]:
    """ListHeartbeats

    Args:
        page (int | Unset): Data page number Default: 1.
        per_page (int | Unset): Amount of results per page Default: 20.
        q (None | str | Unset):
        group_id (None | Unset | UUID):
        tag_ids (list[UUID] | None | Unset):
        sort_by (HeartbeatSortingEnum | None | Unset):
        ordering (None | SortingOrderingEnum | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | HeartbeatPaginatedSchema]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        q=q,
        group_id=group_id,
        tag_ids=tag_ids,
        sort_by=sort_by,
        ordering=ordering,
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
    group_id: None | Unset | UUID = UNSET,
    tag_ids: list[UUID] | None | Unset = UNSET,
    sort_by: HeartbeatSortingEnum | None | Unset = UNSET,
    ordering: None | SortingOrderingEnum | Unset = UNSET,
) -> Error | HeartbeatPaginatedSchema | None:
    """ListHeartbeats

    Args:
        page (int | Unset): Data page number Default: 1.
        per_page (int | Unset): Amount of results per page Default: 20.
        q (None | str | Unset):
        group_id (None | Unset | UUID):
        tag_ids (list[UUID] | None | Unset):
        sort_by (HeartbeatSortingEnum | None | Unset):
        ordering (None | SortingOrderingEnum | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | HeartbeatPaginatedSchema
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        q=q,
        group_id=group_id,
        tag_ids=tag_ids,
        sort_by=sort_by,
        ordering=ordering,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    q: None | str | Unset = UNSET,
    group_id: None | Unset | UUID = UNSET,
    tag_ids: list[UUID] | None | Unset = UNSET,
    sort_by: HeartbeatSortingEnum | None | Unset = UNSET,
    ordering: None | SortingOrderingEnum | Unset = UNSET,
) -> Response[Error | HeartbeatPaginatedSchema]:
    """ListHeartbeats

    Args:
        page (int | Unset): Data page number Default: 1.
        per_page (int | Unset): Amount of results per page Default: 20.
        q (None | str | Unset):
        group_id (None | Unset | UUID):
        tag_ids (list[UUID] | None | Unset):
        sort_by (HeartbeatSortingEnum | None | Unset):
        ordering (None | SortingOrderingEnum | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | HeartbeatPaginatedSchema]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        q=q,
        group_id=group_id,
        tag_ids=tag_ids,
        sort_by=sort_by,
        ordering=ordering,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    q: None | str | Unset = UNSET,
    group_id: None | Unset | UUID = UNSET,
    tag_ids: list[UUID] | None | Unset = UNSET,
    sort_by: HeartbeatSortingEnum | None | Unset = UNSET,
    ordering: None | SortingOrderingEnum | Unset = UNSET,
) -> Error | HeartbeatPaginatedSchema | None:
    """ListHeartbeats

    Args:
        page (int | Unset): Data page number Default: 1.
        per_page (int | Unset): Amount of results per page Default: 20.
        q (None | str | Unset):
        group_id (None | Unset | UUID):
        tag_ids (list[UUID] | None | Unset):
        sort_by (HeartbeatSortingEnum | None | Unset):
        ordering (None | SortingOrderingEnum | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | HeartbeatPaginatedSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            q=q,
            group_id=group_id,
            tag_ids=tag_ids,
            sort_by=sort_by,
            ordering=ordering,
        )
    ).parsed
