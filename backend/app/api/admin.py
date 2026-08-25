from fastapi import APIRouter, Depends

from app.auth import AdminIdentity, get_current_admin

router = APIRouter(prefix="/api/admin", tags=["admin"])


@router.get("/session", response_model=AdminIdentity)
def get_admin_session(admin: AdminIdentity = Depends(get_current_admin)) -> AdminIdentity:
    return admin
