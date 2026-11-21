from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.policy_step_detail_schema import PolicyStepDetailSchema


T = TypeVar("T", bound="PolicyDetailSchema")


@_attrs_define
class PolicyDetailSchema:
    """
    Attributes:
        id (UUID):
        name (str):
        steps (list[PolicyStepDetailSchema]):
    """

    id: UUID
    name: str
    steps: list[PolicyStepDetailSchema]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "steps": steps,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.policy_step_detail_schema import PolicyStepDetailSchema  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = PolicyStepDetailSchema.from_dict(steps_item_data)

            steps.append(steps_item)

        policy_detail_schema = cls(
            id=id,
            name=name,
            steps=steps,
        )

        policy_detail_schema.additional_properties = d
        return policy_detail_schema

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
