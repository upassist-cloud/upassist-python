from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.maintenance_detail_schema import MaintenanceDetailSchema
from ...types import Response


def _get_kwargs(
    maintenance_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/maintenance/{maintenance_id}".format(
            maintenance_id=quote(str(maintenance_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | MaintenanceDetailSchema | None:
    if response.status_code == 200:
        response_200 = MaintenanceDetailSchema.from_dict(response.json())

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
) -> Response[Error | MaintenanceDetailSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    maintenance_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Error | MaintenanceDetailSchema]:
    """Detail

    Args:
        maintenance_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MaintenanceDetailSchema]
    """

    kwargs = _get_kwargs(
        maintenance_id=maintenance_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    maintenance_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Error | MaintenanceDetailSchema | None:
    """Detail

    Args:
        maintenance_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MaintenanceDetailSchema
    """

    return sync_detailed(
        maintenance_id=maintenance_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    maintenance_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Error | MaintenanceDetailSchema]:
    """Detail

    Args:
        maintenance_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MaintenanceDetailSchema]
    """

    kwargs = _get_kwargs(
        maintenance_id=maintenance_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    maintenance_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Error | MaintenanceDetailSchema | None:
    """Detail

    Args:
        maintenance_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MaintenanceDetailSchema
    """

    return (
        await asyncio_detailed(
            maintenance_id=maintenance_id,
            client=client,
        )
    ).parsed
