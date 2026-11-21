from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dashboard_total_count_schema import DashboardTotalCountSchema
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: None | str | Unset = UNSET,
    group_id: None | Unset | UUID = UNSET,
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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/dashboards",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DashboardTotalCountSchema | Error | None:
    if response.status_code == 200:
        response_200 = DashboardTotalCountSchema.from_dict(response.json())

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
) -> Response[DashboardTotalCountSchema | Error]:
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
) -> Response[DashboardTotalCountSchema | Error]:
    """ListDashboards

     List project dashboards.

    Requires dashboard:read scope.

    Args:
        q (None | str | Unset):
        group_id (None | Unset | UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DashboardTotalCountSchema | Error]
    """

    kwargs = _get_kwargs(
        q=q,
        group_id=group_id,
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
) -> DashboardTotalCountSchema | Error | None:
    """ListDashboards

     List project dashboards.

    Requires dashboard:read scope.

    Args:
        q (None | str | Unset):
        group_id (None | Unset | UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DashboardTotalCountSchema | Error
    """

    return sync_detailed(
        client=client,
        q=q,
        group_id=group_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    q: None | str | Unset = UNSET,
    group_id: None | Unset | UUID = UNSET,
) -> Response[DashboardTotalCountSchema | Error]:
    """ListDashboards

     List project dashboards.

    Requires dashboard:read scope.

    Args:
        q (None | str | Unset):
        group_id (None | Unset | UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DashboardTotalCountSchema | Error]
    """

    kwargs = _get_kwargs(
        q=q,
        group_id=group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    q: None | str | Unset = UNSET,
    group_id: None | Unset | UUID = UNSET,
) -> DashboardTotalCountSchema | Error | None:
    """ListDashboards

     List project dashboards.

    Requires dashboard:read scope.

    Args:
        q (None | str | Unset):
        group_id (None | Unset | UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DashboardTotalCountSchema | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            group_id=group_id,
        )
    ).parsed
