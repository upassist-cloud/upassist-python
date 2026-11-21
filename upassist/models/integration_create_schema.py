from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.integration_source_enum import IntegrationSourceEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.discord_integration_create_schema import DiscordIntegrationCreateSchema
    from ..models.email_integration_create_schema import EmailIntegrationCreateSchema
    from ..models.teams_integration_create_schema import TeamsIntegrationCreateSchema
    from ..models.telegram_integration_create_schema import TelegramIntegrationCreateSchema
    from ..models.webhook_integration_create_schema import WebhookIntegrationCreateSchema


T = TypeVar("T", bound="IntegrationCreateSchema")


@_attrs_define
class IntegrationCreateSchema:
    """
    Attributes:
        name (str):
        source (IntegrationSourceEnum):
        data (DiscordIntegrationCreateSchema | EmailIntegrationCreateSchema | TeamsIntegrationCreateSchema |
            TelegramIntegrationCreateSchema | WebhookIntegrationCreateSchema):
        is_active (bool | Unset):  Default: True.
    """

    name: str
    source: IntegrationSourceEnum
    data: (
        DiscordIntegrationCreateSchema
        | EmailIntegrationCreateSchema
        | TeamsIntegrationCreateSchema
        | TelegramIntegrationCreateSchema
        | WebhookIntegrationCreateSchema
    )
    is_active: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.discord_integration_create_schema import DiscordIntegrationCreateSchema  # noqa: PLC0415
        from ..models.email_integration_create_schema import EmailIntegrationCreateSchema  # noqa: PLC0415
        from ..models.teams_integration_create_schema import TeamsIntegrationCreateSchema  # noqa: PLC0415
        from ..models.telegram_integration_create_schema import TelegramIntegrationCreateSchema  # noqa: PLC0415

        name = self.name

        source = self.source.value

        data: dict[str, Any]
        if isinstance(self.data, EmailIntegrationCreateSchema):
            data = self.data.to_dict()
        elif isinstance(self.data, TelegramIntegrationCreateSchema):
            data = self.data.to_dict()
        elif isinstance(self.data, DiscordIntegrationCreateSchema):
            data = self.data.to_dict()
        elif isinstance(self.data, TeamsIntegrationCreateSchema):
            data = self.data.to_dict()
        else:
            data = self.data.to_dict()

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "source": source,
                "data": data,
            }
        )
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.discord_integration_create_schema import DiscordIntegrationCreateSchema  # noqa: PLC0415
        from ..models.email_integration_create_schema import EmailIntegrationCreateSchema  # noqa: PLC0415
        from ..models.teams_integration_create_schema import TeamsIntegrationCreateSchema  # noqa: PLC0415
        from ..models.telegram_integration_create_schema import TelegramIntegrationCreateSchema  # noqa: PLC0415
        from ..models.webhook_integration_create_schema import WebhookIntegrationCreateSchema  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        source = IntegrationSourceEnum(d.pop("source"))

        def _parse_data(
            data: object,
        ) -> (
            DiscordIntegrationCreateSchema
            | EmailIntegrationCreateSchema
            | TeamsIntegrationCreateSchema
            | TelegramIntegrationCreateSchema
            | WebhookIntegrationCreateSchema
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = EmailIntegrationCreateSchema.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_1 = TelegramIntegrationCreateSchema.from_dict(data)

                return data_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_2 = DiscordIntegrationCreateSchema.from_dict(data)

                return data_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_3 = TeamsIntegrationCreateSchema.from_dict(data)

                return data_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            data_type_4 = WebhookIntegrationCreateSchema.from_dict(data)

            return data_type_4

        data = _parse_data(d.pop("data"))

        is_active = d.pop("is_active", UNSET)

        integration_create_schema = cls(
            name=name,
            source=source,
            data=data,
            is_active=is_active,
        )

        integration_create_schema.additional_properties = d
        return integration_create_schema

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
