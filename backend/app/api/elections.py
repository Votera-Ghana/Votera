from uuid import UUID

from fastapi import APIRouter, Depends, Response, status

from app.auth import AdminIdentity, get_current_admin
from app.core.supabase import supabase
from app.repositories.elections import ElectionRepository
from app.schemas.elections import ElectionCreate, ElectionResponse, ElectionUpdate
from app.services.elections import ElectionService

router = APIRouter(prefix="/api/elections", tags=["elections"])


def get_election_service() -> ElectionService:
    return ElectionService(ElectionRepository(supabase))


@router.post(
    "",
    response_model=ElectionResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_election(
    payload: ElectionCreate,
    admin: AdminIdentity = Depends(get_current_admin),
    service: ElectionService = Depends(get_election_service),
) -> ElectionResponse:
    return service.create(payload, admin)


@router.get("", response_model=list[ElectionResponse])
def list_elections(
    admin: AdminIdentity = Depends(get_current_admin),
    service: ElectionService = Depends(get_election_service),
) -> list[ElectionResponse]:
    return service.list(admin)


@router.get("/{election_id}", response_model=ElectionResponse)
def get_election(
    election_id: UUID,
    admin: AdminIdentity = Depends(get_current_admin),
    service: ElectionService = Depends(get_election_service),
) -> ElectionResponse:
    return service.get(election_id, admin)


@router.patch("/{election_id}", response_model=ElectionResponse)
def update_election(
    election_id: UUID,
    payload: ElectionUpdate,
    admin: AdminIdentity = Depends(get_current_admin),
    service: ElectionService = Depends(get_election_service),
) -> ElectionResponse:
    return service.update(election_id, payload, admin)


@router.delete("/{election_id}", status_code=status.HTTP_204_NO_CONTENT)
def archive_election(
    election_id: UUID,
    admin: AdminIdentity = Depends(get_current_admin),
    service: ElectionService = Depends(get_election_service),
) -> Response:
    service.archive(election_id, admin)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post("/{election_id}/open", response_model=ElectionResponse)
def open_election(
    election_id: UUID,
    admin: AdminIdentity = Depends(get_current_admin),
    service: ElectionService = Depends(get_election_service),
) -> ElectionResponse:
    return service.open(election_id, admin)


@router.post("/{election_id}/close", response_model=ElectionResponse)
def close_election(
    election_id: UUID,
    admin: AdminIdentity = Depends(get_current_admin),
    service: ElectionService = Depends(get_election_service),
) -> ElectionResponse:
    return service.close(election_id, admin)
