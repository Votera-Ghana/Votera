from datetime import UTC, datetime
from typing import Any
from uuid import UUID

from fastapi import HTTPException, status

from app.schemas.elections import ElectionCreate, ElectionUpdate


def _data(response: Any) -> Any:
    if isinstance(response, dict):
        return response.get("data")
    return getattr(response, "data", None)


class ElectionRepository:
    def __init__(self, database_client: Any) -> None:
        self.database_client = database_client

    def create(self, payload: ElectionCreate, admin_id: str) -> dict[str, Any]:
        row = payload.model_dump(mode="json")
        row["status"] = "DRAFT"
        row["created_by"] = admin_id
        try:
            response = self.database_client.table("elections").insert(row).execute()
        except Exception as error:
            raise database_error() from error

        created = _first(_data(response))
        if not created:
            raise database_error()
        return created

    def list_active(self) -> list[dict[str, Any]]:
        try:
            response = (
                self.database_client.table("elections")
                .select(_election_columns())
                .is_("archived_at", "null")
                .order("created_at", desc=True)
                .execute()
            )
        except Exception as error:
            raise database_error() from error
        return _data(response) or []

    def get(self, election_id: UUID) -> dict[str, Any] | None:
        try:
            response = (
                self.database_client.table("elections")
                .select(_election_columns())
                .eq("id", str(election_id))
                .is_("archived_at", "null")
                .maybe_single()
                .execute()
            )
        except Exception as error:
            raise database_error() from error
        return _data(response)

    def update(self, election_id: UUID, payload: ElectionUpdate) -> dict[str, Any]:
        row = payload.model_dump(mode="json", exclude_unset=True)
        row["updated_at"] = datetime.now(UTC).isoformat()
        try:
            response = (
                self.database_client.table("elections")
                .update(row)
                .eq("id", str(election_id))
                .select(_election_columns())
                .maybe_single()
                .execute()
            )
        except Exception as error:
            raise database_error() from error

        updated = _data(response)
        if not updated:
            raise database_error()
        return updated

    def set_status(self, election_id: UUID, status_value: str) -> dict[str, Any]:
        try:
            response = (
                self.database_client.table("elections")
                .update(
                    {
                        "status": status_value,
                        "updated_at": datetime.now(UTC).isoformat(),
                    }
                )
                .eq("id", str(election_id))
                .select(_election_columns())
                .maybe_single()
                .execute()
            )
        except Exception as error:
            raise database_error() from error

        updated = _data(response)
        if not updated:
            raise database_error()
        return updated

    def archive(self, election_id: UUID) -> None:
        now = datetime.now(UTC).isoformat()
        try:
            (
                self.database_client.table("elections")
                .update({"archived_at": now, "updated_at": now})
                .eq("id", str(election_id))
                .execute()
            )
        except Exception as error:
            raise database_error() from error


def _first(data: Any) -> dict[str, Any] | None:
    if isinstance(data, list):
        return data[0] if data else None
    return data


def _election_columns() -> str:
    return (
        "id, organization_id, name, description, starts_at, ends_at, status, "
        "created_by, created_at, updated_at, archived_at"
    )


def database_error() -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Election data could not be persisted.",
    )
