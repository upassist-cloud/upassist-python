from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.policy_detail_schema import PolicyDetailSchema
from ...models.policy_update_schema import PolicyUpdateSchema
from ...types import Response


def _get_kwargs(
    policy_id: UUID,
    *,
    body: PolicyUpdateSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/escalation-policies/{policy_id}".format(
            policy_id=quote(str(policy_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | PolicyDetailSchema | None:
    if response.status_code == 200:
        response_200 = PolicyDetailSchema.from_dict(response.json())

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
) -> Response[Error | PolicyDetailSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    policy_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PolicyUpdateSchema,
) -> Response[Error | PolicyDetailSchema]:
    """Update

    Args:
        policy_id (UUID):
        body (PolicyUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PolicyDetailSchema]
    """

    kwargs = _get_kwargs(
        policy_id=policy_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    policy_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PolicyUpdateSchema,
) -> Error | PolicyDetailSchema | None:
    """Update

    Args:
        policy_id (UUID):
        body (PolicyUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PolicyDetailSchema
    """

    return sync_detailed(
        policy_id=policy_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    policy_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PolicyUpdateSchema,
) -> Response[Error | PolicyDetailSchema]:
    """Update

    Args:
        policy_id (UUID):
        body (PolicyUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PolicyDetailSchema]
    """

    kwargs = _get_kwargs(
        policy_id=policy_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    policy_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PolicyUpdateSchema,
) -> Error | PolicyDetailSchema | None:
    """Update

    Args:
        policy_id (UUID):
        body (PolicyUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PolicyDetailSchema
    """

    return (
        await asyncio_detailed(
            policy_id=policy_id,
            client=client,
            body=body,
        )
    ).parsed
