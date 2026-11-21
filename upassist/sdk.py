"""Official Python SDK for the Upassist Monitoring & Observability Platform.

Management API calls require a Project API Key sent as Bearer token to https://api.upassist.cloud.
High-throughput ingestion calls (heartbeat pings, log streams, metric points) are handled via
dedicated low-latency ingestion hosts.

Provides:
- Upassist: Synchronous client with ergonomic typed resource facades.
- AsyncUpassist: True asynchronous client (asyncio) with identical facade structure.
- APIError, IngestError: Structured error types.
"""

from __future__ import annotations

import importlib
import inspect
import os
import pkgutil
from typing import Any, AsyncIterator, Iterator, Mapping, Self
from uuid import UUID

import httpx

from . import api as api_package
from .client import AuthenticatedClient, Client as LowLevelClient
from .models.error import Error
from .types import UNSET, Unset

MANAGEMENT_URL = "https://api.upassist.cloud"
HEARTBEATS_URL = "https://heartbeats.upassist.cloud"
LOGS_URL = "https://logs.upassist.cloud"
METRICS_URL = "https://metrics.upassist.cloud"
RUM_URL = "https://rum.upassist.cloud"


class APIError(Exception):
    """Raised when the management API returns an error response."""

    def __init__(self, code: str, message: str, request_id: str | None = None, status_code: int = 400):
        super().__init__(f"[{code}] {message}" if code else message)
        self.code = code
        self.message = message
        self.request_id = request_id
        self.status_code = status_code

    def __repr__(self) -> str:
        return f"APIError(code={self.code!r}, message={self.message!r}, request_id={self.request_id!r})"


class IngestError(Exception):
    """Raised when an ingestion host returns a non-2xx status code."""

    def __init__(self, status_code: int, body: str):
        super().__init__(f"Ingest error {status_code}: {body}")
        self.status_code = status_code
        self.body = body


class _OpMetadata:
    """Pre-indexed metadata for an OpenAPI operation."""

    __slots__ = ("name", "sync_fn", "async_fn", "body_param", "body_cls")

    def __init__(self, name: str, sync_fn: Any, async_fn: Any):
        self.name = name
        self.sync_fn = sync_fn
        self.async_fn = async_fn
        self.body_param: str | None = None
        self.body_cls: Any | None = None

        if sync_fn is not None:
            try:
                sig = inspect.signature(sync_fn)
                for p_name, param in sig.parameters.items():
                    if p_name == "body":
                        self.body_param = p_name
                        self.body_cls = param.annotation
                        break
            except Exception:
                pass


def _index_operations() -> dict[str, _OpMetadata]:
    """Index operations once at module load to avoid runtime filesystem scanning."""
    operations: dict[str, _OpMetadata] = {}
    for module_info in pkgutil.walk_packages(api_package.__path__, api_package.__name__ + "."):
        if module_info.ispkg:
            continue
        try:
            module = importlib.import_module(module_info.name)
            sync_fn = getattr(module, "sync", None)
            async_fn = getattr(module, "asyncio", None)
            if sync_fn is not None or async_fn is not None:
                op_name = module_info.name.rsplit(".", 1)[-1]
                operations[op_name] = _OpMetadata(op_name, sync_fn, async_fn)
        except Exception:
            continue
    return operations


_OPERATIONS = _index_operations()


def _prepare_call_kwargs(op: _OpMetadata, kwargs: dict[str, Any]) -> dict[str, Any]:
    """Prepare keyword arguments, adapting dicts to schema models if required."""
    call_kwargs = dict(kwargs)
    if op.body_cls and op.body_param:
        body_val = call_kwargs.get(op.body_param)
        if body_val is None and len(call_kwargs) > 0:
            # Caller passed payload fields as kwargs
            body_dict = {k: v for k, v in call_kwargs.items() if k not in ("client",)}
            if hasattr(op.body_cls, "from_dict"):
                try:
                    call_kwargs = {op.body_param: op.body_cls.from_dict(body_dict)}
                except Exception:
                    pass
        elif isinstance(body_val, dict) and hasattr(op.body_cls, "from_dict"):
            try:
                call_kwargs[op.body_param] = op.body_cls.from_dict(body_val)
            except Exception:
                pass
    return call_kwargs


def _unwrap_result(parsed: Any) -> Any:
    """Unwrap parsed OpenAPI model, raising APIError if an error was returned."""
    if isinstance(parsed, Error):
        req_id = None if isinstance(parsed.request_id, Unset) else parsed.request_id
        code = str(getattr(parsed, "code", "api_error"))
        message = str(getattr(parsed, "message", "Unknown error"))
        raise APIError(code, message, req_id)
    return parsed


# ---------------------------------------------------------------------------
# Base Resource Classes
# ---------------------------------------------------------------------------


class SyncResource:
    """Base for synchronous resource facades."""

    prefix: str = ""

    def __init__(self, client: "Upassist"):
        self._client = client

    def _call(self, op_name: str, *args: Any, **kwargs: Any) -> Any:
        full_name = f"{self.prefix}_{op_name}" if self.prefix else op_name
        op = _OPERATIONS.get(full_name)
        if op is None or op.sync_fn is None:
            raise AttributeError(f"Operation {full_name!r} not supported")
        call_kwargs = _prepare_call_kwargs(op, kwargs)
        parsed = op.sync_fn(*args, client=self._client._http, **call_kwargs)
        return _unwrap_result(parsed)

    def _paginate(self, op_name: str, **kwargs: Any) -> Iterator[Any]:
        page = kwargs.pop("page", 1)
        per_page = kwargs.pop("per_page", 50)
        while True:
            response = self._call(op_name, page=page, per_page=per_page, **kwargs)
            items = getattr(response, "items", None) or getattr(response, "data", None) or []
            for item in items:
                yield item
            total = getattr(response, "total", None) or getattr(response, "total_count", None) or getattr(response, "count", None)
            if total is None or page * per_page >= total or len(items) == 0:
                break
            page += 1


class AsyncResource:
    """Base for asynchronous resource facades."""

    prefix: str = ""

    def __init__(self, client: "AsyncUpassist"):
        self._client = client

    async def _call(self, op_name: str, *args: Any, **kwargs: Any) -> Any:
        full_name = f"{self.prefix}_{op_name}" if self.prefix else op_name
        op = _OPERATIONS.get(full_name)
        if op is None or op.async_fn is None:
            raise AttributeError(f"Async operation {full_name!r} not supported")
        call_kwargs = _prepare_call_kwargs(op, kwargs)
        parsed = await op.async_fn(*args, client=self._client._http, **call_kwargs)
        return _unwrap_result(parsed)

    async def _paginate(self, op_name: str, **kwargs: Any) -> AsyncIterator[Any]:
        page = kwargs.pop("page", 1)
        per_page = kwargs.pop("per_page", 50)
        while True:
            response = await self._call(op_name, page=page, per_page=per_page, **kwargs)
            items = getattr(response, "items", None) or getattr(response, "data", None) or []
            for item in items:
                yield item
            total = getattr(response, "total", None) or getattr(response, "total_count", None) or getattr(response, "count", None)
            if total is None or page * per_page >= total or len(items) == 0:
                break
            page += 1


# ---------------------------------------------------------------------------
# Monitors Resource (Sync & Async)
# ---------------------------------------------------------------------------


class MonitorsResource(SyncResource):
    prefix = "monitor"

    def list(self, **kwargs: Any) -> Any:
        return self._call("list", **kwargs)

    def iter(self, **kwargs: Any) -> Iterator[Any]:
        return self._paginate("list", **kwargs)

    def get(self, monitor_id: str | UUID) -> Any:
        return self._call("get", monitor_id=monitor_id)

    def create(self, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return self._call("create", body=payload)

    def update(self, monitor_id: str | UUID, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return self._call("update", monitor_id=monitor_id, body=payload)

    def delete(self, monitor_id: str | UUID) -> None:
        self._call("delete", monitor_id=monitor_id)

    def pause(self, monitor_id: str | UUID) -> Any:
        return self._call("pause", monitor_id=monitor_id)

    def unpause(self, monitor_id: str | UUID) -> Any:
        return self._call("unpause", monitor_id=monitor_id)

    def turn_on_alerts(self, monitor_id: str | UUID) -> Any:
        return self._call("turn_on_alerts", monitor_id=monitor_id)

    def turn_off_alerts(self, monitor_id: str | UUID) -> Any:
        return self._call("turn_off_alerts", monitor_id=monitor_id)

    def test_alert(self, monitor_id: str | UUID) -> Any:
        return self._call("test_alert", monitor_id=monitor_id)


class AsyncMonitorsResource(AsyncResource):
    prefix = "monitor"

    async def list(self, **kwargs: Any) -> Any:
        return await self._call("list", **kwargs)

    async def iter(self, **kwargs: Any) -> AsyncIterator[Any]:
        async for item in self._paginate("list", **kwargs):
            yield item

    async def get(self, monitor_id: str | UUID) -> Any:
        return await self._call("get", monitor_id=monitor_id)

    async def create(self, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return await self._call("create", body=payload)

    async def update(self, monitor_id: str | UUID, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return await self._call("update", monitor_id=monitor_id, body=payload)

    async def delete(self, monitor_id: str | UUID) -> None:
        await self._call("delete", monitor_id=monitor_id)

    async def pause(self, monitor_id: str | UUID) -> Any:
        return await self._call("pause", monitor_id=monitor_id)

    async def unpause(self, monitor_id: str | UUID) -> Any:
        return await self._call("unpause", monitor_id=monitor_id)

    async def turn_on_alerts(self, monitor_id: str | UUID) -> Any:
        return await self._call("turn_on_alerts", monitor_id=monitor_id)

    async def turn_off_alerts(self, monitor_id: str | UUID) -> Any:
        return await self._call("turn_off_alerts", monitor_id=monitor_id)

    async def test_alert(self, monitor_id: str | UUID) -> Any:
        return await self._call("test_alert", monitor_id=monitor_id)


# ---------------------------------------------------------------------------
# Heartbeats Resource (Sync & Async)
# ---------------------------------------------------------------------------


class HeartbeatsResource(SyncResource):
    prefix = "heartbeat"

    def list(self, **kwargs: Any) -> Any:
        return self._call("list", **kwargs)

    def iter(self, **kwargs: Any) -> Iterator[Any]:
        return self._paginate("list", **kwargs)

    def get(self, heartbeat_slug: str) -> Any:
        return self._call("get", heartbeat_slug=heartbeat_slug)

    def create(self, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return self._call("create", body=payload)

    def update(self, heartbeat_slug: str, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return self._call("update", heartbeat_slug=heartbeat_slug, body=payload)

    def delete(self, heartbeat_slug: str) -> None:
        self._call("delete", heartbeat_slug=heartbeat_slug)

    def pause(self, heartbeat_slug: str) -> Any:
        return self._call("pause", heartbeat_slug=heartbeat_slug)

    def unpause(self, heartbeat_slug: str) -> Any:
        return self._call("unpause", heartbeat_slug=heartbeat_slug)

    def turn_on_alerts(self, heartbeat_slug: str) -> Any:
        return self._call("turn_on_alerts", heartbeat_slug=heartbeat_slug)

    def turn_off_alerts(self, heartbeat_slug: str) -> Any:
        return self._call("turn_off_alerts", heartbeat_slug=heartbeat_slug)

    def ping(
        self,
        token: str,
        *,
        status: str = "up",
        duration_ms: int | None = None,
        message: str | None = None,
    ) -> str:
        """Send zero-latency heartbeat ping to high-throughput ingest host."""
        params: dict[str, Any] = {}
        if status == "down":
            params["error"] = "true"
        if duration_ms is not None:
            params["duration"] = str(duration_ms)
        if message is not None:
            params["errorMessage"] = message

        url = f"{HEARTBEATS_URL}/api/event/{token}"
        resp = httpx.get(
            url,
            params=params,
            headers={"Authorization": f"Bearer {self._client.api_key}"},
            timeout=10,
        )
        if resp.status_code >= 400:
            raise IngestError(resp.status_code, resp.text)
        return resp.text


class AsyncHeartbeatsResource(AsyncResource):
    prefix = "heartbeat"

    async def list(self, **kwargs: Any) -> Any:
        return await self._call("list", **kwargs)

    async def iter(self, **kwargs: Any) -> AsyncIterator[Any]:
        async for item in self._paginate("list", **kwargs):
            yield item

    async def get(self, heartbeat_slug: str) -> Any:
        return await self._call("get", heartbeat_slug=heartbeat_slug)

    async def create(self, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return await self._call("create", body=payload)

    async def update(self, heartbeat_slug: str, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return await self._call("update", heartbeat_slug=heartbeat_slug, body=payload)

    async def delete(self, heartbeat_slug: str) -> None:
        await self._call("delete", heartbeat_slug=heartbeat_slug)

    async def pause(self, heartbeat_slug: str) -> Any:
        return await self._call("pause", heartbeat_slug=heartbeat_slug)

    async def unpause(self, heartbeat_slug: str) -> Any:
        return await self._call("unpause", heartbeat_slug=heartbeat_slug)

    async def turn_on_alerts(self, heartbeat_slug: str) -> Any:
        return await self._call("turn_on_alerts", heartbeat_slug=heartbeat_slug)

    async def turn_off_alerts(self, heartbeat_slug: str) -> Any:
        return await self._call("turn_off_alerts", heartbeat_slug=heartbeat_slug)

    async def ping(
        self,
        token: str,
        *,
        status: str = "up",
        duration_ms: int | None = None,
        message: str | None = None,
    ) -> str:
        """Asynchronously send zero-latency heartbeat ping to ingest host."""
        params: dict[str, Any] = {}
        if status == "down":
            params["error"] = "true"
        if duration_ms is not None:
            params["duration"] = str(duration_ms)
        if message is not None:
            params["errorMessage"] = message

        url = f"{HEARTBEATS_URL}/api/event/{token}"
        client = await self._client._http.get_async_httpx_client()
        resp = await client.get(url, params=params, headers={"Authorization": f"Bearer {self._client.api_key}"})
        if resp.status_code >= 400:
            raise IngestError(resp.status_code, resp.text)
        return resp.text


# ---------------------------------------------------------------------------
# Incidents Resource (Sync & Async)
# ---------------------------------------------------------------------------


class IncidentsResource(SyncResource):
    prefix = "incident"

    def list(self, **kwargs: Any) -> Any:
        return self._call("list", **kwargs)

    def iter(self, **kwargs: Any) -> Iterator[Any]:
        return self._paginate("list", **kwargs)

    def get(self, incident_id: str | UUID) -> Any:
        return self._call("get", incident_id=incident_id)

    def acknowledge(self, incident_id: str | UUID) -> Any:
        return self._call("acknowledge", incident_id=incident_id)

    def ack(self, incident_id: str | UUID) -> Any:
        """Convenience alias for acknowledge."""
        return self.acknowledge(incident_id)

    def resolve(self, incident_id: str | UUID) -> Any:
        return self._call("resolve", incident_id=incident_id)

    def delete(self, incident_id: str | UUID) -> None:
        self._call("delete", incident_id=incident_id)


class AsyncIncidentsResource(AsyncResource):
    prefix = "incident"

    async def list(self, **kwargs: Any) -> Any:
        return await self._call("list", **kwargs)

    async def iter(self, **kwargs: Any) -> AsyncIterator[Any]:
        async for item in self._paginate("list", **kwargs):
            yield item

    async def get(self, incident_id: str | UUID) -> Any:
        return await self._call("get", incident_id=incident_id)

    async def acknowledge(self, incident_id: str | UUID) -> Any:
        return await self._call("acknowledge", incident_id=incident_id)

    async def ack(self, incident_id: str | UUID) -> Any:
        return await self.acknowledge(incident_id)

    async def resolve(self, incident_id: str | UUID) -> Any:
        return await self._call("resolve", incident_id=incident_id)

    async def delete(self, incident_id: str | UUID) -> None:
        await self._call("delete", incident_id=incident_id)


# ---------------------------------------------------------------------------
# Maintenance Resource (Sync & Async)
# ---------------------------------------------------------------------------


class MaintenanceResource(SyncResource):
    prefix = "maintenance"

    def list(self, **kwargs: Any) -> Any:
        return self._call("list", **kwargs)

    def iter(self, **kwargs: Any) -> Iterator[Any]:
        return self._paginate("list", **kwargs)

    def get(self, maintenance_id: str | UUID) -> Any:
        return self._call("get", maintenance_id=maintenance_id)

    def create(self, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return self._call("create", body=payload)

    def update(self, maintenance_id: str | UUID, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return self._call("update", maintenance_id=maintenance_id, body=payload)

    def delete(self, maintenance_id: str | UUID) -> None:
        self._call("delete", maintenance_id=maintenance_id)


class AsyncMaintenanceResource(AsyncResource):
    prefix = "maintenance"

    async def list(self, **kwargs: Any) -> Any:
        return await self._call("list", **kwargs)

    async def iter(self, **kwargs: Any) -> AsyncIterator[Any]:
        async for item in self._paginate("list", **kwargs):
            yield item

    async def get(self, maintenance_id: str | UUID) -> Any:
        return await self._call("get", maintenance_id=maintenance_id)

    async def create(self, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return await self._call("create", body=payload)

    async def update(self, maintenance_id: str | UUID, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return await self._call("update", maintenance_id=maintenance_id, body=payload)

    async def delete(self, maintenance_id: str | UUID) -> None:
        await self._call("delete", maintenance_id=maintenance_id)


# ---------------------------------------------------------------------------
# Error Apps Resource (Sync & Async)
# ---------------------------------------------------------------------------


class ErrorAppIssuesResource(SyncResource):
    prefix = "error_app"

    def list(self, app_id: str | UUID, **kwargs: Any) -> Any:
        return self._call("issue_list", app_id=app_id, **kwargs)

    def get(self, app_id: str | UUID, issue_id: str | UUID) -> Any:
        return self._call("issue_get", app_id=app_id, issue_id=issue_id)

    def update(self, app_id: str | UUID, issue_id: str | UUID, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return self._call("issue_update", app_id=app_id, issue_id=issue_id, body=payload)

    def resolve(self, app_id: str | UUID, issue_id: str | UUID) -> Any:
        return self.update(app_id, issue_id, status="resolved")

    def delete(self, app_id: str | UUID, issue_id: str | UUID) -> None:
        self._call("issue_delete", app_id=app_id, issue_id=issue_id)


class AsyncErrorAppIssuesResource(AsyncResource):
    prefix = "error_app"

    async def list(self, app_id: str | UUID, **kwargs: Any) -> Any:
        return await self._call("issue_list", app_id=app_id, **kwargs)

    async def get(self, app_id: str | UUID, issue_id: str | UUID) -> Any:
        return await self._call("issue_get", app_id=app_id, issue_id=issue_id)

    async def update(self, app_id: str | UUID, issue_id: str | UUID, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return await self._call("issue_update", app_id=app_id, issue_id=issue_id, body=payload)

    async def resolve(self, app_id: str | UUID, issue_id: str | UUID) -> Any:
        return await self.update(app_id, issue_id, status="resolved")

    async def delete(self, app_id: str | UUID, issue_id: str | UUID) -> None:
        await self._call("issue_delete", app_id=app_id, issue_id=issue_id)


class ErrorAppsResource(SyncResource):
    prefix = "error_app"

    def __init__(self, client: "Upassist"):
        super().__init__(client)
        self.issues = ErrorAppIssuesResource(client)

    def list(self, **kwargs: Any) -> Any:
        return self._call("list", **kwargs)

    def get(self, app_id: str | UUID) -> Any:
        return self._call("get", app_id=app_id)

    def create(self, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return self._call("create", body=payload)

    def update(self, app_id: str | UUID, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return self._call("update", app_id=app_id, body=payload)

    def delete(self, app_id: str | UUID) -> None:
        self._call("delete", app_id=app_id)


class AsyncErrorAppsResource(AsyncResource):
    prefix = "error_app"

    def __init__(self, client: "AsyncUpassist"):
        super().__init__(client)
        self.issues = AsyncErrorAppIssuesResource(client)

    async def list(self, **kwargs: Any) -> Any:
        return await self._call("list", **kwargs)

    async def get(self, app_id: str | UUID) -> Any:
        return await self._call("get", app_id=app_id)

    async def create(self, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return await self._call("create", body=payload)

    async def update(self, app_id: str | UUID, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return await self._call("update", app_id=app_id, body=payload)

    async def delete(self, app_id: str | UUID) -> None:
        await self._call("delete", app_id=app_id)


# ---------------------------------------------------------------------------
# Status Pages Resource (Sync & Async)
# ---------------------------------------------------------------------------


class StatusPagesResource(SyncResource):
    prefix = "status_page"

    def list(self, **kwargs: Any) -> Any:
        return self._call("list", **kwargs)

    def get(self, status_page_id: str | UUID) -> Any:
        return self._call("get", status_page_id=status_page_id)

    def create(self, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return self._call("create", body=payload)

    def update(self, status_page_id: str | UUID, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return self._call("update", status_page_id=status_page_id, body=payload)

    def delete(self, status_page_id: str | UUID) -> None:
        self._call("delete", status_page_id=status_page_id)


class AsyncStatusPagesResource(AsyncResource):
    prefix = "status_page"

    async def list(self, **kwargs: Any) -> Any:
        return await self._call("list", **kwargs)

    async def get(self, status_page_id: str | UUID) -> Any:
        return await self._call("get", status_page_id=status_page_id)

    async def create(self, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return await self._call("create", body=payload)

    async def update(self, status_page_id: str | UUID, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return await self._call("update", status_page_id=status_page_id, body=payload)

    async def delete(self, status_page_id: str | UUID) -> None:
        await self._call("delete", status_page_id=status_page_id)


# ---------------------------------------------------------------------------
# Dashboards Resource (Sync & Async)
# ---------------------------------------------------------------------------


class DashboardsResource(SyncResource):
    prefix = "dashboard"

    def list(self, **kwargs: Any) -> Any:
        return self._call("list", **kwargs)

    def get(self, dashboard_id: str | UUID) -> Any:
        return self._call("get", dashboard_id=dashboard_id)

    def create(self, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return self._call("create", body=payload)

    def update(self, dashboard_id: str | UUID, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return self._call("update", dashboard_id=dashboard_id, body=payload)

    def delete(self, dashboard_id: str | UUID) -> None:
        self._call("delete", dashboard_id=dashboard_id)


class AsyncDashboardsResource(AsyncResource):
    prefix = "dashboard"

    async def list(self, **kwargs: Any) -> Any:
        return await self._call("list", **kwargs)

    async def get(self, dashboard_id: str | UUID) -> Any:
        return await self._call("get", dashboard_id=dashboard_id)

    async def create(self, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return await self._call("create", body=payload)

    async def update(self, dashboard_id: str | UUID, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return await self._call("update", dashboard_id=dashboard_id, body=payload)

    async def delete(self, dashboard_id: str | UUID) -> None:
        await self._call("delete", dashboard_id=dashboard_id)


# ---------------------------------------------------------------------------
# Project, Members & API Keys Resource (Sync & Async)
# ---------------------------------------------------------------------------


class ProjectMembersResource(SyncResource):
    prefix = "project_member"

    def list(self, **kwargs: Any) -> Any:
        return self._call("list", **kwargs)

    def delete(self, user_id: int) -> None:
        self._call("delete", user_id=user_id)


class AsyncProjectMembersResource(AsyncResource):
    prefix = "project_member"

    async def list(self, **kwargs: Any) -> Any:
        return await self._call("list", **kwargs)

    async def delete(self, user_id: int) -> None:
        await self._call("delete", user_id=user_id)


class ProjectInvitationsResource(SyncResource):
    prefix = "project_invitation"

    def list(self, **kwargs: Any) -> Any:
        return self._call("list", **kwargs)

    def create(self, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return self._call("create", body=payload)

    def delete(self, invitation_id: str | UUID) -> None:
        self._call("delete", invitation_id=invitation_id)


class AsyncProjectInvitationsResource(AsyncResource):
    prefix = "project_invitation"

    async def list(self, **kwargs: Any) -> Any:
        return await self._call("list", **kwargs)

    async def create(self, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return await self._call("create", body=payload)

    async def delete(self, invitation_id: str | UUID) -> None:
        await self._call("delete", invitation_id=invitation_id)


class APIKeysResource(SyncResource):
    prefix = "api_key"

    def list(self, **kwargs: Any) -> Any:
        return self._call("list", **kwargs)

    def get(self, api_key_id: str | UUID) -> Any:
        return self._call("get", api_key_id=api_key_id)

    def create(self, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return self._call("create", body=payload)

    def update(self, api_key_id: str | UUID, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return self._call("update", api_key_id=api_key_id, body=payload)

    def delete(self, api_key_id: str | UUID) -> None:
        self._call("delete", api_key_id=api_key_id)


class AsyncAPIKeysResource(AsyncResource):
    prefix = "api_key"

    async def list(self, **kwargs: Any) -> Any:
        return await self._call("list", **kwargs)

    async def get(self, api_key_id: str | UUID) -> Any:
        return await self._call("get", api_key_id=api_key_id)

    async def create(self, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return await self._call("create", body=payload)

    async def update(self, api_key_id: str | UUID, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return await self._call("update", api_key_id=api_key_id, body=payload)

    async def delete(self, api_key_id: str | UUID) -> None:
        await self._call("delete", api_key_id=api_key_id)


class ProjectResource(SyncResource):
    prefix = "project"

    def get(self) -> Any:
        return self._call("get")

    def quota(self) -> Any:
        return self._call("quota")


class AsyncProjectResource(AsyncResource):
    prefix = "project"

    async def get(self) -> Any:
        return await self._call("get")

    async def quota(self) -> Any:
        return await self._call("quota")


# ---------------------------------------------------------------------------
# Telemetry Ingestion (Logs, Metrics, Sites)
# ---------------------------------------------------------------------------


class LogsResource:
    """Structured log telemetry ingestion."""

    def __init__(self, client: "Upassist"):
        self._client = client

    def collect(self, *, service: str, logs: list[dict[str, Any]]) -> str:
        url = f"{LOGS_URL}/v1/logs/collect"
        payload = {"service": service, "logs": logs}
        resp = httpx.post(
            url,
            json=payload,
            headers={"Authorization": f"Bearer {self._client.api_key}"},
            timeout=15,
        )
        if resp.status_code >= 400:
            raise IngestError(resp.status_code, resp.text)
        return resp.text


class AsyncLogsResource:
    """Asynchronous structured log telemetry ingestion."""

    def __init__(self, client: "AsyncUpassist"):
        self._client = client

    async def collect(self, *, service: str, logs: list[dict[str, Any]]) -> str:
        url = f"{LOGS_URL}/v1/logs/collect"
        payload = {"service": service, "logs": logs}
        client = await self._client._http.get_async_httpx_client()
        resp = await client.post(url, json=payload, headers={"Authorization": f"Bearer {self._client.api_key}"})
        if resp.status_code >= 400:
            raise IngestError(resp.status_code, resp.text)
        return resp.text


class MetricsResource:
    """Custom metric telemetry ingestion."""

    def __init__(self, client: "Upassist"):
        self._client = client

    def collect(self, *, metrics: list[dict[str, Any]]) -> str:
        url = f"{METRICS_URL}/v1/metrics/collect"
        payload = {"metrics": metrics}
        resp = httpx.post(
            url,
            json=payload,
            headers={"Authorization": f"Bearer {self._client.api_key}"},
            timeout=15,
        )
        if resp.status_code >= 400:
            raise IngestError(resp.status_code, resp.text)
        return resp.text


class AsyncMetricsResource:
    """Asynchronous custom metric telemetry ingestion."""

    def __init__(self, client: "AsyncUpassist"):
        self._client = client

    async def collect(self, *, metrics: list[dict[str, Any]]) -> str:
        url = f"{METRICS_URL}/v1/metrics/collect"
        payload = {"metrics": metrics}
        client = await self._client._http.get_async_httpx_client()
        resp = await client.post(url, json=payload, headers={"Authorization": f"Bearer {self._client.api_key}"})
        if resp.status_code >= 400:
            raise IngestError(resp.status_code, resp.text)
        return resp.text


# ---------------------------------------------------------------------------
# Additional Resources (Escalation, Sites, Groups, Tags, Radar, Locations)
# ---------------------------------------------------------------------------


class EscalationPoliciesResource(SyncResource):
    prefix = "escalation_policy"

    def list(self, **kwargs: Any) -> Any:
        return self._call("list", **kwargs)

    def get(self, policy_id: str | UUID) -> Any:
        return self._call("get", policy_id=policy_id)

    def create(self, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return self._call("create", body=payload)

    def update(self, policy_id: str | UUID, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return self._call("update", policy_id=policy_id, body=payload)

    def delete(self, policy_id: str | UUID) -> None:
        self._call("delete", policy_id=policy_id)


class AsyncEscalationPoliciesResource(AsyncResource):
    prefix = "escalation_policy"

    async def list(self, **kwargs: Any) -> Any:
        return await self._call("list", **kwargs)

    async def get(self, policy_id: str | UUID) -> Any:
        return await self._call("get", policy_id=policy_id)

    async def create(self, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return await self._call("create", body=payload)

    async def update(self, policy_id: str | UUID, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return await self._call("update", policy_id=policy_id, body=payload)

    async def delete(self, policy_id: str | UUID) -> None:
        await self._call("delete", policy_id=policy_id)


class SitesResource(SyncResource):
    prefix = "site"

    def list(self, **kwargs: Any) -> Any:
        return self._call("list", **kwargs)

    def get(self, site_id: str | UUID) -> Any:
        return self._call("get", site_id=site_id)

    def create(self, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return self._call("create", body=payload)

    def update(self, site_id: str | UUID, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return self._call("update", site_id=site_id, body=payload)

    def delete(self, site_id: str | UUID) -> None:
        self._call("delete", site_id=site_id)


class AsyncSitesResource(AsyncResource):
    prefix = "site"

    async def list(self, **kwargs: Any) -> Any:
        return await self._call("list", **kwargs)

    async def get(self, site_id: str | UUID) -> Any:
        return await self._call("get", site_id=site_id)

    async def create(self, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return await self._call("create", body=payload)

    async def update(self, site_id: str | UUID, body: Any = None, **kwargs: Any) -> Any:
        payload = body if body is not None else kwargs
        return await self._call("update", site_id=site_id, body=payload)

    async def delete(self, site_id: str | UUID) -> None:
        await self._call("delete", site_id=site_id)


class GroupsResource(SyncResource):
    prefix = "group"

    def list(self, **kwargs: Any) -> Any:
        return self._call("list", **kwargs)


class AsyncGroupsResource(AsyncResource):
    prefix = "group"

    async def list(self, **kwargs: Any) -> Any:
        return await self._call("list", **kwargs)


class TagsResource(SyncResource):
    prefix = "tag"

    def list(self, **kwargs: Any) -> Any:
        return self._call("list", **kwargs)


class AsyncTagsResource(AsyncResource):
    prefix = "tag"

    async def list(self, **kwargs: Any) -> Any:
        return await self._call("list", **kwargs)


# ---------------------------------------------------------------------------
# HTTP Clients & Retry Transport
# ---------------------------------------------------------------------------


class _RetryTransport:
    """httpx transport wrapper that automatically retries idempotent transient errors."""

    def __init__(self, retries: int = 3):
        self.retries = retries

    def install(self, client: httpx.Client, verify: bool | str = True) -> httpx.Client:
        transport = httpx.HTTPTransport(retries=self.retries)
        return httpx.Client(
            base_url=client.base_url,
            cookies=client.cookies,
            headers=client.headers,
            timeout=client.timeout,
            verify=verify,
            follow_redirects=client.follow_redirects,
            transport=transport,
        )

    def install_async(self, client: httpx.AsyncClient, verify: bool | str = True) -> httpx.AsyncClient:
        transport = httpx.AsyncHTTPTransport(retries=self.retries)
        return httpx.AsyncClient(
            base_url=client.base_url,
            cookies=client.cookies,
            headers=client.headers,
            timeout=client.timeout,
            verify=verify,
            follow_redirects=client.follow_redirects,
            transport=transport,
        )


# ---------------------------------------------------------------------------
# Main Public Clients
# ---------------------------------------------------------------------------


class Upassist:
    """Official synchronous client for the Upassist Monitoring & Observability Platform.

    Args:
        api_key: Project API Key (defaults to UPASSIST_API_KEY environment variable).
        base_url: Management API URL (defaults to https://api.upassist.cloud).
        timeout: Request timeout in seconds (default: 30.0).
        retries: Number of automatic retries on transient connection errors (default: 3).
        verify_ssl: True, or path to CA bundle file.
    """

    def __init__(
        self,
        api_key: str | None = None,
        *,
        base_url: str = MANAGEMENT_URL,
        timeout: float = 30.0,
        retries: int = 3,
        verify_ssl: bool | str = True,
    ) -> None:
        key = api_key or os.environ.get("UPASSIST_API_KEY")
        if not key:
            raise ValueError(
                "Upassist API key is required. Pass api_key='up_live_...' or set the UPASSIST_API_KEY env variable."
            )
        self.api_key = key
        self.base_url = base_url.rstrip("/")

        self._http = AuthenticatedClient(
            base_url=self.base_url,
            token=self.api_key,
            timeout=httpx.Timeout(timeout),
            verify_ssl=verify_ssl,
        )
        if retries > 0:
            retry = _RetryTransport(retries=retries)
            self._http._client = retry.install(self._http.get_httpx_client(), verify=verify_ssl)

        # Resource Facades
        self.monitors = MonitorsResource(self)
        self.heartbeats = HeartbeatsResource(self)
        self.incidents = IncidentsResource(self)
        self.maintenance = MaintenanceResource(self)
        self.error_apps = ErrorAppsResource(self)
        self.status_pages = StatusPagesResource(self)
        self.dashboards = DashboardsResource(self)
        self.escalation_policies = EscalationPoliciesResource(self)
        self.members = ProjectMembersResource(self)
        self.invitations = ProjectInvitationsResource(self)
        self.api_keys = APIKeysResource(self)
        self.project = ProjectResource(self)
        self.sites = SitesResource(self)
        self.groups = GroupsResource(self)
        self.tags = TagsResource(self)
        self.logs = LogsResource(self)
        self.metrics = MetricsResource(self)

    def __enter__(self) -> Self:
        self._http.__enter__()
        return self

    def __exit__(self, *args: object) -> None:
        self._http.__exit__(*args)


class AsyncUpassist:
    """Official asynchronous (asyncio) client for the Upassist Monitoring & Observability Platform.

    Args:
        api_key: Project API Key (defaults to UPASSIST_API_KEY environment variable).
        base_url: Management API URL (defaults to https://api.upassist.cloud).
        timeout: Request timeout in seconds (default: 30.0).
        retries: Number of automatic retries on transient connection errors (default: 3).
        verify_ssl: True, or path to CA bundle file.
    """

    def __init__(
        self,
        api_key: str | None = None,
        *,
        base_url: str = MANAGEMENT_URL,
        timeout: float = 30.0,
        retries: int = 3,
        verify_ssl: bool | str = True,
    ) -> None:
        key = api_key or os.environ.get("UPASSIST_API_KEY")
        if not key:
            raise ValueError(
                "Upassist API key is required. Pass api_key='up_live_...' or set the UPASSIST_API_KEY env variable."
            )
        self.api_key = key
        self.base_url = base_url.rstrip("/")

        self._http = AuthenticatedClient(
            base_url=self.base_url,
            token=self.api_key,
            timeout=httpx.Timeout(timeout),
            verify_ssl=verify_ssl,
        )
        if retries > 0:
            retry = _RetryTransport(retries=retries)
            # Rebuild on async client instantiation
            self._http._async_client = retry.install_async(self._http.get_async_httpx_client(), verify=verify_ssl)

        # Asynchronous Resource Facades
        self.monitors = AsyncMonitorsResource(self)
        self.heartbeats = AsyncHeartbeatsResource(self)
        self.incidents = AsyncIncidentsResource(self)
        self.maintenance = AsyncMaintenanceResource(self)
        self.error_apps = AsyncErrorAppsResource(self)
        self.status_pages = AsyncStatusPagesResource(self)
        self.dashboards = AsyncDashboardsResource(self)
        self.escalation_policies = AsyncEscalationPoliciesResource(self)
        self.members = AsyncProjectMembersResource(self)
        self.invitations = AsyncProjectInvitationsResource(self)
        self.api_keys = AsyncAPIKeysResource(self)
        self.project = AsyncProjectResource(self)
        self.sites = AsyncSitesResource(self)
        self.groups = AsyncGroupsResource(self)
        self.tags = AsyncTagsResource(self)
        self.logs = AsyncLogsResource(self)
        self.metrics = AsyncMetricsResource(self)

    async def __aenter__(self) -> Self:
        await self._http.__aenter__()
        return self

    async def __aexit__(self, *args: object) -> None:
        await self._http.__aexit__(*args)
