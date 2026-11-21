from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dashboard_detail_schema import DashboardDetailSchema
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    dashboard_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/dashboards/{dashboard_id}".format(
            dashboard_id=quote(str(dashboard_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DashboardDetailSchema | Error | None:
    if response.status_code == 200:
        response_200 = DashboardDetailSchema.from_dict(response.json())

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
) -> Response[DashboardDetailSchema | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dashboard_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[DashboardDetailSchema | Error]:
    """Detail

     Get full details of a dashboard with its sections, charts, and queries.

    Requires dashboard:read scope.

    Args:
        dashboard_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DashboardDetailSchema | Error]
    """

    kwargs = _get_kwargs(
        dashboard_id=dashboard_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dashboard_id: UUID,
    *,
    client: AuthenticatedClient,
) -> DashboardDetailSchema | Error | None:
    """Detail

     Get full details of a dashboard with its sections, charts, and queries.

    Requires dashboard:read scope.

    Args:
        dashboard_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DashboardDetailSchema | Error
    """

    return sync_detailed(
        dashboard_id=dashboard_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    dashboard_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[DashboardDetailSchema | Error]:
    """Detail

     Get full details of a dashboard with its sections, charts, and queries.

    Requires dashboard:read scope.

    Args:
        dashboard_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DashboardDetailSchema | Error]
    """

    kwargs = _get_kwargs(
        dashboard_id=dashboard_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dashboard_id: UUID,
    *,
    client: AuthenticatedClient,
) -> DashboardDetailSchema | Error | None:
    """Detail

     Get full details of a dashboard with its sections, charts, and queries.

    Requires dashboard:read scope.

    Args:
        dashboard_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DashboardDetailSchema | Error
    """

    return (
        await asyncio_detailed(
            dashboard_id=dashboard_id,
            client=client,
        )
    ).parsed
