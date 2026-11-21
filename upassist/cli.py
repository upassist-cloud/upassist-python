"""Command-line interface for Upassist.

Usage:
    upassist whoami
    upassist monitors list
    upassist heartbeats ping <slug>
    upassist heartbeats run <slug> -- <command...>
    upassist incidents list
    upassist maintenance list
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

from .sdk import APIError, IngestError, Upassist

CONFIG_DIR = Path.home() / ".config" / "upassist"
CONFIG_FILE = CONFIG_DIR / "config.json"


def _load_config() -> dict[str, str]:
    if CONFIG_FILE.exists():
        try:
            return json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def _save_config(data: dict[str, str]) -> None:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    existing = _load_config()
    existing.update(data)
    CONFIG_FILE.write_text(json.dumps(existing, indent=2), encoding="utf-8")


def _get_api_key(args: argparse.Namespace) -> str:
    key = getattr(args, "api_key", None)
    if key:
        return key
    env_key = os.environ.get("UPASSIST_API_KEY")
    if env_key:
        return env_key
    conf = _load_config()
    conf_key = conf.get("api_key")
    if conf_key:
        return conf_key
    sys.stderr.write(
        "Error: API key is required. Provide --api-key, set UPASSIST_API_KEY, "
        "or run 'upassist auth login <key>'.\n"
    )
    sys.exit(1)


def _get_client(args: argparse.Namespace) -> Upassist:
    api_key = _get_api_key(args)
    base_url = (
        getattr(args, "base_url", None)
        or os.environ.get("UPASSIST_BASE_URL")
        or "https://api.upassist.cloud"
    )
    return Upassist(api_key=api_key, base_url=base_url)


def _print_output(data: Any, as_json: bool = False) -> None:
    if as_json:
        if hasattr(data, "to_dict"):
            print(json.dumps(data.to_dict(), indent=2))
        elif isinstance(data, (dict, list)):
            print(json.dumps(data, indent=2, default=str))
        else:
            print(json.dumps(getattr(data, "__dict__", str(data)), indent=2, default=str))
        return

    # Formatted human output
    if hasattr(data, "to_dict"):
        data = data.to_dict()
    if isinstance(data, dict):
        for k, v in data.items():
            print(f"  {k}: {v}")
    elif isinstance(data, list):
        if not data:
            print("  (empty)")
            return
        for item in data:
            if hasattr(item, "to_dict"):
                item = item.to_dict()
            if isinstance(item, dict):
                first_few = [f"{k}={v}" for k, v in list(item.items())[:4]]
                print("  * " + ", ".join(first_few))
            else:
                print(f"  * {item}")
    else:
        print(data)


# ---------------------------------------------------------------------------
# Command Handlers
# ---------------------------------------------------------------------------


def cmd_auth_login(args: argparse.Namespace) -> None:
    _save_config({"api_key": args.key})
    print(f"Saved API key to {CONFIG_FILE}")


def cmd_whoami(args: argparse.Namespace) -> None:
    client = _get_client(args)
    try:
        project = client.project.get()
        if args.json:
            _print_output(project, as_json=True)
            return
        p_dict = project.to_dict() if hasattr(project, "to_dict") else project
        print(f"Project: {p_dict.get('name')} (ID: {p_dict.get('id')})")
        print(f"Plan:    {p_dict.get('tariff_name')} (Paid: {p_dict.get('is_paid')})")
        quotas = p_dict.get("quotas", {})
        print("Quotas:")
        print(f"  Monitors:   {quotas.get('monitors_used', 0)} / {quotas.get('monitors_limit', 'unlimited')}")
        print(f"  Heartbeats: {quotas.get('heartbeats_used', 0)} / {quotas.get('heartbeats_limit', 'unlimited')}")
        print(f"  Sites:      {quotas.get('sites_used', 0)} / {quotas.get('sites_limit', 'unlimited')}")
        print(f"  Members:    limit {quotas.get('members_limit', 'unlimited')}")
    except APIError as e:
        sys.stderr.write(f"API Error ({e.code}): {e.message}\n")
        sys.exit(1)


def cmd_monitors_list(args: argparse.Namespace) -> None:
    client = _get_client(args)
    page = client.monitors.list(page=args.page, per_page=args.per_page, q=args.query)
    data = getattr(page, "data", [])
    if args.json:
        _print_output([item.to_dict() if hasattr(item, "to_dict") else item for item in data], as_json=True)
        return
    print(f"Monitors ({len(data)} items):")
    for m in data:
        m_dict = m.to_dict() if hasattr(m, "to_dict") else m
        status = "PAUSED" if m_dict.get("is_paused") else "ACTIVE"
        print(f"  [{status}] {m_dict.get('name', 'Unnamed')} -> {m_dict.get('url', '')} (id: {m_dict.get('id')})")


def cmd_monitors_pause(args: argparse.Namespace) -> None:
    client = _get_client(args)
    client.monitors.pause(args.monitor_id)
    print(f"Monitor {args.monitor_id} paused.")


def cmd_monitors_unpause(args: argparse.Namespace) -> None:
    client = _get_client(args)
    client.monitors.unpause(args.monitor_id)
    print(f"Monitor {args.monitor_id} unpaused.")


def cmd_monitors_test(args: argparse.Namespace) -> None:
    client = _get_client(args)
    client.monitors.test_alert(args.monitor_id)
    print(f"Test alert triggered for monitor {args.monitor_id}.")


def cmd_heartbeats_list(args: argparse.Namespace) -> None:
    client = _get_client(args)
    page = client.heartbeats.list(page=args.page, per_page=args.per_page, q=args.query)
    data = getattr(page, "data", [])
    if args.json:
        _print_output([item.to_dict() if hasattr(item, "to_dict") else item for item in data], as_json=True)
        return
    print(f"Heartbeats ({len(data)} items):")
    for h in data:
        h_dict = h.to_dict() if hasattr(h, "to_dict") else h
        status = "PAUSED" if h_dict.get("is_paused") else "ACTIVE"
        print(f"  [{status}] {h_dict.get('name', 'Unnamed')} (slug: {h_dict.get('slug')}, period: {h_dict.get('period')}s)")


def cmd_heartbeats_ping(args: argparse.Namespace) -> None:
    client = _get_client(args)
    try:
        resp = client.heartbeats.ping(args.slug, error=args.error, message=args.message)
        print(f"Ping sent for '{args.slug}': {resp.strip()}")
    except IngestError as e:
        sys.stderr.write(f"Ping failed (HTTP {e.status_code}): {e.body}\n")
        sys.exit(1)


def cmd_heartbeats_run(args: argparse.Namespace) -> None:
    """Wraps command execution: pings heartbeat on start/success or failure."""
    client = _get_client(args)
    slug = args.slug
    cmd = args.command
    if not cmd:
        sys.stderr.write("Error: command to run is required after --\n")
        sys.exit(1)

    # Execute wrapped command
    process = subprocess.run(cmd)
    if process.returncode != 0:
        err_msg = f"Command failed with exit code {process.returncode}: {' '.join(cmd)}"
        try:
            client.heartbeats.ping(slug, error=True, message=err_msg)
        except Exception as e:
            sys.stderr.write(f"Warning: could not report error ping to heartbeat: {e}\n")
        sys.exit(process.returncode)
    else:
        try:
            client.heartbeats.ping(slug, error=False)
        except Exception as e:
            sys.stderr.write(f"Warning: could not report success ping to heartbeat: {e}\n")
        sys.exit(0)


def cmd_incidents_list(args: argparse.Namespace) -> None:
    client = _get_client(args)
    page = client.incidents.list(page=args.page, per_page=args.per_page)
    data = getattr(page, "data", [])
    if args.json:
        _print_output([item.to_dict() if hasattr(item, "to_dict") else item for item in data], as_json=True)
        return
    print(f"Incidents ({len(data)} items):")
    for inc in data:
        i_dict = inc.to_dict() if hasattr(inc, "to_dict") else inc
        res = "RESOLVED" if i_dict.get("resolved_at") else ("ACK" if i_dict.get("acknowledged_at") else "OPEN")
        print(f"  [{res}] {i_dict.get('summary', 'Incident')} (ID: {i_dict.get('id')})")


def cmd_incidents_ack(args: argparse.Namespace) -> None:
    client = _get_client(args)
    client.incidents.acknowledge(args.incident_id)
    print(f"Incident {args.incident_id} acknowledged.")


def cmd_incidents_resolve(args: argparse.Namespace) -> None:
    client = _get_client(args)
    client.incidents.resolve(args.incident_id)
    print(f"Incident {args.incident_id} resolved.")


def cmd_maintenance_list(args: argparse.Namespace) -> None:
    client = _get_client(args)
    page = client.maintenance.list(page=args.page, per_page=args.per_page)
    data = getattr(page, "data", [])
    if args.json:
        _print_output([item.to_dict() if hasattr(item, "to_dict") else item for item in data], as_json=True)
        return
    print(f"Maintenance Windows ({len(data)} items):")
    for m in data:
        m_dict = m.to_dict() if hasattr(m, "to_dict") else m
        print(f"  * {m_dict.get('name')} [{m_dict.get('started_at')} to {m_dict.get('finished_at')}] (ID: {m_dict.get('id')})")


def cmd_maintenance_end(args: argparse.Namespace) -> None:
    client = _get_client(args)
    client.maintenance.end(args.maintenance_id)
    print(f"Maintenance window {args.maintenance_id} ended.")


def cmd_members_list(args: argparse.Namespace) -> None:
    client = _get_client(args)
    members = client.members.list()
    if args.json:
        _print_output([m.to_dict() if hasattr(m, "to_dict") else m for m in members], as_json=True)
        return
    print(f"Project Members ({len(members)}):")
    for m in members:
        m_dict = m.to_dict() if hasattr(m, "to_dict") else m
        user = m_dict.get("user", {})
        print(f"  * {user.get('email', 'No email')} - Role: {m_dict.get('role')} (ID: {m_dict.get('id')})")


def cmd_api_keys_list(args: argparse.Namespace) -> None:
    client = _get_client(args)
    page = client.api_keys.list()
    data = getattr(page, "data", [])
    if args.json:
        _print_output([k.to_dict() if hasattr(k, "to_dict") else k for k in data], as_json=True)
        return
    print(f"API Keys ({len(data)}):")
    for k in data:
        k_dict = k.to_dict() if hasattr(k, "to_dict") else k
        scopes = ", ".join(k_dict.get("scopes") or ["ALL"])
        print(f"  * {k_dict.get('name', 'Key')} (id: {k_dict.get('id')}) - Scopes: [{scopes}]")


# ---------------------------------------------------------------------------
# CLI Argument Parser Setup
# ---------------------------------------------------------------------------


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="upassist",
        description="Official CLI for the Upassist Monitoring & Observability Platform",
    )
    parser.add_argument("--api-key", help="Upassist Project API Key (overrides env and config)")
    parser.add_argument("--base-url", help="Base URL for the management API")
    parser.add_argument("--json", action="store_true", help="Output raw JSON instead of human-formatted text")

    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # auth
    auth_parser = subparsers.add_parser("auth", help="Manage CLI authentication")
    auth_sub = auth_parser.add_subparsers(dest="auth_command")
    login_p = auth_sub.add_parser("login", help="Save project API key to config")
    login_p.add_argument("key", help="Project API Key")
    login_p.set_defaults(func=cmd_auth_login)

    # whoami
    whoami_p = subparsers.add_parser("whoami", help="Display current authenticated project details and quotas")
    whoami_p.set_defaults(func=cmd_whoami)

    status_p = subparsers.add_parser("status", help="Alias for whoami")
    status_p.set_defaults(func=cmd_whoami)

    # monitors
    mon_parser = subparsers.add_parser("monitors", help="Manage uptime monitors")
    mon_sub = mon_parser.add_subparsers(dest="monitors_command")
    mon_list = mon_sub.add_parser("list", help="List monitors")
    mon_list.add_argument("--page", type=int, default=1)
    mon_list.add_argument("--per-page", type=int, default=50)
    mon_list.add_argument("--query", "-q", help="Filter by name/url")
    mon_list.set_defaults(func=cmd_monitors_list)

    mon_pause = mon_sub.add_parser("pause", help="Pause a monitor")
    mon_pause.add_argument("monitor_id", help="Monitor UUID")
    mon_pause.set_defaults(func=cmd_monitors_pause)

    mon_unpause = mon_sub.add_parser("unpause", help="Unpause a monitor")
    mon_unpause.add_argument("monitor_id", help="Monitor UUID")
    mon_unpause.set_defaults(func=cmd_monitors_unpause)

    mon_test = mon_sub.add_parser("test-alert", help="Send a test alert for a monitor")
    mon_test.add_argument("monitor_id", help="Monitor UUID")
    mon_test.set_defaults(func=cmd_monitors_test)

    # heartbeats
    hb_parser = subparsers.add_parser("heartbeats", help="Manage and ping cron heartbeats")
    hb_sub = hb_parser.add_subparsers(dest="heartbeats_command")
    hb_list = hb_sub.add_parser("list", help="List heartbeats")
    hb_list.add_argument("--page", type=int, default=1)
    hb_list.add_argument("--per-page", type=int, default=50)
    hb_list.add_argument("--query", "-q", help="Filter by name/slug")
    hb_list.set_defaults(func=cmd_heartbeats_list)

    hb_ping = hb_sub.add_parser("ping", help="Ping a heartbeat slug")
    hb_ping.add_argument("slug", help="Heartbeat slug")
    hb_ping.add_argument("--error", action="store_true", help="Report a failure event")
    hb_ping.add_argument("--message", help="Optional error or status message")
    hb_ping.set_defaults(func=cmd_heartbeats_ping)

    hb_run = hb_sub.add_parser("run", help="Wrap a command execution with heartbeat telemetry")
    hb_run.add_argument("slug", help="Heartbeat slug")
    hb_run.add_argument("command", nargs=argparse.REMAINDER, help="Command to run after --")
    hb_run.set_defaults(func=cmd_heartbeats_run)

    # incidents
    inc_parser = subparsers.add_parser("incidents", help="View and acknowledge incidents")
    inc_sub = inc_parser.add_subparsers(dest="incidents_command")
    inc_list = inc_sub.add_parser("list", help="List incidents")
    inc_list.add_argument("--page", type=int, default=1)
    inc_list.add_argument("--per-page", type=int, default=50)
    inc_list.set_defaults(func=cmd_incidents_list)

    inc_ack = inc_sub.add_parser("ack", help="Acknowledge an incident")
    inc_ack.add_argument("incident_id", help="Incident UUID")
    inc_ack.set_defaults(func=cmd_incidents_ack)

    inc_res = inc_sub.add_parser("resolve", help="Resolve an incident")
    inc_res.add_argument("incident_id", help="Incident UUID")
    inc_res.set_defaults(func=cmd_incidents_resolve)

    # maintenance
    maint_parser = subparsers.add_parser("maintenance", help="Manage maintenance windows")
    maint_sub = maint_parser.add_subparsers(dest="maintenance_command")
    maint_list = maint_sub.add_parser("list", help="List maintenance windows")
    maint_list.add_argument("--page", type=int, default=1)
    maint_list.add_argument("--per-page", type=int, default=50)
    maint_list.set_defaults(func=cmd_maintenance_list)

    maint_end = maint_sub.add_parser("end", help="End an active maintenance window immediately")
    maint_end.add_argument("maintenance_id", help="Maintenance UUID")
    maint_end.set_defaults(func=cmd_maintenance_end)

    # members
    mem_parser = subparsers.add_parser("members", help="View team members")
    mem_sub = mem_parser.add_subparsers(dest="members_command")
    mem_list = mem_sub.add_parser("list", help="List members")
    mem_list.set_defaults(func=cmd_members_list)

    # api-keys
    key_parser = subparsers.add_parser("api-keys", help="View and manage API keys")
    key_sub = key_parser.add_subparsers(dest="keys_command")
    key_list = key_sub.add_parser("list", help="List API keys")
    key_list.set_defaults(func=cmd_api_keys_list)

    return parser


def main() -> None:
    parser = create_parser()
    args = parser.parse_args()
    if not hasattr(args, "func"):
        parser.print_help()
        sys.exit(0)
    try:
        args.func(args)
    except APIError as e:
        sys.stderr.write(f"API Error ({e.code}): {e.message}\n")
        sys.exit(1)
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
