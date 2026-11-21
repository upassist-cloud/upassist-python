from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...types import UNSET, Response


def _get_kwargs(
    status_page_id: UUID,
    report_id: UUID,
    *,
    status_page_report_service: Any,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["status_page_report_service"] = status_page_report_service

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/status-pages/{status_page_id}/reports/{report_id}".format(
            status_page_id=quote(str(status_page_id), safe=""),
            report_id=quote(str(report_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    status_page_id: UUID,
    report_id: UUID,
    *,
    client: AuthenticatedClient,
    status_page_report_service: Any,
) -> Response[Any | Error]:
    """DeleteDetail

     Delete a status report.

    Args:
        status_page_id (UUID):
        report_id (UUID):
        status_page_report_service (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        status_page_id=status_page_id,
        report_id=report_id,
        status_page_report_service=status_page_report_service,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    status_page_id: UUID,
    report_id: UUID,
    *,
    client: AuthenticatedClient,
    status_page_report_service: Any,
) -> Any | Error | None:
    """DeleteDetail

     Delete a status report.

    Args:
        status_page_id (UUID):
        report_id (UUID):
        status_page_report_service (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return sync_detailed(
        status_page_id=status_page_id,
        report_id=report_id,
        client=client,
        status_page_report_service=status_page_report_service,
    ).parsed


async def asyncio_detailed(
    status_page_id: UUID,
    report_id: UUID,
    *,
    client: AuthenticatedClient,
    status_page_report_service: Any,
) -> Response[Any | Error]:
    """DeleteDetail

     Delete a status report.

    Args:
        status_page_id (UUID):
        report_id (UUID):
        status_page_report_service (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        status_page_id=status_page_id,
        report_id=report_id,
        status_page_report_service=status_page_report_service,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    status_page_id: UUID,
    report_id: UUID,
    *,
    client: AuthenticatedClient,
    status_page_report_service: Any,
) -> Any | Error | None:
    """DeleteDetail

     Delete a status report.

    Args:
        status_page_id (UUID):
        report_id (UUID):
        status_page_report_service (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return (
        await asyncio_detailed(
            status_page_id=status_page_id,
            report_id=report_id,
            client=client,
            status_page_report_service=status_page_report_service,
        )
    ).parsed
