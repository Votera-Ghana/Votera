from datetime import datetime
from enum import StrEnum
from typing import Self
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


class ElectionStatus(StrEnum):
    DRAFT = "DRAFT"
    OPEN = "OPEN"
    CLOSED = "CLOSED"


class ElectionCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    organization_id: UUID
    name: str = Field(min_length=1, max_length=200)
    description: str = Field(min_length=1, max_length=5000)
    starts_at: datetime
    ends_at: datetime

    @field_validator("name", "description")
    @classmethod
    def reject_blank_text(cls, value: str) -> str:
        stripped = value.strip()
        if not stripped:
            raise ValueError("Field must not be empty.")
        return stripped

    @model_validator(mode="after")
    def validate_dates(self) -> Self:
        if self.ends_at <= self.starts_at:
            raise ValueError("Election end time must occur after start time.")
        return self


class ElectionUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str | None = Field(default=None, min_length=1, max_length=200)
    description: str | None = Field(default=None, min_length=1, max_length=5000)
    starts_at: datetime | None = None
    ends_at: datetime | None = None

    @field_validator("name", "description")
    @classmethod
    def reject_blank_text(cls, value: str | None) -> str | None:
        if value is None:
            return value
        stripped = value.strip()
        if not stripped:
            raise ValueError("Field must not be empty.")
        return stripped

    @model_validator(mode="after")
    def validate_dates(self) -> Self:
        if self.starts_at is not None and self.ends_at is not None:
            if self.ends_at <= self.starts_at:
                raise ValueError("Election end time must occur after start time.")
        return self


class ElectionResponse(BaseModel):
    id: UUID
    organization_id: UUID
    name: str
    description: str
    starts_at: datetime
    ends_at: datetime
    status: ElectionStatus
    created_by: UUID
    created_at: datetime | None = None
    updated_at: datetime | None = None
    archived_at: datetime | None = None
