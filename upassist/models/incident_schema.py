from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_content_type_enum import IncidentContentTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.incident_schema_meta_type_0 import IncidentSchemaMetaType0


T = TypeVar("T", bound="IncidentSchema")


@_attrs_define
class IncidentSchema:
    """
    Attributes:
        id (UUID):
        name (str):
        cause (str):
        content_type (IncidentContentTypeEnum):
        started_at (datetime.datetime):
        is_ongoing (bool):
        is_finished (bool):
        is_acknowledged (bool):
        finished_at (datetime.datetime | None | Unset):
        meta (IncidentSchemaMetaType0 | None | Unset):
        comments_count (int | None | Unset):
        acknowledged_at (datetime.datetime | None | Unset):
        acknowledged_by_id (None | Unset | UUID):
        resolved_by_id (None | Unset | UUID):
        group_id (None | Unset | UUID):
    """

    id: UUID
    name: str
    cause: str
    content_type: IncidentContentTypeEnum
    started_at: datetime.datetime
    is_ongoing: bool
    is_finished: bool
    is_acknowledged: bool
    finished_at: datetime.datetime | None | Unset = UNSET
    meta: IncidentSchemaMetaType0 | None | Unset = UNSET
    comments_count: int | None | Unset = UNSET
    acknowledged_at: datetime.datetime | None | Unset = UNSET
    acknowledged_by_id: None | Unset | UUID = UNSET
    resolved_by_id: None | Unset | UUID = UNSET
    group_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.incident_schema_meta_type_0 import IncidentSchemaMetaType0  # noqa: PLC0415

        id = str(self.id)

        name = self.name

        cause = self.cause

        content_type = self.content_type.value

        started_at = self.started_at.isoformat()

        is_ongoing = self.is_ongoing

        is_finished = self.is_finished

        is_acknowledged = self.is_acknowledged

        finished_at: None | str | Unset
        if isinstance(self.finished_at, Unset):
            finished_at = UNSET
        elif isinstance(self.finished_at, datetime.datetime):
            finished_at = self.finished_at.isoformat()
        else:
            finished_at = self.finished_at

        meta: dict[str, Any] | None | Unset
        if isinstance(self.meta, Unset):
            meta = UNSET
        elif isinstance(self.meta, IncidentSchemaMetaType0):
            meta = self.meta.to_dict()
        else:
            meta = self.meta

        comments_count: int | None | Unset
        if isinstance(self.comments_count, Unset):
            comments_count = UNSET
        else:
            comments_count = self.comments_count

        acknowledged_at: None | str | Unset
        if isinstance(self.acknowledged_at, Unset):
            acknowledged_at = UNSET
        elif isinstance(self.acknowledged_at, datetime.datetime):
            acknowledged_at = self.acknowledged_at.isoformat()
        else:
            acknowledged_at = self.acknowledged_at

        acknowledged_by_id: None | str | Unset
        if isinstance(self.acknowledged_by_id, Unset):
            acknowledged_by_id = UNSET
        elif isinstance(self.acknowledged_by_id, UUID):
            acknowledged_by_id = str(self.acknowledged_by_id)
        else:
            acknowledged_by_id = self.acknowledged_by_id

        resolved_by_id: None | str | Unset
        if isinstance(self.resolved_by_id, Unset):
            resolved_by_id = UNSET
        elif isinstance(self.resolved_by_id, UUID):
            resolved_by_id = str(self.resolved_by_id)
        else:
            resolved_by_id = self.resolved_by_id

        group_id: None | str | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        elif isinstance(self.group_id, UUID):
            group_id = str(self.group_id)
        else:
            group_id = self.group_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "cause": cause,
                "content_type": content_type,
                "started_at": started_at,
                "is_ongoing": is_ongoing,
                "is_finished": is_finished,
                "is_acknowledged": is_acknowledged,
            }
        )
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at
        if meta is not UNSET:
            field_dict["meta"] = meta
        if comments_count is not UNSET:
            field_dict["comments_count"] = comments_count
        if acknowledged_at is not UNSET:
            field_dict["acknowledged_at"] = acknowledged_at
        if acknowledged_by_id is not UNSET:
            field_dict["acknowledged_by_id"] = acknowledged_by_id
        if resolved_by_id is not UNSET:
            field_dict["resolved_by_id"] = resolved_by_id
        if group_id is not UNSET:
            field_dict["group_id"] = group_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.incident_schema_meta_type_0 import IncidentSchemaMetaType0  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        cause = d.pop("cause")

        content_type = IncidentContentTypeEnum(d.pop("content_type"))

        started_at = datetime.datetime.fromisoformat(d.pop("started_at"))

        is_ongoing = d.pop("is_ongoing")

        is_finished = d.pop("is_finished")

        is_acknowledged = d.pop("is_acknowledged")

        def _parse_finished_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                finished_at_type_0 = datetime.datetime.fromisoformat(data)

                return finished_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        finished_at = _parse_finished_at(d.pop("finished_at", UNSET))

        def _parse_meta(data: object) -> IncidentSchemaMetaType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = IncidentSchemaMetaType0.from_dict(data)

                return meta_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IncidentSchemaMetaType0 | None | Unset, data)

        meta = _parse_meta(d.pop("meta", UNSET))

        def _parse_comments_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        comments_count = _parse_comments_count(d.pop("comments_count", UNSET))

        def _parse_acknowledged_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                acknowledged_at_type_0 = datetime.datetime.fromisoformat(data)

                return acknowledged_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        acknowledged_at = _parse_acknowledged_at(d.pop("acknowledged_at", UNSET))

        def _parse_acknowledged_by_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                acknowledged_by_id_type_0 = UUID(data)

                return acknowledged_by_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        acknowledged_by_id = _parse_acknowledged_by_id(d.pop("acknowledged_by_id", UNSET))

        def _parse_resolved_by_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resolved_by_id_type_0 = UUID(data)

                return resolved_by_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        resolved_by_id = _parse_resolved_by_id(d.pop("resolved_by_id", UNSET))

        def _parse_group_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                group_id_type_0 = UUID(data)

                return group_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        group_id = _parse_group_id(d.pop("group_id", UNSET))

        incident_schema = cls(
            id=id,
            name=name,
            cause=cause,
            content_type=content_type,
            started_at=started_at,
            is_ongoing=is_ongoing,
            is_finished=is_finished,
            is_acknowledged=is_acknowledged,
            finished_at=finished_at,
            meta=meta,
            comments_count=comments_count,
            acknowledged_at=acknowledged_at,
            acknowledged_by_id=acknowledged_by_id,
            resolved_by_id=resolved_by_id,
            group_id=group_id,
        )

        incident_schema.additional_properties = d
        return incident_schema

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
