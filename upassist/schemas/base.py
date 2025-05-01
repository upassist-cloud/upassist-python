from collections.abc import Sequence
from uuid import UUID

from pydantic import BaseModel, Field, NonNegativeInt, PositiveInt
from pydantic.alias_generators import to_camel


class BaseSchema(BaseModel):
    """Base schema class that provides common configuration for all schemas.

    This class sets up basic Pydantic model configuration like whitespace stripping.
    """

    class Config:
        str_strip_whitespace = True


class CamelCaseSchemaSchema(BaseModel):
    """Schema class that converts field names to camelCase for JSON serialization.

    This class is used when the API expects camelCase field names in JSON responses.
    """

    class Config:
        populate_by_name = True
        alias_generator = to_camel
        str_strip_whitespace = True


class IDSchema(BaseSchema):
    """Base schema for models that use integer IDs.

    Attributes:
        id: Integer identifier
    """

    id: int


class UUIDSchema(BaseSchema):
    """Base schema for models that use UUID identifiers.

    Attributes:
        id: UUID identifier
    """

    id: UUID


class BasePaginatedSchema(BaseSchema):
    """Base schema for paginated responses.

    Attributes:
        data: List of data items
        per_page: Number of items per page
        pages_count: Total number of pages
        count: Number of items in current page
        total_count: Total number of items across all pages
        page: Current page number
        next_page: Next page number (None if on last page)
        prev_page: Previous page number (None if on first page)
    """

    data: Sequence[BaseSchema] = Field(description="List of data")
    per_page: PositiveInt = Field(default=50, description="Count of data per page")
    pages_count: NonNegativeInt = Field(description="Count of pages")
    count: NonNegativeInt = Field(description="Count of data rows by given parameters")
    total_count: NonNegativeInt = Field(description="Count of all data rows")
    page: PositiveInt = Field(default=1, description="Current page number")
    next_page: PositiveInt | None = Field(default=None, description="Next page number, nullable if not exists.")
    prev_page: PositiveInt | None = Field(default=None, description="Previous page number, nullable if not exists.")


class DetailResponse(BaseSchema):
    """Schema for simple detail responses.

    Attributes:
        detail: Optional detail message
    """

    detail: str | None = None
