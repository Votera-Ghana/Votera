from fastapi import APIRouter, Depends, Request, Response, status
from fastapi.security import HTTPAuthorizationCredentials

from app.auth import (
    AdminAuthService,
    AdminLoginRequest,
    AdminSession,
    bearer_scheme,
    get_admin_auth_service,
    get_current_admin,
    invalid_token,
)

router = APIRouter(prefix="/api/auth", tags=["authentication"])


@router.post("/admin/login", response_model=AdminSession)
def admin_login(
    credentials: AdminLoginRequest,
    response: Response,
    service: AdminAuthService = Depends(get_admin_auth_service),
) -> AdminSession:
    session = service.login(credentials)
    response.set_cookie(
        key="votera_admin_refresh_token",
        value=session.refresh_token,
        httponly=True,
        secure=True,
        samesite="lax",
        max_age=60 * 60 * 24 * 30,
        path="/api/auth",
    )
    return session


@router.post("/admin/logout", status_code=status.HTTP_204_NO_CONTENT)
def admin_logout(
    request: Request,
    response: Response,
    token: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
    _admin=Depends(get_current_admin),
    service: AdminAuthService = Depends(get_admin_auth_service),
) -> None:
    if token is None:
        raise invalid_token()
    refresh_token = request.cookies.get("votera_admin_refresh_token")
    if not refresh_token:
        raise invalid_token()
    service.logout(token.credentials, refresh_token)
    response.delete_cookie("votera_admin_refresh_token", path="/api/auth")
