from typing import Sequence
from uuid import UUID

from pydantic import BaseModel, Field, NonNegativeInt, PositiveInt
from pydantic.alias_generators import to_camel


class BaseSchema(BaseModel):
    class Config:
        str_strip_whitespace = True


class CamelCaseSchemaSchema(BaseModel):
    class Config:
        populate_by_name = True
        alias_generator = to_camel
        str_strip_whitespace = True


class IDSchema(BaseSchema):
    id: int


class UUIDSchema(BaseSchema):
    id: UUID


class BasePaginatedSchema(BaseSchema):
    data: Sequence[BaseSchema] = Field(description="List of data")
    per_page: PositiveInt = Field(default=50, description="Count of data per page")
    pages_count: NonNegativeInt = Field(description="Count of pages")
    count: NonNegativeInt = Field(description="Count of data rows by given parameters")
    total_count: NonNegativeInt = Field(description="Count of all data rows")
    page: PositiveInt = Field(default=1, description="Current page number")
    next_page: PositiveInt | None = Field(
        default=None, description="Next page number, nullable if not exists."
    )
    prev_page: PositiveInt | None = Field(
        default=None, description="Previous page number, nullable if not exists."
    )


class DetailResponse(BaseSchema):
    detail: str | None = None
