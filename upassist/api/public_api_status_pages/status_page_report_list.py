from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.status_page_report_schema import StatusPageReportSchema
from ...types import Response


def _get_kwargs(
    status_page_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/status-pages/{status_page_id}/reports".format(
            status_page_id=quote(str(status_page_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | list[StatusPageReportSchema] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = StatusPageReportSchema.from_dict(response_200_item_data)

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
) -> Response[Error | list[StatusPageReportSchema]]:
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
) -> Response[Error | list[StatusPageReportSchema]]:
    """ListReports

     List active and historical status reports for a status page.

    Args:
        status_page_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[StatusPageReportSchema]]
    """

    kwargs = _get_kwargs(
        status_page_id=status_page_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    status_page_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Error | list[StatusPageReportSchema] | None:
    """ListReports

     List active and historical status reports for a status page.

    Args:
        status_page_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[StatusPageReportSchema]
    """

    return sync_detailed(
        status_page_id=status_page_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    status_page_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Error | list[StatusPageReportSchema]]:
    """ListReports

     List active and historical status reports for a status page.

    Args:
        status_page_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[StatusPageReportSchema]]
    """

    kwargs = _get_kwargs(
        status_page_id=status_page_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    status_page_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Error | list[StatusPageReportSchema] | None:
    """ListReports

     List active and historical status reports for a status page.

    Args:
        status_page_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[StatusPageReportSchema]
    """

    return (
        await asyncio_detailed(
            status_page_id=status_page_id,
            client=client,
        )
    ).parsed
