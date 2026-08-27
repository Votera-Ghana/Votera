from typing import Any
from uuid import UUID

from fastapi import HTTPException, status

from app.auth import ADMIN_ROLES, AdminIdentity
from app.repositories.elections import ElectionRepository
from app.schemas.elections import (
    ElectionCreate,
    ElectionResponse,
    ElectionStatus,
    ElectionUpdate,
)


class ElectionService:
    def __init__(self, repository: ElectionRepository) -> None:
        self.repository = repository

    def create(self, payload: ElectionCreate, admin: AdminIdentity) -> ElectionResponse:
        require_admin(admin)
        return ElectionResponse.model_validate(self.repository.create(payload, admin.id))

    def list(self, admin: AdminIdentity) -> list[ElectionResponse]:
        require_admin(admin)
        return [
            ElectionResponse.model_validate(row) for row in self.repository.list_active()
        ]

    def get(self, election_id: UUID, admin: AdminIdentity) -> ElectionResponse:
        require_admin(admin)
        return ElectionResponse.model_validate(self._get_existing(election_id))

    def update(
        self, election_id: UUID, payload: ElectionUpdate, admin: AdminIdentity
    ) -> ElectionResponse:
        require_admin(admin)
        if not payload.model_fields_set:
            raise business_error("No election fields provided for update.")
        current = self._get_existing(election_id)
        if current.get("status") != ElectionStatus.DRAFT:
            raise business_error("Only DRAFT elections can be updated.")

        merged = {**current, **payload.model_dump(mode="json", exclude_unset=True)}
        self._validate_election_complete(merged)
        return ElectionResponse.model_validate(self.repository.update(election_id, payload))

    def archive(self, election_id: UUID, admin: AdminIdentity) -> None:
        require_admin(admin)
        current = self._get_existing(election_id)
        if current.get("status") != ElectionStatus.DRAFT:
            raise business_error("Only DRAFT elections can be archived.")
        self.repository.archive(election_id)

    def open(self, election_id: UUID, admin: AdminIdentity) -> ElectionResponse:
        require_admin(admin)
        current = self._get_existing(election_id)
        if current.get("status") != ElectionStatus.DRAFT:
            raise business_error(
                "Election must be in DRAFT status before it can be opened."
            )
        self._validate_election_complete(current)
        return ElectionResponse.model_validate(
            self.repository.set_status(election_id, ElectionStatus.OPEN)
        )

    def close(self, election_id: UUID, admin: AdminIdentity) -> ElectionResponse:
        require_admin(admin)
        current = self._get_existing(election_id)
        if current.get("status") != ElectionStatus.OPEN:
            raise business_error(
                "Election must be in OPEN status before it can be closed."
            )
        return ElectionResponse.model_validate(
            self.repository.set_status(election_id, ElectionStatus.CLOSED)
        )

    def _get_existing(self, election_id: UUID) -> dict[str, Any]:
        election = self.repository.get(election_id)
        if election is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Election not found.",
            )
        return election

    def _validate_election_complete(self, election: dict[str, Any]) -> None:
        required = ("organization_id", "name", "description", "starts_at", "ends_at")
        for field_name in required:
            value = election.get(field_name)
            if value is None or (isinstance(value, str) and not value.strip()):
                raise business_error("Election information is incomplete.")

        parsed = ElectionResponse.model_validate(election)
        if parsed.ends_at <= parsed.starts_at:
            raise business_error("Election end time must occur after start time.")


def require_admin(admin: AdminIdentity) -> None:
    if admin.role not in ADMIN_ROLES:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only administrators can perform this operation.",
        )


def business_error(detail: str) -> HTTPException:
    return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)
