from typing import Any

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel, EmailStr, Field

ADMIN_ROLES = {"election_admin", "system_admin"}
bearer_scheme = HTTPBearer(auto_error=False)


class AdminLoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=1, max_length=256)


class AdminIdentity(BaseModel):
    id: str
    email: EmailStr
    role: str


class AdminSession(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
    expires_in: int | None = None
    admin: AdminIdentity


def _value(source: Any, name: str, default: Any = None) -> Any:
    if isinstance(source, dict):
        return source.get(name, default)
    return getattr(source, name, default)


class AdminAuthService:
    def __init__(self, auth_client: Any, database_client: Any) -> None:
        self.auth_client = auth_client
        self.database_client = database_client

    def login(self, credentials: AdminLoginRequest) -> AdminSession:
        try:
            response = self.auth_client.auth.sign_in_with_password(
                {"email": str(credentials.email), "password": credentials.password}
            )
            session = _value(response, "session")
            user = _value(response, "user")
            if not session or not user:
                raise ValueError("Missing authentication session")
            identity = self._admin_identity(_value(user, "id"))
        except HTTPException:
            raise
        except Exception as error:
            raise invalid_credentials() from error

        return AdminSession(
            access_token=_value(session, "access_token"),
            refresh_token=_value(session, "refresh_token"),
            token_type=_value(session, "token_type", "bearer"),
            expires_in=_value(session, "expires_in"),
            admin=identity,
        )

    def current_admin(self, access_token: str) -> AdminIdentity:
        try:
            response = self.auth_client.auth.get_user(access_token)
            user = _value(response, "user")
            user_id = _value(user, "id")
            if not user_id:
                raise ValueError("Missing authenticated user")
            return self._admin_identity(user_id)
        except HTTPException:
            raise
        except Exception as error:
            raise invalid_token() from error

    def logout(self, access_token: str, refresh_token: str) -> None:
        try:
            self.auth_client.auth.set_session(access_token, refresh_token)
            self.auth_client.auth.sign_out({"scope": "global"})
        except Exception as error:
            raise invalid_token() from error

    def _admin_identity(self, user_id: str | None) -> AdminIdentity:
        if not user_id:
            raise invalid_credentials()
        response = (
            self.database_client.table("users")
            .select("id, email, role, is_active")
            .eq("id", user_id)
            .maybe_single()
            .execute()
        )
        profile = _value(response, "data")
        role = _value(profile, "role")
        if not profile or not _value(profile, "is_active") or role not in ADMIN_ROLES:
            raise invalid_credentials()
        return AdminIdentity(
            id=_value(profile, "id"), email=_value(profile, "email"), role=role
        )


def invalid_credentials() -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid administrator credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )


def invalid_token() -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired authentication token",
        headers={"WWW-Authenticate": "Bearer"},
    )


def get_admin_auth_service() -> AdminAuthService:
    from app.core.supabase import supabase, supabase_auth

    return AdminAuthService(supabase_auth, supabase)


def get_current_admin(
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
    service: AdminAuthService = Depends(get_admin_auth_service),
) -> AdminIdentity:
    if credentials is None or credentials.scheme.lower() != "bearer":
        raise invalid_token()
    return service.current_admin(credentials.credentials)
