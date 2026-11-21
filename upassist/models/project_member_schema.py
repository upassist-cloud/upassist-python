from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.project_member_role_enum import ProjectMemberRoleEnum

if TYPE_CHECKING:
    from ..models.user_schema import UserSchema


T = TypeVar("T", bound="ProjectMemberSchema")


@_attrs_define
class ProjectMemberSchema:
    """
    Attributes:
        id (UUID):
        role (ProjectMemberRoleEnum):
        user (UserSchema):
    """

    id: UUID
    role: ProjectMemberRoleEnum
    user: UserSchema
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        role = self.role.value

        user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "role": role,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_schema import UserSchema  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        role = ProjectMemberRoleEnum(d.pop("role"))

        user = UserSchema.from_dict(d.pop("user"))

        project_member_schema = cls(
            id=id,
            role=role,
            user=user,
        )

        project_member_schema.additional_properties = d
        return project_member_schema

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
