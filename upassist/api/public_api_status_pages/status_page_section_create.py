from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.status_page_section_create_schema import StatusPageSectionCreateSchema
from ...models.status_page_section_schema import StatusPageSectionSchema
from ...types import Response


def _get_kwargs(
    status_page_id: UUID,
    *,
    body: StatusPageSectionCreateSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/status-pages/{status_page_id}/sections".format(
            status_page_id=quote(str(status_page_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | StatusPageSectionSchema | None:
    if response.status_code == 201:
        response_201 = StatusPageSectionSchema.from_dict(response.json())

        return response_201

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
) -> Response[Error | StatusPageSectionSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    status_page_id: UUID,
    *,
    client: AuthenticatedClient,
    body: StatusPageSectionCreateSchema,
) -> Response[Error | StatusPageSectionSchema]:
    """Create

     Create a new section on a status page.

    Args:
        status_page_id (UUID):
        body (StatusPageSectionCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | StatusPageSectionSchema]
    """

    kwargs = _get_kwargs(
        status_page_id=status_page_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    status_page_id: UUID,
    *,
    client: AuthenticatedClient,
    body: StatusPageSectionCreateSchema,
) -> Error | StatusPageSectionSchema | None:
    """Create

     Create a new section on a status page.

    Args:
        status_page_id (UUID):
        body (StatusPageSectionCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | StatusPageSectionSchema
    """

    return sync_detailed(
        status_page_id=status_page_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    status_page_id: UUID,
    *,
    client: AuthenticatedClient,
    body: StatusPageSectionCreateSchema,
) -> Response[Error | StatusPageSectionSchema]:
    """Create

     Create a new section on a status page.

    Args:
        status_page_id (UUID):
        body (StatusPageSectionCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | StatusPageSectionSchema]
    """

    kwargs = _get_kwargs(
        status_page_id=status_page_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    status_page_id: UUID,
    *,
    client: AuthenticatedClient,
    body: StatusPageSectionCreateSchema,
) -> Error | StatusPageSectionSchema | None:
    """Create

     Create a new section on a status page.

    Args:
        status_page_id (UUID):
        body (StatusPageSectionCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | StatusPageSectionSchema
    """

    return (
        await asyncio_detailed(
            status_page_id=status_page_id,
            client=client,
            body=body,
        )
    ).parsed
