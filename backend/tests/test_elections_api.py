from copy import deepcopy
from datetime import UTC, datetime
from uuid import UUID, uuid4

from fastapi import HTTPException
from fastapi.testclient import TestClient

from app.api.elections import get_election_service
from app.auth import (
    AdminIdentity,
    AdminLoginRequest,
    AdminSession,
    get_admin_auth_service,
    invalid_token,
)
from app.main import app
from app.schemas.elections import ElectionCreate, ElectionUpdate
from app.services.elections import ElectionService


ADMIN_ID = "11111111-1111-1111-1111-111111111111"
NON_ADMIN_ID = "22222222-2222-2222-2222-222222222222"
ORG_ID = "33333333-3333-3333-3333-333333333333"
ELECTION_ID = "44444444-4444-4444-4444-444444444444"


class FakeAuthService:
    def __init__(self, admin: AdminIdentity) -> None:
        self.admin = admin

    def login(self, credentials: AdminLoginRequest) -> AdminSession:
        raise NotImplementedError

    def current_admin(self, access_token: str) -> AdminIdentity:
        if access_token != "access-token":
            raise invalid_token()
        return self.admin

    def logout(self, access_token: str, refresh_token: str) -> None:
        raise NotImplementedError


class FakeElectionRepository:
    def __init__(self) -> None:
        self.rows: dict[str, dict] = {}

    def create(self, payload: ElectionCreate, admin_id: str) -> dict:
        election_id = str(uuid4())
        row = {
            **payload.model_dump(mode="json"),
            "id": election_id,
            "status": "DRAFT",
            "created_by": admin_id,
            "created_at": now(),
            "updated_at": now(),
            "archived_at": None,
        }
        self.rows[election_id] = row
        return deepcopy(row)

    def list_active(self) -> list[dict]:
        return [
            deepcopy(row)
            for row in self.rows.values()
            if row.get("archived_at") is None
        ]

    def get(self, election_id: UUID) -> dict | None:
        row = self.rows.get(str(election_id))
        if row is None or row.get("archived_at") is not None:
            return None
        return deepcopy(row)

    def update(self, election_id: UUID, payload: ElectionUpdate) -> dict:
        row = self.rows[str(election_id)]
        row.update(payload.model_dump(mode="json", exclude_unset=True))
        row["updated_at"] = now()
        return deepcopy(row)

    def set_status(self, election_id: UUID, status_value: str) -> dict:
        row = self.rows[str(election_id)]
        row["status"] = status_value
        row["updated_at"] = now()
        return deepcopy(row)

    def archive(self, election_id: UUID) -> None:
        row = self.rows[str(election_id)]
        row["archived_at"] = now()
        row["updated_at"] = now()


def now() -> str:
    return datetime.now(UTC).isoformat()


def valid_payload() -> dict:
    return {
        "organization_id": ORG_ID,
        "name": "Student Council Election",
        "description": "Annual student leadership election.",
        "starts_at": "2027-01-01T09:00:00Z",
        "ends_at": "2027-01-02T17:00:00Z",
    }


def seed_election(repository: FakeElectionRepository, status: str = "DRAFT") -> str:
    row = {
        **valid_payload(),
        "id": ELECTION_ID,
        "status": status,
        "created_by": ADMIN_ID,
        "created_at": now(),
        "updated_at": now(),
        "archived_at": None,
    }
    repository.rows[ELECTION_ID] = row
    return ELECTION_ID


def client_with(
    repository: FakeElectionRepository | None = None,
    admin: AdminIdentity | None = None,
) -> TestClient:
    repository = repository or FakeElectionRepository()
    admin = admin or AdminIdentity(
        id=ADMIN_ID, email="admin@example.com", role="election_admin"
    )
    app.dependency_overrides[get_admin_auth_service] = lambda: FakeAuthService(admin)
    app.dependency_overrides[get_election_service] = lambda: ElectionService(repository)
    return TestClient(app)


def auth_headers(token: str = "access-token") -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def teardown_function() -> None:
    app.dependency_overrides.clear()


def test_admin_can_create_election_and_new_election_is_draft() -> None:
    repository = FakeElectionRepository()
    response = client_with(repository).post(
        "/api/elections", json=valid_payload(), headers=auth_headers()
    )

    assert response.status_code == 201
    body = response.json()
    assert body["status"] == "DRAFT"
    assert body["created_by"] == ADMIN_ID
    assert len(repository.rows) == 1


def test_create_election_requires_authentication_and_admin_role() -> None:
    client = client_with()

    assert client.post("/api/elections", json=valid_payload()).status_code == 401

    non_admin = AdminIdentity(id=NON_ADMIN_ID, email="voter@example.com", role="voter")
    response = client_with(admin=non_admin).post(
        "/api/elections", json=valid_payload(), headers=auth_headers()
    )
    assert response.status_code == 403
    assert response.json()["detail"] == "Only administrators can perform this operation."


def test_invalid_election_data_is_rejected() -> None:
    payload = valid_payload()
    payload["name"] = " "
    payload["ends_at"] = "2026-12-31T17:00:00Z"

    response = client_with().post(
        "/api/elections", json=payload, headers=auth_headers()
    )

    assert response.status_code == 422


def test_admin_can_retrieve_elections_and_empty_result_sets() -> None:
    repository = FakeElectionRepository()
    client = client_with(repository)

    assert client.get("/api/elections", headers=auth_headers()).json() == []

    seed_election(repository)
    response = client.get("/api/elections", headers=auth_headers())

    assert response.status_code == 200
    assert response.json()[0]["id"] == ELECTION_ID


def test_get_single_election_handles_missing_and_invalid_ids() -> None:
    repository = FakeElectionRepository()
    seed_election(repository)
    client = client_with(repository)

    found = client.get(f"/api/elections/{ELECTION_ID}", headers=auth_headers())
    missing = client.get(f"/api/elections/{uuid4()}", headers=auth_headers())
    invalid = client.get("/api/elections/not-a-uuid", headers=auth_headers())

    assert found.status_code == 200
    assert found.json()["id"] == ELECTION_ID
    assert "archived_at" in found.json()
    assert missing.status_code == 404
    assert missing.json()["detail"] == "Election not found."
    assert invalid.status_code == 422


def test_retrieve_elections_requires_authentication() -> None:
    client = client_with()

    assert client.get("/api/elections").status_code == 401
    assert client.get(f"/api/elections/{ELECTION_ID}").status_code == 401


def test_admin_can_update_draft_election() -> None:
    repository = FakeElectionRepository()
    seed_election(repository)

    response = client_with(repository).patch(
        f"/api/elections/{ELECTION_ID}",
        json={"name": "Updated Election"},
        headers=auth_headers(),
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Updated Election"


def test_update_rejects_invalid_missing_unauthorized_and_status_changes() -> None:
    repository = FakeElectionRepository()
    seed_election(repository)
    client = client_with(repository)

    invalid = client.patch(
        f"/api/elections/{ELECTION_ID}",
        json={
            "starts_at": "2027-01-03T09:00:00Z",
            "ends_at": "2027-01-02T17:00:00Z",
        },
        headers=auth_headers(),
    )
    missing = client.patch(
        f"/api/elections/{uuid4()}",
        json={"name": "Missing"},
        headers=auth_headers(),
    )
    unauthenticated = client.patch(
        f"/api/elections/{ELECTION_ID}", json={"name": "Nope"}
    )
    direct_status = client.patch(
        f"/api/elections/{ELECTION_ID}",
        json={"status": "OPEN"},
        headers=auth_headers(),
    )
    empty_update = client.patch(
        f"/api/elections/{ELECTION_ID}",
        json={},
        headers=auth_headers(),
    )

    assert invalid.status_code == 422
    assert missing.status_code == 404
    assert unauthenticated.status_code == 401
    assert direct_status.status_code == 422
    assert empty_update.status_code == 400


def test_open_draft_election_succeeds() -> None:
    repository = FakeElectionRepository()
    seed_election(repository, status="DRAFT")

    response = client_with(repository).post(
        f"/api/elections/{ELECTION_ID}/open", headers=auth_headers()
    )

    assert response.status_code == 200
    assert response.json()["status"] == "OPEN"


def test_open_rejects_open_closed_incomplete_unauthenticated_and_non_admin() -> None:
    for current_status in ("OPEN", "CLOSED"):
        repository = FakeElectionRepository()
        seed_election(repository, status=current_status)
        response = client_with(repository).post(
            f"/api/elections/{ELECTION_ID}/open", headers=auth_headers()
        )
        assert response.status_code == 400

    repository = FakeElectionRepository()
    seed_election(repository)
    repository.rows[ELECTION_ID]["description"] = " "
    incomplete = client_with(repository).post(
        f"/api/elections/{ELECTION_ID}/open", headers=auth_headers()
    )
    assert incomplete.status_code == 400
    assert incomplete.json()["detail"] == "Election information is incomplete."

    assert (
        client_with(repository).post(f"/api/elections/{ELECTION_ID}/open").status_code
        == 401
    )

    non_admin = AdminIdentity(id=NON_ADMIN_ID, email="voter@example.com", role="voter")
    forbidden = client_with(repository, admin=non_admin).post(
        f"/api/elections/{ELECTION_ID}/open", headers=auth_headers()
    )
    assert forbidden.status_code == 403


def test_close_open_election_succeeds() -> None:
    repository = FakeElectionRepository()
    seed_election(repository, status="OPEN")

    response = client_with(repository).post(
        f"/api/elections/{ELECTION_ID}/close", headers=auth_headers()
    )

    assert response.status_code == 200
    assert response.json()["status"] == "CLOSED"


def test_close_rejects_draft_closed_unauthenticated_and_non_admin() -> None:
    for current_status in ("DRAFT", "CLOSED"):
        repository = FakeElectionRepository()
        seed_election(repository, status=current_status)
        response = client_with(repository).post(
            f"/api/elections/{ELECTION_ID}/close", headers=auth_headers()
        )
        assert response.status_code == 400

    repository = FakeElectionRepository()
    seed_election(repository, status="OPEN")
    assert (
        client_with(repository).post(f"/api/elections/{ELECTION_ID}/close").status_code
        == 401
    )

    non_admin = AdminIdentity(id=NON_ADMIN_ID, email="voter@example.com", role="voter")
    forbidden = client_with(repository, admin=non_admin).post(
        f"/api/elections/{ELECTION_ID}/close", headers=auth_headers()
    )
    assert forbidden.status_code == 403


def test_archive_only_allows_draft_elections() -> None:
    repository = FakeElectionRepository()
    seed_election(repository, status="DRAFT")
    client = client_with(repository)

    response = client.delete(f"/api/elections/{ELECTION_ID}", headers=auth_headers())

    assert response.status_code == 204
    assert client.get(f"/api/elections/{ELECTION_ID}", headers=auth_headers()).status_code == 404

    for current_status in ("OPEN", "CLOSED"):
        repository = FakeElectionRepository()
        seed_election(repository, status=current_status)
        response = client_with(repository).delete(
            f"/api/elections/{ELECTION_ID}", headers=auth_headers()
        )
        assert response.status_code == 400


def test_status_state_machine_allows_only_draft_to_open_to_closed() -> None:
    repository = FakeElectionRepository()
    seed_election(repository, status="DRAFT")
    client = client_with(repository)

    opened = client.post(f"/api/elections/{ELECTION_ID}/open", headers=auth_headers())
    closed = client.post(f"/api/elections/{ELECTION_ID}/close", headers=auth_headers())

    assert opened.status_code == 200
    assert closed.status_code == 200
    assert closed.json()["status"] == "CLOSED"

    invalid_cases = [
        ("DRAFT", "close"),
        ("OPEN", "open"),
        ("CLOSED", "open"),
        ("CLOSED", "close"),
    ]
    for initial_status, action in invalid_cases:
        repository = FakeElectionRepository()
        seed_election(repository, status=initial_status)
        response = client_with(repository).post(
            f"/api/elections/{ELECTION_ID}/{action}", headers=auth_headers()
        )
        assert response.status_code == 400
