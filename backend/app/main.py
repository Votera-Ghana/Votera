from fastapi import FastAPI

from app.core.supabase import supabase

app = FastAPI(
    title="Votera API",
    description="Backend API for the Votera digital voting platform.",
    version="0.1.0",
)


@app.get("/api/health")
def health_check():
    return {
        "status": "ok",
        "service": "votera-api",
        "version": "0.1.0",
        "database": "configured",
    }