from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.sdk_setup_schema import SdkSetupSchema
from ...types import Response


def _get_kwargs(
    error_app_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/error-apps/{error_app_id}/sdk-setup".format(
            error_app_id=quote(str(error_app_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | SdkSetupSchema | None:
    if response.status_code == 200:
        response_200 = SdkSetupSchema.from_dict(response.json())

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
) -> Response[Error | SdkSetupSchema]:
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
) -> Response[Error | SdkSetupSchema]:
    """SdkSetup

    Args:
        error_app_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SdkSetupSchema]
    """

    kwargs = _get_kwargs(
        error_app_id=error_app_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    error_app_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Error | SdkSetupSchema | None:
    """SdkSetup

    Args:
        error_app_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SdkSetupSchema
    """

    return sync_detailed(
        error_app_id=error_app_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    error_app_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Error | SdkSetupSchema]:
    """SdkSetup

    Args:
        error_app_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SdkSetupSchema]
    """

    kwargs = _get_kwargs(
        error_app_id=error_app_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    error_app_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Error | SdkSetupSchema | None:
    """SdkSetup

    Args:
        error_app_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SdkSetupSchema
    """

    return (
        await asyncio_detailed(
            error_app_id=error_app_id,
            client=client,
        )
    ).parsed
