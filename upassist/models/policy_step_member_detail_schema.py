from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.escalation_type_enum import EscalationTypeEnum

if TYPE_CHECKING:
    from ..models.integration_schema import IntegrationSchema
    from ..models.project_member_base_schema import ProjectMemberBaseSchema


T = TypeVar("T", bound="PolicyStepMemberDetailSchema")


@_attrs_define
class PolicyStepMemberDetailSchema:
    """
    Attributes:
        id (UUID):
        type_ (EscalationTypeEnum):
        integrations (list[IntegrationSchema]):
        project_members (list[ProjectMemberBaseSchema]):
    """

    id: UUID
    type_: EscalationTypeEnum
    integrations: list[IntegrationSchema]
    project_members: list[ProjectMemberBaseSchema]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        type_ = self.type_.value

        integrations = []
        for integrations_item_data in self.integrations:
            integrations_item = integrations_item_data.to_dict()
            integrations.append(integrations_item)

        project_members = []
        for project_members_item_data in self.project_members:
            project_members_item = project_members_item_data.to_dict()
            project_members.append(project_members_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "integrations": integrations,
                "project_members": project_members,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integration_schema import IntegrationSchema  # noqa: PLC0415
        from ..models.project_member_base_schema import ProjectMemberBaseSchema  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        type_ = EscalationTypeEnum(d.pop("type"))

        integrations = []
        _integrations = d.pop("integrations")
        for integrations_item_data in _integrations:
            integrations_item = IntegrationSchema.from_dict(integrations_item_data)

            integrations.append(integrations_item)

        project_members = []
        _project_members = d.pop("project_members")
        for project_members_item_data in _project_members:
            project_members_item = ProjectMemberBaseSchema.from_dict(project_members_item_data)

            project_members.append(project_members_item)

        policy_step_member_detail_schema = cls(
            id=id,
            type_=type_,
            integrations=integrations,
            project_members=project_members,
        )

        policy_step_member_detail_schema.additional_properties = d
        return policy_step_member_detail_schema

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
