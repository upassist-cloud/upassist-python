from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_variable_create_schema import DashboardVariableCreateSchema


T = TypeVar("T", bound="DashboardCreateSchema")


@_attrs_define
class DashboardCreateSchema:
    """
    Attributes:
        name (str):
        source_id (UUID):
        date_from (None | str | Unset):  Default: 'now-24h'.
        date_to (None | str | Unset):  Default: 'now'.
        group_id (None | Unset | UUID):
        fetch_interval (int | Unset):  Default: 30.
        dashboard_template_id (None | Unset | UUID):
        variables (list[DashboardVariableCreateSchema] | None | Unset):
    """

    name: str
    source_id: UUID
    date_from: None | str | Unset = "now-24h"
    date_to: None | str | Unset = "now"
    group_id: None | Unset | UUID = UNSET
    fetch_interval: int | Unset = 30
    dashboard_template_id: None | Unset | UUID = UNSET
    variables: list[DashboardVariableCreateSchema] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        source_id = str(self.source_id)

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

        group_id: None | str | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        elif isinstance(self.group_id, UUID):
            group_id = str(self.group_id)
        else:
            group_id = self.group_id

        fetch_interval = self.fetch_interval

        dashboard_template_id: None | str | Unset
        if isinstance(self.dashboard_template_id, Unset):
            dashboard_template_id = UNSET
        elif isinstance(self.dashboard_template_id, UUID):
            dashboard_template_id = str(self.dashboard_template_id)
        else:
            dashboard_template_id = self.dashboard_template_id

        variables: list[dict[str, Any]] | None | Unset
        if isinstance(self.variables, Unset):
            variables = UNSET
        elif isinstance(self.variables, list):
            variables = []
            for variables_type_0_item_data in self.variables:
                variables_type_0_item = variables_type_0_item_data.to_dict()
                variables.append(variables_type_0_item)

        else:
            variables = self.variables

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "source_id": source_id,
            }
        )
        if date_from is not UNSET:
            field_dict["date_from"] = date_from
        if date_to is not UNSET:
            field_dict["date_to"] = date_to
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if fetch_interval is not UNSET:
            field_dict["fetch_interval"] = fetch_interval
        if dashboard_template_id is not UNSET:
            field_dict["dashboard_template_id"] = dashboard_template_id
        if variables is not UNSET:
            field_dict["variables"] = variables

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_variable_create_schema import DashboardVariableCreateSchema  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        source_id = UUID(d.pop("source_id"))

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

        fetch_interval = d.pop("fetch_interval", UNSET)

        def _parse_dashboard_template_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dashboard_template_id_type_0 = UUID(data)

                return dashboard_template_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        dashboard_template_id = _parse_dashboard_template_id(d.pop("dashboard_template_id", UNSET))

        def _parse_variables(data: object) -> list[DashboardVariableCreateSchema] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                variables_type_0 = []
                _variables_type_0 = data
                for variables_type_0_item_data in _variables_type_0:
                    variables_type_0_item = DashboardVariableCreateSchema.from_dict(variables_type_0_item_data)

                    variables_type_0.append(variables_type_0_item)

                return variables_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DashboardVariableCreateSchema] | None | Unset, data)

        variables = _parse_variables(d.pop("variables", UNSET))

        dashboard_create_schema = cls(
            name=name,
            source_id=source_id,
            date_from=date_from,
            date_to=date_to,
            group_id=group_id,
            fetch_interval=fetch_interval,
            dashboard_template_id=dashboard_template_id,
            variables=variables,
        )

        dashboard_create_schema.additional_properties = d
        return dashboard_create_schema

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
