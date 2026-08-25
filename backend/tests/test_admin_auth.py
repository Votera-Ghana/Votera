from fastapi import HTTPException
from fastapi.testclient import TestClient

from app.auth import (
    AdminIdentity,
    AdminLoginRequest,
    AdminSession,
    get_admin_auth_service,
    invalid_credentials,
    invalid_token,
)
from app.main import app


ADMIN = AdminIdentity(
    id="admin-1", email="admin@example.com", role="election_admin"
)


class FakeAdminAuthService:
    def __init__(self, valid_login: bool = True) -> None:
        self.valid_login = valid_login
        self.logged_out_token: str | None = None

    def login(self, credentials: AdminLoginRequest) -> AdminSession:
        if not self.valid_login:
            raise invalid_credentials()
        return AdminSession(
            access_token="access-token",
            refresh_token="refresh-token",
            token_type="bearer",
            expires_in=3600,
            admin=ADMIN,
        )

    def current_admin(self, access_token: str) -> AdminIdentity:
        if access_token != "access-token":
            raise invalid_token()
        return ADMIN

    def logout(self, access_token: str, refresh_token: str) -> None:
        if access_token != "access-token" or refresh_token != "refresh-token":
            raise invalid_token()
        self.logged_out_token = access_token


def client_with(service: FakeAdminAuthService) -> TestClient:
    app.dependency_overrides[get_admin_auth_service] = lambda: service
    return TestClient(app)


def teardown_function() -> None:
    app.dependency_overrides.clear()


def test_admin_can_log_in_with_valid_credentials() -> None:
    response = client_with(FakeAdminAuthService()).post(
        "/api/auth/admin/login",
        json={"email": "admin@example.com", "password": "correct-password"},
    )

    assert response.status_code == 200
    assert response.json()["admin"]["role"] == "election_admin"
    assert "HttpOnly" in response.headers["set-cookie"]
    assert "Secure" in response.headers["set-cookie"]


def test_invalid_admin_credentials_are_rejected() -> None:
    response = client_with(FakeAdminAuthService(valid_login=False)).post(
        "/api/auth/admin/login",
        json={"email": "admin@example.com", "password": "wrong-password"},
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid administrator credentials"


def test_admin_endpoint_requires_a_valid_bearer_token() -> None:
    client = client_with(FakeAdminAuthService())

    assert client.get("/api/admin/session").status_code == 401
    assert client.get(
        "/api/admin/session", headers={"Authorization": "Bearer invalid"}
    ).status_code == 401
    assert client.get(
        "/api/admin/session", headers={"Authorization": "Bearer access-token"}
    ).json() == ADMIN.model_dump(mode="json")


def test_logout_revokes_the_authenticated_session() -> None:
    service = FakeAdminAuthService()
    client = client_with(service)
    client.cookies.set("votera_admin_refresh_token", "refresh-token", path="/api/auth")

    response = client.post(
        "/api/auth/admin/logout", headers={"Authorization": "Bearer access-token"}
    )

    assert response.status_code == 204
    assert service.logged_out_token == "access-token"
