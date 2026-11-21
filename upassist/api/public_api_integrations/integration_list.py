from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.integration_schema import IntegrationSchema
from ...models.integration_source_enum import IntegrationSourceEnum
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    source: IntegrationSourceEnum | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_source: None | str | Unset
    if isinstance(source, Unset):
        json_source = UNSET
    elif isinstance(source, IntegrationSourceEnum):
        json_source = source.value
    else:
        json_source = source
    params["source"] = json_source

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/integrations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | list[IntegrationSchema] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = IntegrationSchema.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Error | list[IntegrationSchema]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    source: IntegrationSourceEnum | None | Unset = UNSET,
) -> Response[Error | list[IntegrationSchema]]:
    """ListIntegrations

    Args:
        source (IntegrationSourceEnum | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[IntegrationSchema]]
    """

    kwargs = _get_kwargs(
        source=source,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    source: IntegrationSourceEnum | None | Unset = UNSET,
) -> Error | list[IntegrationSchema] | None:
    """ListIntegrations

    Args:
        source (IntegrationSourceEnum | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[IntegrationSchema]
    """

    return sync_detailed(
        client=client,
        source=source,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    source: IntegrationSourceEnum | None | Unset = UNSET,
) -> Response[Error | list[IntegrationSchema]]:
    """ListIntegrations

    Args:
        source (IntegrationSourceEnum | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[IntegrationSchema]]
    """

    kwargs = _get_kwargs(
        source=source,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    source: IntegrationSourceEnum | None | Unset = UNSET,
) -> Error | list[IntegrationSchema] | None:
    """ListIntegrations

    Args:
        source (IntegrationSourceEnum | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[IntegrationSchema]
    """

    return (
        await asyncio_detailed(
            client=client,
            source=source,
        )
    ).parsed
