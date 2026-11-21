from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TelegramIntegrationCreateSchema")


@_attrs_define
class TelegramIntegrationCreateSchema:
    """
    Attributes:
        chat_id (int):
        message_thread_id (int | None | Unset):
    """

    chat_id: int
    message_thread_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat_id = self.chat_id

        message_thread_id: int | None | Unset
        if isinstance(self.message_thread_id, Unset):
            message_thread_id = UNSET
        else:
            message_thread_id = self.message_thread_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chat_id": chat_id,
            }
        )
        if message_thread_id is not UNSET:
            field_dict["message_thread_id"] = message_thread_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chat_id = d.pop("chat_id")

        def _parse_message_thread_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        message_thread_id = _parse_message_thread_id(d.pop("message_thread_id", UNSET))

        telegram_integration_create_schema = cls(
            chat_id=chat_id,
            message_thread_id=message_thread_id,
        )

        telegram_integration_create_schema.additional_properties = d
        return telegram_integration_create_schema

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
