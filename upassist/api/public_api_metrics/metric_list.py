from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.metric_info_schema import MetricInfoSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    source_id: UUID,
    *,
    q: None | str | Unset = UNSET,
    limit: int | Unset = 200,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_q: None | str | Unset
    if isinstance(q, Unset):
        json_q = UNSET
    else:
        json_q = q
    params["q"] = json_q

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/sources/{source_id}/metrics".format(
            source_id=quote(str(source_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | list[MetricInfoSchema] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = MetricInfoSchema.from_dict(response_200_item_data)

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
) -> Response[Error | list[MetricInfoSchema]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    source_id: UUID,
    *,
    client: AuthenticatedClient,
    q: None | str | Unset = UNSET,
    limit: int | Unset = 200,
) -> Response[Error | list[MetricInfoSchema]]:
    """ListMetrics

    Args:
        source_id (UUID):
        q (None | str | Unset):
        limit (int | Unset):  Default: 200.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[MetricInfoSchema]]
    """

    kwargs = _get_kwargs(
        source_id=source_id,
        q=q,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    source_id: UUID,
    *,
    client: AuthenticatedClient,
    q: None | str | Unset = UNSET,
    limit: int | Unset = 200,
) -> Error | list[MetricInfoSchema] | None:
    """ListMetrics

    Args:
        source_id (UUID):
        q (None | str | Unset):
        limit (int | Unset):  Default: 200.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[MetricInfoSchema]
    """

    return sync_detailed(
        source_id=source_id,
        client=client,
        q=q,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    source_id: UUID,
    *,
    client: AuthenticatedClient,
    q: None | str | Unset = UNSET,
    limit: int | Unset = 200,
) -> Response[Error | list[MetricInfoSchema]]:
    """ListMetrics

    Args:
        source_id (UUID):
        q (None | str | Unset):
        limit (int | Unset):  Default: 200.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[MetricInfoSchema]]
    """

    kwargs = _get_kwargs(
        source_id=source_id,
        q=q,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    source_id: UUID,
    *,
    client: AuthenticatedClient,
    q: None | str | Unset = UNSET,
    limit: int | Unset = 200,
) -> Error | list[MetricInfoSchema] | None:
    """ListMetrics

    Args:
        source_id (UUID):
        q (None | str | Unset):
        limit (int | Unset):  Default: 200.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[MetricInfoSchema]
    """

    return (
        await asyncio_detailed(
            source_id=source_id,
            client=client,
            q=q,
            limit=limit,
        )
    ).parsed
