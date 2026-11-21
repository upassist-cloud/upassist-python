"""Public client for the Upassist Management API.

Management calls go to ``https://api.upassist.cloud`` and require a project API key
sent as ``Authorization: Bearer <api_key>``. Ingest calls (heartbeat ping, log/metric
batches, RUM events) live on their own hosts and are grouped under the ``heartbeats``,
``logs``, ``metrics`` and ``sites`` resources.

Example::

    from upassist import Upassist

    client = Upassist(api_key="...")
    for monitor in client.monitors.iter(per_page=100):
        print(monitor.name, monitor.url)

    # maintenance windows (deploy-time silencing of alerts)
    client.maintenance.create(
        name="Deploy v2.3",
        started_at="2026-11-20T20:00:00Z",
        finished_at="2026-11-20T21:00:00Z",
        resources=[{"public_name": "api", "object_id": "...", "resource_type": "monitor"}],
    )

Async::

    from upassist import AsyncUpassist

    async with AsyncUpassist(api_key="...") as client:
        page = await client.monitors.list(page=1)
"""

from __future__ import annotations

import httpx
import importlib
import pkgutil
from typing import Any, AsyncIterator, Iterator, Self

from . import api as api_package
from .client import AuthenticatedClient, Client as _BaseClient
from .models.error import Error
from .types import Unset

HEARTBEATS_URL = "https://heartbeats.upassist.cloud"
LOGS_URL = "https://logs.upassist.cloud"
METRICS_URL = "https://metrics.upassist.cloud"
RUM_URL = "https://rum.upassist.cloud"


class APIError(Exception):
    """Raised when the API returns an error status code."""

    def __init__(self, code: str, message: str, request_id: str | None = None):
        super().__init__(message)
        self.code = code
        self.message = message
        self.request_id = request_id


class IngestError(Exception):
    """Raised by ingest helpers when the ingest host returns an error status."""

    def __init__(self, status_code: int, body: str):
        super().__init__(body)
        self.status_code = status_code
        self.body = body


def _operations() -> dict[str, Any]:
    found: dict[str, Any] = {}
    for module_info in pkgutil.walk_packages(api_package.__path__, api_package.__name__ + "."):
        module = importlib.import_module(module_info.name)
        sync = getattr(module, "sync", None)
        if sync is not None:
            found[module_info.name.rsplit(".", 1)[-1]] = sync
    return found


_OPERATIONS = _operations()


def _unwrap(operation: str, client: AuthenticatedClient, kwargs: dict[str, Any]) -> Any:
    parsed = _OPERATIONS[operation](client=client, **kwargs)
    if isinstance(parsed, Error):
        request_id = None if isinstance(parsed.request_id, Unset) else parsed.request_id
        raise APIError(parsed.code, parsed.message, request_id)
    return parsed


async def _unwrap_async(operation: str, client: AuthenticatedClient, kwargs: dict[str, Any]) -> Any:
    module_name = None
    for module_info in pkgutil.walk_packages(api_package.__path__, api_package.__name__ + "."):
        if module_info.name.rsplit(".", 1)[-1] == operation:
            module_name = module_info.name
            break
    if module_name is None:
        raise KeyError(operation)
    module = importlib.import_module(module_name)
    asyncio_fn = getattr(module, "asyncio", None)
    if asyncio_fn is None:
        raise AttributeError(f"{operation} has no async implementation")
    parsed = await asyncio_fn(client=client, **kwargs)
    if isinstance(parsed, Error):
        request_id = None if isinstance(parsed.request_id, Unset) else parsed.request_id
        raise APIError(parsed.code, parsed.message, request_id)
    return parsed


class _RetryTransport:
    """httpx transport with retries for transient failures."""

    def __init__(self, retries: int = 3, backoff_factor: float = 0.5) -> None:
        self.retries = retries
        self.backoff_factor = backoff_factor

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
            event_hooks=client.event_hooks,
        )

    async def install_async(
        self, client: httpx.AsyncClient, verify: bool | str = True
    ) -> httpx.AsyncClient:
        transport = httpx.AsyncHTTPTransport(retries=self.retries)
        return httpx.AsyncClient(
            base_url=client.base_url,
            cookies=client.cookies,
            headers=client.headers,
            timeout=client.timeout,
            verify=verify,
            follow_redirects=client.follow_redirects,
            transport=transport,
            event_hooks=client.event_hooks,
        )


class _Resource:
    """Base for typed resource wrappers."""

    prefix = ""

    def __init__(self, owner: "Upassist"):
        self._owner = owner

    def _call(self, name: str, **kwargs: Any) -> Any:
        operation = f"{self.prefix}_{name}"
        if operation not in _OPERATIONS:
            raise AttributeError(name)
        return _unwrap(operation, self._owner._http, kwargs)

    async def _call_async(self, name: str, **kwargs: Any) -> Any:
        operation = f"{self.prefix}_{name}"
        return await _unwrap_async(operation, self._owner._http, kwargs)

    def _paginate(self, name: str, **kwargs: Any) -> Iterator[dict[str, Any]]:
        """Yield every item across all pages of a list operation."""
        page = kwargs.pop("page", 1)
        per_page = kwargs.pop("per_page", 50)
        while True:
            response = self._call(name, page=page, per_page=per_page, **kwargs)
            data = getattr(response, "data", None) or []
            for item in data:
                yield item
            count = getattr(response, "count", None)
            total = getattr(response, "total_count", None)
            last = total if total is not None else count
            if last is None or page * per_page >= last:
                break
            page += 1

    async def _paginate_async(self, name: str, **kwargs: Any) -> AsyncIterator[dict[str, Any]]:
        page = kwargs.pop("page", 1)
        per_page = kwargs.pop("per_page", 50)
        while True:
            response = await self._call_async(name, page=page, per_page=per_page, **kwargs)
            data = getattr(response, "data", None) or []
            for item in data:
                yield item
            count = getattr(response, "count", None)
            total = getattr(response, "total_count", None)
            last = total if total is not None else count
            if last is None or page * per_page >= last:
                break
            page += 1


# ---------------------------------------------------------------------------
# Typed resources
# ---------------------------------------------------------------------------


class MonitorsResource(_Resource):
    prefix = "monitor"

    def list(
        self,
        *,
        q: str | None = None,
        group_id: str | None = None,
        tag_ids: list[str] | None = None,
        page: int = 1,
        per_page: int = 50,
        sort_by: str | None = None,
        ordering: str | None = None,
    ) -> Any:
        return self._call(
            "list",
            q=q,
            group_id=group_id,
            tag_ids=tag_ids,
            page=page,
            per_page=per_page,
            sort_by=sort_by,
            ordering=ordering,
        )

    def iter(self, **kwargs: Any) -> Iterator[dict[str, Any]]:
        return self._paginate("list", **kwargs)

    def get(self, monitor_id: str) -> Any:
        return self._call("get", monitor_id=monitor_id)

    def create(
        self,
        *,
        name: str,
        uri: str,
        locations: list[str] | None = None,
        tags: list[str] | None = None,
        **kwargs: Any,
    ) -> Any:
        return self._call("create", name=name, uri=uri, locations=locations, tags=tags, **kwargs)

    def update(self, monitor_id: str, **data: Any) -> Any:
        return self._call("update", monitor_id=monitor_id, **data)

    def delete(self, monitor_id: str) -> None:
        self._call("delete", monitor_id=monitor_id)

    def pause(self, monitor_id: str) -> Any:
        return self._call("pause", monitor_id=monitor_id)

    def unpause(self, monitor_id: str) -> Any:
        return self._call("unpause", monitor_id=monitor_id)

    def turn_on_alerts(self, monitor_id: str) -> Any:
        return self._call("turn_on_alerts", monitor_id=monitor_id)

    def turn_off_alerts(self, monitor_id: str) -> Any:
        return self._call("turn_off_alerts", monitor_id=monitor_id)

    def test_alert(self, monitor_id: str) -> Any:
        return self._call("test_alert", monitor_id=monitor_id)


class HeartbeatsResource(_Resource):
    prefix = "heartbeat"

    def list(
        self,
        *,
        q: str | None = None,
        group_id: str | None = None,
        tag_ids: list[str] | None = None,
        page: int = 1,
        per_page: int = 50,
        sort_by: str | None = None,
        ordering: str | None = None,
    ) -> Any:
        return self._call(
            "list",
            q=q,
            group_id=group_id,
            tag_ids=tag_ids,
            page=page,
            per_page=per_page,
            sort_by=sort_by,
            ordering=ordering,
        )

    def iter(self, **kwargs: Any) -> Iterator[dict[str, Any]]:
        return self._paginate("list", **kwargs)

    def get(self, heartbeat_slug: str) -> Any:
        return self._call("get", heartbeat_slug=heartbeat_slug)

    def create(self, **data: Any) -> Any:
        return self._call("create", **data)

    def update(self, heartbeat_slug: str, **data: Any) -> Any:
        return self._call("update", heartbeat_slug=heartbeat_slug, **data)

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

    def ping(self, slug: str, *, error: bool = False, message: str | None = None) -> str:
        params: dict[str, str] = {}
        if error:
            params["error"] = "true"
        if message is not None:
            params["errorMessage"] = message
        return self._owner._request(
            "GET",
            f"{HEARTBEATS_URL}/api/event/{slug}",
            params=params,
            token=self._owner.api_key,
        )


class IncidentsResource(_Resource):
    prefix = "incident"

    def list(self, **kwargs: Any) -> Any:
        return self._call("list", **kwargs)

    def iter(self, **kwargs: Any) -> Iterator[dict[str, Any]]:
        return self._paginate("list", **kwargs)

    def get(self, incident_id: str) -> Any:
        return self._call("get", incident_id=incident_id)

    def acknowledge(self, incident_id: str) -> Any:
        return self._call("acknowledge", incident_id=incident_id)

    def resolve(self, incident_id: str) -> Any:
        return self._call("resolve", incident_id=incident_id)


class SitesResource(_Resource):
    prefix = "site"

    def list(self, **kwargs: Any) -> Any:
        return self._call("list", **kwargs)

    def iter(self, **kwargs: Any) -> Iterator[dict[str, Any]]:
        return self._paginate("list", **kwargs)

    def get(self, site_id: str) -> Any:
        return self._call("get", site_id=site_id)

    def create(self, **data: Any) -> Any:
        return self._call("create", **data)

    def update(self, site_id: str, **data: Any) -> Any:
        return self._call("update", site_id=site_id, **data)

    def delete(self, site_id: str) -> None:
        self._call("delete", site_id=site_id)


class SourcesResource(_Resource):
    prefix = "source"

    def list(self, **kwargs: Any) -> Any:
        return self._call("list", **kwargs)

    def iter(self, **kwargs: Any) -> Iterator[dict[str, Any]]:
        return self._paginate("list", **kwargs)

    def get(self, source_id: str) -> Any:
        return self._call("get", source_id=source_id)

    def create(self, **data: Any) -> Any:
        return self._call("create", **data)

    def update(self, source_id: str, **data: Any) -> Any:
        return self._call("update", source_id=source_id, **data)

    def delete(self, source_id: str) -> None:
        self._call("delete", source_id=source_id)

    def pause(self, source_id: str) -> Any:
        return self._call("pause", source_id=source_id)

    def unpause(self, source_id: str) -> Any:
        return self._call("unpause", source_id=source_id)


class StatusPagesResource(_Resource):
    prefix = "status_page"

    def list(self, **kwargs: Any) -> Any:
        return self._call("list", **kwargs)

    def iter(self, **kwargs: Any) -> Iterator[dict[str, Any]]:
        return self._paginate("list", **kwargs)

    def get(self, status_page_id: str) -> Any:
        return self._call("get", status_page_id=status_page_id)

    def create(self, **data: Any) -> Any:
        return self._call("create", **data)

    def update(self, status_page_id: str, **data: Any) -> Any:
        return self._call("update", status_page_id=status_page_id, **data)

    def delete(self, status_page_id: str) -> None:
        self._call("delete", status_page_id=status_page_id)


class IntegrationsResource(_Resource):
    prefix = "integration"

    def list(self, **kwargs: Any) -> Any:
        return self._call("list", **kwargs)

    def iter(self, **kwargs: Any) -> Iterator[dict[str, Any]]:
        return self._paginate("list", **kwargs)

    def get(self, integration_id: str) -> Any:
        return self._call("get", integration_id=integration_id)

    def create(self, **data: Any) -> Any:
        return self._call("create", **data)

    def update(self, integration_id: str, **data: Any) -> Any:
        return self._call("update", integration_id=integration_id, **data)

    def delete(self, integration_id: str) -> None:
        self._call("delete", integration_id=integration_id)

    def activate(self, integration_id: str) -> Any:
        return self._call("activate", integration_id=integration_id)

    def deactivate(self, integration_id: str) -> Any:
        return self._call("deactivate", integration_id=integration_id)


class GroupsResource(_Resource):
    prefix = "group"

    def list(self, **kwargs: Any) -> Any:
        return self._call("list", **kwargs)

    def iter(self, **kwargs: Any) -> Iterator[dict[str, Any]]:
        return self._paginate("list", **kwargs)


class TagsResource(_Resource):
    prefix = "tag"

    def list(self, **kwargs: Any) -> Any:
        return self._call("list", **kwargs)

    def iter(self, **kwargs: Any) -> Iterator[dict[str, Any]]:
        return self._paginate("list", **kwargs)


class HeartbeatGroupsResource(_Resource):
    prefix = "heartbeat_group"

    def list(self, **kwargs: Any) -> Any:
        return self._call("list", **kwargs)

    def iter(self, **kwargs: Any) -> Iterator[dict[str, Any]]:
        return self._paginate("list", **kwargs)

    def assign(self, **data: Any) -> Any:
        return self._call("assign", **data)


class MonitorGroupsResource(_Resource):
    prefix = "monitor_group"

    def list(self, **kwargs: Any) -> Any:
        return self._call("list", **kwargs)

    def iter(self, **kwargs: Any) -> Iterator[dict[str, Any]]:
        return self._paginate("list", **kwargs)

    def assign(self, **data: Any) -> Any:
        return self._call("assign", **data)


class SiteGroupsResource(_Resource):
    prefix = "site_group"

    def list(self, **kwargs: Any) -> Any:
        return self._call("list", **kwargs)

    def iter(self, **kwargs: Any) -> Iterator[dict[str, Any]]:
        return self._paginate("list", **kwargs)

    def assign(self, **data: Any) -> Any:
        return self._call("assign", **data)


class RadarPagesResource(_Resource):
    prefix = "radar_page"

    def list(self, **kwargs: Any) -> Any:
        return self._call("list", **kwargs)

    def iter(self, **kwargs: Any) -> Iterator[dict[str, Any]]:
        return self._paginate("list", **kwargs)

    def create(self, **data: Any) -> Any:
        return self._call("create", **data)

    def delete(self, radar_page_id: str) -> None:
        self._call("delete", radar_page_id=radar_page_id)


class RadarSettingsResource(_Resource):
    prefix = "radar_settings"

    def get(self) -> Any:
        return self._call("get")

    def update(self, **data: Any) -> Any:
        return self._call("update", **data)


class MaintenanceResource(_Resource):
    prefix = "maintenance"

    def list(
        self,
        *,
        q: str | None = None,
        page: int = 1,
        per_page: int = 50,
        timeline_type: str | None = None,
        status_page_id: str | None = None,
    ) -> Any:
        return self._call(
            "list",
            q=q,
            page=page,
            per_page=per_page,
            timeline_type=timeline_type,
            status_page_id=status_page_id,
        )

    def iter(self, **kwargs: Any) -> Iterator[dict[str, Any]]:
        return self._paginate("list", **kwargs)

    def get(self, maintenance_id: str) -> Any:
        return self._call("get", maintenance_id=maintenance_id)

    def create(self, **data: Any) -> Any:
        return self._call("create", **data)

    def update(self, maintenance_id: str, **data: Any) -> Any:
        return self._call("update", maintenance_id=maintenance_id, **data)

    def delete(self, maintenance_id: str) -> None:
        self._call("delete", maintenance_id=maintenance_id)

    def end(self, maintenance_id: str) -> Any:
        return self._call("end", maintenance_id=maintenance_id)


class LocationsResource(_Resource):
    prefix = "location"

    def list(self, **kwargs: Any) -> Any:
        return self._call("list", **kwargs)

    def iter(self, **kwargs: Any) -> Iterator[dict[str, Any]]:
        return self._paginate("list", **kwargs)


class PlatformsResource(_Resource):
    prefix = "platform"

    def list(self, **kwargs: Any) -> Any:
        return self._call("list", **kwargs)

    def iter(self, **kwargs: Any) -> Iterator[dict[str, Any]]:
        return self._paginate("list", **kwargs)


class EscalationPoliciesResource(_Resource):
    prefix = "escalation_policy"

    def list(
        self,
        *,
        q: str | None = None,
        page: int = 1,
        per_page: int = 20,
        sort_by: str | None = None,
        ordering: str | None = None,
    ) -> Any:
        return self._call(
            "list",
            q=q,
            page=page,
            per_page=per_page,
            sort_by=sort_by,
            ordering=ordering,
        )

    def iter(self, **kwargs: Any) -> Iterator[dict[str, Any]]:
        return self._paginate("list", **kwargs)

    def get(self, policy_id: str) -> Any:
        return self._call("get", policy_id=policy_id)

    def create(self, **data: Any) -> Any:
        return self._call("create", **data)

    def update(self, policy_id: str, **data: Any) -> Any:
        return self._call("update", policy_id=policy_id, **data)

    def delete(self, policy_id: str) -> None:
        self._call("delete", policy_id=policy_id)


class ErrorAppsResource(_Resource):
    prefix = "error_app"

    def list(
        self,
        *,
        q: str | None = None,
        group_id: str | None = None,
    ) -> Any:
        return self._call("list", q=q, group_id=group_id)

    def iter(self, **kwargs: Any) -> Iterator[dict[str, Any]]:
        return self._paginate("list", **kwargs)

    def get(self, error_app_id: str) -> Any:
        return self._call("get", error_app_id=error_app_id)

    def create(self, **data: Any) -> Any:
        return self._call("create", **data)

    def update(self, error_app_id: str, **data: Any) -> Any:
        return self._call("update", error_app_id=error_app_id, **data)

    def delete(self, error_app_id: str) -> None:
        self._call("delete", error_app_id=error_app_id)

    def sdk_setup(self, error_app_id: str) -> Any:
        return self._call("sdk_setup", error_app_id=error_app_id)

    def test_event(self, error_app_id: str) -> Any:
        return self._call("test_event", error_app_id=error_app_id)

    def list_issues(
        self,
        error_app_id: str,
        *,
        page: int = 1,
        per_page: int = 20,
        q: str | None = None,
        is_resolved: bool | None = None,
        is_muted: bool | None = None,
        environment: str | None = None,
        level: str | None = None,
        period: str | None = None,
        sort: str | None = None,
    ) -> Any:
        return _unwrap(
            "error_app_issue_list",
            self._owner._http,
            {
                "error_app_id": error_app_id,
                "page": page,
                "per_page": per_page,
                "q": q,
                "is_resolved": is_resolved,
                "is_muted": is_muted,
                "environment": environment,
                "level": level,
                "period": period,
                "sort": sort,
            },
        )

    def get_issue(self, error_app_id: str, issue_id: str) -> Any:
        return _unwrap(
            "error_app_issue_get",
            self._owner._http,
            {"error_app_id": error_app_id, "issue_id": issue_id},
        )

    def update_issue(self, error_app_id: str, issue_id: str, **data: Any) -> Any:
        return _unwrap(
            "error_app_issue_update",
            self._owner._http,
            {"error_app_id": error_app_id, "issue_id": issue_id, **data},
        )

    def delete_issue(self, error_app_id: str, issue_id: str) -> None:
        _unwrap(
            "error_app_issue_delete",
            self._owner._http,
            {"error_app_id": error_app_id, "issue_id": issue_id},
        )


class DashboardsResource(_Resource):
    prefix = "dashboard"

    def list(
        self,
        *,
        q: str | None = None,
        group_id: str | None = None,
    ) -> Any:
        return self._call("list", q=q, group_id=group_id)

    def iter(self, **kwargs: Any) -> Iterator[dict[str, Any]]:
        return self._paginate("list", **kwargs)

    def get(self, dashboard_id: str) -> Any:
        return self._call("get", dashboard_id=dashboard_id)

    def create(self, **data: Any) -> Any:
        return self._call("create", **data)

    def update(self, dashboard_id: str, **data: Any) -> Any:
        return self._call("update", dashboard_id=dashboard_id, **data)

    def delete(self, dashboard_id: str) -> None:
        self._call("delete", dashboard_id=dashboard_id)


class ProjectResource(_Resource):
    prefix = "project"

    def get(self) -> Any:
        return self._call("get")


class StatusPageSectionsResource(_Resource):
    prefix = "status_page_section"

    def list(self, status_page_id: str) -> Any:
        return self._call("list", status_page_id=status_page_id)

    def create(self, status_page_id: str, **data: Any) -> Any:
        return self._call("create", status_page_id=status_page_id, **data)

    def update(self, status_page_id: str, section_id: str, **data: Any) -> Any:
        return self._call("update", status_page_id=status_page_id, section_id=section_id, **data)

    def delete(self, status_page_id: str, section_id: str) -> None:
        self._call("delete", status_page_id=status_page_id, section_id=section_id)


class StatusPageReportsResource(_Resource):
    prefix = "status_page_report"

    def list(self, status_page_id: str) -> Any:
        return self._call("list", status_page_id=status_page_id)

    def create(self, status_page_id: str, **data: Any) -> Any:
        return self._call("create", status_page_id=status_page_id, **data)

    def get(self, status_page_id: str, report_id: str) -> Any:
        return self._call("get", status_page_id=status_page_id, report_id=report_id)

    def delete(self, status_page_id: str, report_id: str) -> None:
        self._call("delete", status_page_id=status_page_id, report_id=report_id)


class StatusPageSubscribersResource(_Resource):
    prefix = "status_page_subscriber"

    def list(self, status_page_id: str, *, page: int = 1, per_page: int = 20) -> Any:
        return self._call("list", status_page_id=status_page_id, page=page, per_page=per_page)

    def iter(self, status_page_id: str, **kwargs: Any) -> Iterator[dict[str, Any]]:
        return self._paginate("list", status_page_id=status_page_id, **kwargs)

    def create(self, status_page_id: str, *, email: str) -> Any:
        return self._call("create", status_page_id=status_page_id, body={"email": email})

    def delete(self, status_page_id: str, subscriber_id: str) -> None:
        self._call("delete", status_page_id=status_page_id, subscriber_id=subscriber_id)


class ProjectMembersResource(_Resource):
    prefix = "project_member"

    def list(self) -> Any:
        return self._call("list")

    def delete(self, member_id: str) -> None:
        self._call("delete", member_id=member_id)


class ProjectInvitationsResource(_Resource):
    prefix = "project_invitation"

    def list(self) -> Any:
        return self._call("list")

    def create(self, **data: Any) -> Any:
        return self._call("create", **data)

    def delete(self, invitation_id: str) -> None:
        self._call("delete", invitation_id=invitation_id)


class APIKeysResource(_Resource):
    prefix = "api_key"

    def list(self, *, page: int = 1, per_page: int = 20, q: str | None = None, **kwargs: Any) -> Any:
        return self._call("list", page=page, per_page=per_page, q=q, **kwargs)

    def iter(self, **kwargs: Any) -> Iterator[dict[str, Any]]:
        return self._paginate("list", **kwargs)

    def get(self, api_key_id: str) -> Any:
        return self._call("get", api_key_id=api_key_id)

    def create(self, **data: Any) -> Any:
        return self._call("create", **data)

    def update(self, api_key_id: str, **data: Any) -> Any:
        return self._call("update", api_key_id=api_key_id, **data)

    def delete(self, api_key_id: str) -> None:
        self._call("delete", api_key_id=api_key_id)


class LogsResource:
    """Ingest helpers for logs (separate host)."""

    def __init__(self, owner: "Upassist"):
        self._owner = owner

    def collect(self, entries: list[dict[str, Any]], *, token: str) -> str:
        return self._owner._request("POST", f"{LOGS_URL}/collect", json=entries, token=token)


class MetricsResource:
    """Ingest helpers for metrics (separate host)."""

    def __init__(self, owner: "Upassist"):
        self._owner = owner

    def collect(self, points: list[dict[str, Any]], *, token: str) -> str:
        return self._owner._request("POST", f"{METRICS_URL}/collect", json=points, token=token)


class SitesIngestResource:
    """Ingest helpers for RUM site events (separate host)."""

    def __init__(self, owner: "Upassist"):
        self._owner = owner

    def track(self, event: dict[str, Any]) -> str:
        return self._owner._request("POST", f"{RUM_URL}/api/sites/events", json=event)


# ---------------------------------------------------------------------------
# Top-level clients
# ---------------------------------------------------------------------------


class Upassist:
    """Sync management client plus ingest helpers on their own hosts."""

    def __init__(
        self,
        api_key: str,
        *,
        base_url: str = "https://api.upassist.cloud",
        timeout: float = 30,
        retries: int = 3,
    ) -> None:
        self.api_key = api_key
        self._http = AuthenticatedClient(
            base_url=base_url,
            token=api_key,
            timeout=httpx.Timeout(timeout),
        )
        # Apply retry transport.
        retry = _RetryTransport(retries=retries)
        self._http._client = retry.install(
            self._http.get_httpx_client(), verify=self._http._verify_ssl
        )
        self._http._async_client = None  # force rebuild on async access

        self.monitors = MonitorsResource(self)
        self.heartbeats = HeartbeatsResource(self)
        self.incidents = IncidentsResource(self)
        self.sites = SitesResource(self)
        self.sources = SourcesResource(self)
        self.status_pages = StatusPagesResource(self)
        self.integrations = IntegrationsResource(self)
        self.groups = GroupsResource(self)
        self.tags = TagsResource(self)
        self.heartbeat_groups = HeartbeatGroupsResource(self)
        self.monitor_groups = MonitorGroupsResource(self)
        self.site_groups = SiteGroupsResource(self)
        self.radar_pages = RadarPagesResource(self)
        self.radar_settings = RadarSettingsResource(self)
        self.maintenance = MaintenanceResource(self)
        self.locations = LocationsResource(self)
        self.platforms = PlatformsResource(self)
        self.escalation_policies = EscalationPoliciesResource(self)
        self.error_apps = ErrorAppsResource(self)
        self.dashboards = DashboardsResource(self)
        self.project = ProjectResource(self)
        self.status_page_sections = StatusPageSectionsResource(self)
        self.status_page_reports = StatusPageReportsResource(self)
        self.status_page_subscribers = StatusPageSubscribersResource(self)
        self.members = ProjectMembersResource(self)
        self.invitations = ProjectInvitationsResource(self)
        self.api_keys = APIKeysResource(self)
        self.logs = LogsResource(self)
        self.metrics = MetricsResource(self)
        self.sites_ingest = SitesIngestResource(self)

    def __enter__(self) -> Self:
        self._http.__enter__()
        return self

    def __exit__(self, *args: object) -> None:
        self._http.__exit__(*args)

    def _request(self, method: str, url: str, *, token: str | None = None, **kwargs: Any) -> str:
        headers = dict(kwargs.pop("headers", {}))
        if token:
            headers["Authorization"] = f"Bearer {token}"
        response = httpx.request(
            method,
            url,
            headers=headers,
            timeout=self._http._timeout or 30,
            **kwargs,
        )
        if response.status_code >= 400:
            raise IngestError(response.status_code, response.text)
        return response.text


class AsyncUpassist:
    """Async management client plus ingest helpers on their own hosts."""

    def __init__(
        self,
        api_key: str,
        *,
        base_url: str = "https://api.upassist.cloud",
        timeout: float = 30,
        retries: int = 3,
    ) -> None:
        self.api_key = api_key
        self._http = AuthenticatedClient(
            base_url=base_url,
            token=api_key,
            timeout=httpx.Timeout(timeout),
        )
        self.monitors = MonitorsResource(self)
        self.heartbeats = HeartbeatsResource(self)
        self.incidents = IncidentsResource(self)
        self.sites = SitesResource(self)
        self.sources = SourcesResource(self)
        self.status_pages = StatusPagesResource(self)
        self.integrations = IntegrationsResource(self)
        self.groups = GroupsResource(self)
        self.tags = TagsResource(self)
        self.heartbeat_groups = HeartbeatGroupsResource(self)
        self.monitor_groups = MonitorGroupsResource(self)
        self.site_groups = SiteGroupsResource(self)
        self.radar_pages = RadarPagesResource(self)
        self.radar_settings = RadarSettingsResource(self)
        self.maintenance = MaintenanceResource(self)
        self.locations = LocationsResource(self)
        self.platforms = PlatformsResource(self)
        self.escalation_policies = EscalationPoliciesResource(self)
        self.error_apps = ErrorAppsResource(self)
        self.dashboards = DashboardsResource(self)
        self.project = ProjectResource(self)
        self.status_page_sections = StatusPageSectionsResource(self)
        self.status_page_reports = StatusPageReportsResource(self)
        self.status_page_subscribers = StatusPageSubscribersResource(self)
        self.members = ProjectMembersResource(self)
        self.invitations = ProjectInvitationsResource(self)
        self.api_keys = APIKeysResource(self)
        self.logs = LogsResource(self)
        self.metrics = MetricsResource(self)
        self.sites_ingest = SitesIngestResource(self)

    async def __aenter__(self) -> Self:
        await self._http.__aenter__()
        return self

    async def __aexit__(self, *args: object) -> None:
        await self._http.__aexit__(*args)


# Backwards-compatible alias.
Client = Upassist
