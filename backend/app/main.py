from fastapi import FastAPI

from app.api.auth import router as auth_router

from app.core.supabase import supabase

app = FastAPI(
    title="Votera API",
    description="Backend API for the Votera digital voting platform.",
    version="0.1.0",
)

app.include_router(auth_router)

@app.get("/api/health")
def health_check():
    return {
        "status": "ok",
        "service": "votera-api",
        "version": "0.1.0",
        "database": "configured",
    }