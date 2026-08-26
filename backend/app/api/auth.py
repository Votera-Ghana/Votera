from fastapi import APIRouter, HTTPException

from app.schemas.auth import LoginRequest
from app.core.supabase import supabase


router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"],
)


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