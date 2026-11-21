from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ErrorIssueDetailSchema")


@_attrs_define
class ErrorIssueDetailSchema:
    """
    Attributes:
        id (UUID):
        error_app_id (UUID):
        digest_order (int):
        calculated_type (str):
        calculated_value (str):
        first_seen_at (datetime.datetime):
        last_seen_at (datetime.datetime):
        occurrences_count (int):
        is_resolved (bool):
        is_muted (bool):
        short_id (str):
        title (str):
        transaction (None | str | Unset):
        last_frame_filename (None | str | Unset):
        last_frame_module (None | str | Unset):
        last_frame_function (None | str | Unset):
        error_app_name (None | str | Unset):
        comments_count (int | Unset):  Default: 0.
        users_count (int | Unset):  Default: 0.
        environment (None | str | Unset):
        timeline (list[list[datetime.datetime | int]] | None | Unset):
        grouping_key (None | str | Unset):
    """

    id: UUID
    error_app_id: UUID
    digest_order: int
    calculated_type: str
    calculated_value: str
    first_seen_at: datetime.datetime
    last_seen_at: datetime.datetime
    occurrences_count: int
    is_resolved: bool
    is_muted: bool
    short_id: str
    title: str
    transaction: None | str | Unset = UNSET
    last_frame_filename: None | str | Unset = UNSET
    last_frame_module: None | str | Unset = UNSET
    last_frame_function: None | str | Unset = UNSET
    error_app_name: None | str | Unset = UNSET
    comments_count: int | Unset = 0
    users_count: int | Unset = 0
    environment: None | str | Unset = UNSET
    timeline: list[list[datetime.datetime | int]] | None | Unset = UNSET
    grouping_key: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        error_app_id = str(self.error_app_id)

        digest_order = self.digest_order

        calculated_type = self.calculated_type

        calculated_value = self.calculated_value

        first_seen_at = self.first_seen_at.isoformat()

        last_seen_at = self.last_seen_at.isoformat()

        occurrences_count = self.occurrences_count

        is_resolved = self.is_resolved

        is_muted = self.is_muted

        short_id = self.short_id

        title = self.title

        transaction: None | str | Unset
        if isinstance(self.transaction, Unset):
            transaction = UNSET
        else:
            transaction = self.transaction

        last_frame_filename: None | str | Unset
        if isinstance(self.last_frame_filename, Unset):
            last_frame_filename = UNSET
        else:
            last_frame_filename = self.last_frame_filename

        last_frame_module: None | str | Unset
        if isinstance(self.last_frame_module, Unset):
            last_frame_module = UNSET
        else:
            last_frame_module = self.last_frame_module

        last_frame_function: None | str | Unset
        if isinstance(self.last_frame_function, Unset):
            last_frame_function = UNSET
        else:
            last_frame_function = self.last_frame_function

        error_app_name: None | str | Unset
        if isinstance(self.error_app_name, Unset):
            error_app_name = UNSET
        else:
            error_app_name = self.error_app_name

        comments_count = self.comments_count

        users_count = self.users_count

        environment: None | str | Unset
        if isinstance(self.environment, Unset):
            environment = UNSET
        else:
            environment = self.environment

        timeline: list[list[int | str]] | None | Unset
        if isinstance(self.timeline, Unset):
            timeline = UNSET
        elif isinstance(self.timeline, list):
            timeline = []
            for timeline_type_0_item_data in self.timeline:
                timeline_type_0_item = []
                for timeline_type_0_item_item_data in timeline_type_0_item_data:
                    timeline_type_0_item_item: int | str
                    if isinstance(timeline_type_0_item_item_data, datetime.datetime):
                        timeline_type_0_item_item = timeline_type_0_item_item_data.isoformat()
                    else:
                        timeline_type_0_item_item = timeline_type_0_item_item_data
                    timeline_type_0_item.append(timeline_type_0_item_item)

                timeline.append(timeline_type_0_item)

        else:
            timeline = self.timeline

        grouping_key: None | str | Unset
        if isinstance(self.grouping_key, Unset):
            grouping_key = UNSET
        else:
            grouping_key = self.grouping_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "error_app_id": error_app_id,
                "digest_order": digest_order,
                "calculated_type": calculated_type,
                "calculated_value": calculated_value,
                "first_seen_at": first_seen_at,
                "last_seen_at": last_seen_at,
                "occurrences_count": occurrences_count,
                "is_resolved": is_resolved,
                "is_muted": is_muted,
                "short_id": short_id,
                "title": title,
            }
        )
        if transaction is not UNSET:
            field_dict["transaction"] = transaction
        if last_frame_filename is not UNSET:
            field_dict["last_frame_filename"] = last_frame_filename
        if last_frame_module is not UNSET:
            field_dict["last_frame_module"] = last_frame_module
        if last_frame_function is not UNSET:
            field_dict["last_frame_function"] = last_frame_function
        if error_app_name is not UNSET:
            field_dict["error_app_name"] = error_app_name
        if comments_count is not UNSET:
            field_dict["comments_count"] = comments_count
        if users_count is not UNSET:
            field_dict["users_count"] = users_count
        if environment is not UNSET:
            field_dict["environment"] = environment
        if timeline is not UNSET:
            field_dict["timeline"] = timeline
        if grouping_key is not UNSET:
            field_dict["grouping_key"] = grouping_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        error_app_id = UUID(d.pop("error_app_id"))

        digest_order = d.pop("digest_order")

        calculated_type = d.pop("calculated_type")

        calculated_value = d.pop("calculated_value")

        first_seen_at = datetime.datetime.fromisoformat(d.pop("first_seen_at"))

        last_seen_at = datetime.datetime.fromisoformat(d.pop("last_seen_at"))

        occurrences_count = d.pop("occurrences_count")

        is_resolved = d.pop("is_resolved")

        is_muted = d.pop("is_muted")

        short_id = d.pop("short_id")

        title = d.pop("title")

        def _parse_transaction(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        transaction = _parse_transaction(d.pop("transaction", UNSET))

        def _parse_last_frame_filename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_frame_filename = _parse_last_frame_filename(d.pop("last_frame_filename", UNSET))

        def _parse_last_frame_module(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_frame_module = _parse_last_frame_module(d.pop("last_frame_module", UNSET))

        def _parse_last_frame_function(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_frame_function = _parse_last_frame_function(d.pop("last_frame_function", UNSET))

        def _parse_error_app_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_app_name = _parse_error_app_name(d.pop("error_app_name", UNSET))

        comments_count = d.pop("comments_count", UNSET)

        users_count = d.pop("users_count", UNSET)

        def _parse_environment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        environment = _parse_environment(d.pop("environment", UNSET))

        def _parse_timeline(data: object) -> list[list[datetime.datetime | int]] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                timeline_type_0 = []
                _timeline_type_0 = data
                for timeline_type_0_item_data in _timeline_type_0:
                    timeline_type_0_item = []
                    _timeline_type_0_item = timeline_type_0_item_data
                    for timeline_type_0_item_item_data in _timeline_type_0_item:

                        def _parse_timeline_type_0_item_item(data: object) -> datetime.datetime | int:
                            try:
                                if not isinstance(data, str):
                                    raise TypeError()
                                timeline_type_0_item_item_type_0 = datetime.datetime.fromisoformat(data)

                                return timeline_type_0_item_item_type_0
                            except (TypeError, ValueError, AttributeError, KeyError):
                                pass
                            return cast(datetime.datetime | int, data)

                        timeline_type_0_item_item = _parse_timeline_type_0_item_item(timeline_type_0_item_item_data)

                        timeline_type_0_item.append(timeline_type_0_item_item)

                    timeline_type_0.append(timeline_type_0_item)

                return timeline_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[list[datetime.datetime | int]] | None | Unset, data)

        timeline = _parse_timeline(d.pop("timeline", UNSET))

        def _parse_grouping_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        grouping_key = _parse_grouping_key(d.pop("grouping_key", UNSET))

        error_issue_detail_schema = cls(
            id=id,
            error_app_id=error_app_id,
            digest_order=digest_order,
            calculated_type=calculated_type,
            calculated_value=calculated_value,
            first_seen_at=first_seen_at,
            last_seen_at=last_seen_at,
            occurrences_count=occurrences_count,
            is_resolved=is_resolved,
            is_muted=is_muted,
            short_id=short_id,
            title=title,
            transaction=transaction,
            last_frame_filename=last_frame_filename,
            last_frame_module=last_frame_module,
            last_frame_function=last_frame_function,
            error_app_name=error_app_name,
            comments_count=comments_count,
            users_count=users_count,
            environment=environment,
            timeline=timeline,
            grouping_key=grouping_key,
        )

        error_issue_detail_schema.additional_properties = d
        return error_issue_detail_schema

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
