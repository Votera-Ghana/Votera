from fastapi import FastAPI

from app.api.admin import router as admin_router
from app.api.auth import router as auth_router

app = FastAPI(
    title="Votera API",
    description="Backend API for the Votera digital voting platform.",
    version="0.1.0",
)

app.include_router(auth_router)
app.include_router(admin_router)


@app.get("/api/health")
def health_check():
    return {
        "status": "ok",
        "service": "votera-api",
        "version": "0.1.0",
        "database": "configured",
    }
