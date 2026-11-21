from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.radar_page_paginated_schema import RadarPagePaginatedSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 1,
    per_page: int | Unset = 50,
    q: None | str | Unset = UNSET,
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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/radar/pages",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | RadarPagePaginatedSchema | None:
    if response.status_code == 200:
        response_200 = RadarPagePaginatedSchema.from_dict(response.json())

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
) -> Response[Error | RadarPagePaginatedSchema]:
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
    per_page: int | Unset = 50,
    q: None | str | Unset = UNSET,
) -> Response[Error | RadarPagePaginatedSchema]:
    """ListPages

    Args:
        page (int | Unset): Data page number Default: 1.
        per_page (int | Unset): Amount of results per page Default: 50.
        q (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RadarPagePaginatedSchema]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        q=q,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    per_page: int | Unset = 50,
    q: None | str | Unset = UNSET,
) -> Error | RadarPagePaginatedSchema | None:
    """ListPages

    Args:
        page (int | Unset): Data page number Default: 1.
        per_page (int | Unset): Amount of results per page Default: 50.
        q (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RadarPagePaginatedSchema
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        q=q,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    per_page: int | Unset = 50,
    q: None | str | Unset = UNSET,
) -> Response[Error | RadarPagePaginatedSchema]:
    """ListPages

    Args:
        page (int | Unset): Data page number Default: 1.
        per_page (int | Unset): Amount of results per page Default: 50.
        q (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RadarPagePaginatedSchema]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        q=q,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    per_page: int | Unset = 50,
    q: None | str | Unset = UNSET,
) -> Error | RadarPagePaginatedSchema | None:
    """ListPages

    Args:
        page (int | Unset): Data page number Default: 1.
        per_page (int | Unset): Amount of results per page Default: 50.
        q (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RadarPagePaginatedSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            q=q,
        )
    ).parsed
