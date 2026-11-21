from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_preset_schema import DashboardPresetSchema
    from ..models.dashboard_section_list_schema import DashboardSectionListSchema
    from ..models.dashboard_variable_schema import DashboardVariableSchema
    from ..models.source_schema import SourceSchema


T = TypeVar("T", bound="DashboardDetailSchema")


@_attrs_define
class DashboardDetailSchema:
    """
    Attributes:
        id (UUID):
        name (str):
        fetch_interval (int):
        source (SourceSchema):
        sections (list[DashboardSectionListSchema]):
        variables (list[DashboardVariableSchema]):
        group_id (None | Unset | UUID):
        date_from (None | str | Unset):  Default: 'now-24h'.
        date_to (None | str | Unset):  Default: 'now'.
        presets (list[DashboardPresetSchema] | None | Unset):
    """

    id: UUID
    name: str
    fetch_interval: int
    source: SourceSchema
    sections: list[DashboardSectionListSchema]
    variables: list[DashboardVariableSchema]
    group_id: None | Unset | UUID = UNSET
    date_from: None | str | Unset = "now-24h"
    date_to: None | str | Unset = "now"
    presets: list[DashboardPresetSchema] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        fetch_interval = self.fetch_interval

        source = self.source.to_dict()

        sections = []
        for sections_item_data in self.sections:
            sections_item = sections_item_data.to_dict()
            sections.append(sections_item)

        variables = []
        for variables_item_data in self.variables:
            variables_item = variables_item_data.to_dict()
            variables.append(variables_item)

        group_id: None | str | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        elif isinstance(self.group_id, UUID):
            group_id = str(self.group_id)
        else:
            group_id = self.group_id

        date_from: None | str | Unset
        if isinstance(self.date_from, Unset):
            date_from = UNSET
        else:
            date_from = self.date_from

        date_to: None | str | Unset
        if isinstance(self.date_to, Unset):
            date_to = UNSET
        else:
            date_to = self.date_to

        presets: list[dict[str, Any]] | None | Unset
        if isinstance(self.presets, Unset):
            presets = UNSET
        elif isinstance(self.presets, list):
            presets = []
            for presets_type_0_item_data in self.presets:
                presets_type_0_item = presets_type_0_item_data.to_dict()
                presets.append(presets_type_0_item)

        else:
            presets = self.presets

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "fetch_interval": fetch_interval,
                "source": source,
                "sections": sections,
                "variables": variables,
            }
        )
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if date_from is not UNSET:
            field_dict["date_from"] = date_from
        if date_to is not UNSET:
            field_dict["date_to"] = date_to
        if presets is not UNSET:
            field_dict["presets"] = presets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_preset_schema import DashboardPresetSchema  # noqa: PLC0415
        from ..models.dashboard_section_list_schema import DashboardSectionListSchema  # noqa: PLC0415
        from ..models.dashboard_variable_schema import DashboardVariableSchema  # noqa: PLC0415
        from ..models.source_schema import SourceSchema  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        fetch_interval = d.pop("fetch_interval")

        source = SourceSchema.from_dict(d.pop("source"))

        sections = []
        _sections = d.pop("sections")
        for sections_item_data in _sections:
            sections_item = DashboardSectionListSchema.from_dict(sections_item_data)

            sections.append(sections_item)

        variables = []
        _variables = d.pop("variables")
        for variables_item_data in _variables:
            variables_item = DashboardVariableSchema.from_dict(variables_item_data)

            variables.append(variables_item)

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

        def _parse_date_from(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_from = _parse_date_from(d.pop("date_from", UNSET))

        def _parse_date_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_to = _parse_date_to(d.pop("date_to", UNSET))

        def _parse_presets(data: object) -> list[DashboardPresetSchema] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                presets_type_0 = []
                _presets_type_0 = data
                for presets_type_0_item_data in _presets_type_0:
                    presets_type_0_item = DashboardPresetSchema.from_dict(presets_type_0_item_data)

                    presets_type_0.append(presets_type_0_item)

                return presets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DashboardPresetSchema] | None | Unset, data)

        presets = _parse_presets(d.pop("presets", UNSET))

        dashboard_detail_schema = cls(
            id=id,
            name=name,
            fetch_interval=fetch_interval,
            source=source,
            sections=sections,
            variables=variables,
            group_id=group_id,
            date_from=date_from,
            date_to=date_to,
            presets=presets,
        )

        dashboard_detail_schema.additional_properties = d
        return dashboard_detail_schema

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
