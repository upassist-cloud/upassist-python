from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.error_issue_detail_schema import ErrorIssueDetailSchema
from ...models.error_issue_update_schema import ErrorIssueUpdateSchema
from ...types import Response


def _get_kwargs(
    error_app_id: UUID,
    issue_id: UUID,
    *,
    body: ErrorIssueUpdateSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/error-apps/{error_app_id}/issues/{issue_id}".format(
            error_app_id=quote(str(error_app_id), safe=""),
            issue_id=quote(str(issue_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | ErrorIssueDetailSchema | None:
    if response.status_code == 200:
        response_200 = ErrorIssueDetailSchema.from_dict(response.json())

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
) -> Response[Error | ErrorIssueDetailSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    error_app_id: UUID,
    issue_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ErrorIssueUpdateSchema,
) -> Response[Error | ErrorIssueDetailSchema]:
    """Update

    Args:
        error_app_id (UUID):
        issue_id (UUID):
        body (ErrorIssueUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ErrorIssueDetailSchema]
    """

    kwargs = _get_kwargs(
        error_app_id=error_app_id,
        issue_id=issue_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    error_app_id: UUID,
    issue_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ErrorIssueUpdateSchema,
) -> Error | ErrorIssueDetailSchema | None:
    """Update

    Args:
        error_app_id (UUID):
        issue_id (UUID):
        body (ErrorIssueUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ErrorIssueDetailSchema
    """

    return sync_detailed(
        error_app_id=error_app_id,
        issue_id=issue_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    error_app_id: UUID,
    issue_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ErrorIssueUpdateSchema,
) -> Response[Error | ErrorIssueDetailSchema]:
    """Update

    Args:
        error_app_id (UUID):
        issue_id (UUID):
        body (ErrorIssueUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ErrorIssueDetailSchema]
    """

    kwargs = _get_kwargs(
        error_app_id=error_app_id,
        issue_id=issue_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    error_app_id: UUID,
    issue_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ErrorIssueUpdateSchema,
) -> Error | ErrorIssueDetailSchema | None:
    """Update

    Args:
        error_app_id (UUID):
        issue_id (UUID):
        body (ErrorIssueUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ErrorIssueDetailSchema
    """

    return (
        await asyncio_detailed(
            error_app_id=error_app_id,
            issue_id=issue_id,
            client=client,
            body=body,
        )
    ).parsed
