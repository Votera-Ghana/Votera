from fastapi import APIRouter, Cookie, Depends, HTTPException, Response, status

from app.auth import (
    AdminIdentity,
    AdminLoginRequest,
    AdminSession,
    bearer_scheme,
    get_admin_auth_service,
    get_current_admin,
)
from app.schemas.auth import LoginRequest
from app.core.supabase import supabase


router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"],
)


@router.post("/admin/login", response_model=AdminSession)
async def login_admin_session(
    data: AdminLoginRequest,
    response: Response,
    service=Depends(get_admin_auth_service),
) -> AdminSession:
    session = service.login(data)
    response.set_cookie(
        "votera_admin_refresh_token",
        session.refresh_token,
        httponly=True,
        secure=True,
        samesite="lax",
        path="/api/auth",
    )
    return session


@router.post("/admin/logout", status_code=status.HTTP_204_NO_CONTENT)
async def logout_admin_session(
    admin: AdminIdentity = Depends(get_current_admin),
    service=Depends(get_admin_auth_service),
    credentials=Depends(bearer_scheme),
    refresh_token: str | None = Cookie(
        default=None, alias="votera_admin_refresh_token"
    ),
) -> Response:
    _ = admin
    if refresh_token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired authentication token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    service.logout(credentials.credentials, refresh_token)
    response = Response(status_code=status.HTTP_204_NO_CONTENT)
    response.delete_cookie("votera_admin_refresh_token", path="/api/auth")
    return response


@router.post("/login")
async def login_admin(data: LoginRequest):
    try:
        response = supabase.auth.sign_in_with_password(
            {
                "email": data.email,
                "password": data.password,
            }
        )

        if response.user is None or response.session is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password",
            )

        return {
            "message": "Login successful",
            "user_id": response.user.id,
            "email": response.user.email,
            "access_token": response.session.access_token,
            "token_type": "bearer",
        }

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )
