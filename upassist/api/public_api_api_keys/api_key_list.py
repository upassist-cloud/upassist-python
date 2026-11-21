from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_key_paginated_schema import APIKeyPaginatedSchema
from ...models.api_key_scope_enum import APIKeyScopeEnum
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    q: None | str | Unset = UNSET,
    scopes: list[APIKeyScopeEnum] | None | Unset = UNSET,
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

    json_scopes: list[str] | None | Unset
    if isinstance(scopes, Unset):
        json_scopes = UNSET
    elif isinstance(scopes, list):
        json_scopes = []
        for scopes_type_0_item_data in scopes:
            scopes_type_0_item = scopes_type_0_item_data.value
            json_scopes.append(scopes_type_0_item)

    else:
        json_scopes = scopes
    params["scopes"] = json_scopes

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/api-keys",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIKeyPaginatedSchema | Error | None:
    if response.status_code == 200:
        response_200 = APIKeyPaginatedSchema.from_dict(response.json())

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
) -> Response[APIKeyPaginatedSchema | Error]:
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
    scopes: list[APIKeyScopeEnum] | None | Unset = UNSET,
) -> Response[APIKeyPaginatedSchema | Error]:
    """ListApiKeys

     List active API keys in the project with scopes and creation dates.

    Requires api-key:read scope.

    Args:
        page (int | Unset): Data page number Default: 1.
        per_page (int | Unset): Amount of results per page Default: 20.
        q (None | str | Unset):
        scopes (list[APIKeyScopeEnum] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIKeyPaginatedSchema | Error]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        q=q,
        scopes=scopes,
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
    scopes: list[APIKeyScopeEnum] | None | Unset = UNSET,
) -> APIKeyPaginatedSchema | Error | None:
    """ListApiKeys

     List active API keys in the project with scopes and creation dates.

    Requires api-key:read scope.

    Args:
        page (int | Unset): Data page number Default: 1.
        per_page (int | Unset): Amount of results per page Default: 20.
        q (None | str | Unset):
        scopes (list[APIKeyScopeEnum] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIKeyPaginatedSchema | Error
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        q=q,
        scopes=scopes,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    q: None | str | Unset = UNSET,
    scopes: list[APIKeyScopeEnum] | None | Unset = UNSET,
) -> Response[APIKeyPaginatedSchema | Error]:
    """ListApiKeys

     List active API keys in the project with scopes and creation dates.

    Requires api-key:read scope.

    Args:
        page (int | Unset): Data page number Default: 1.
        per_page (int | Unset): Amount of results per page Default: 20.
        q (None | str | Unset):
        scopes (list[APIKeyScopeEnum] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIKeyPaginatedSchema | Error]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        q=q,
        scopes=scopes,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    q: None | str | Unset = UNSET,
    scopes: list[APIKeyScopeEnum] | None | Unset = UNSET,
) -> APIKeyPaginatedSchema | Error | None:
    """ListApiKeys

     List active API keys in the project with scopes and creation dates.

    Requires api-key:read scope.

    Args:
        page (int | Unset): Data page number Default: 1.
        per_page (int | Unset): Amount of results per page Default: 20.
        q (None | str | Unset):
        scopes (list[APIKeyScopeEnum] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIKeyPaginatedSchema | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            q=q,
            scopes=scopes,
        )
    ).parsed
