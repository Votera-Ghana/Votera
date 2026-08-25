from fastapi import FastAPI

<<<<<<< HEAD
from app.api.auth import router as auth_router

from app.core.supabase import supabase
=======
from app.api.admin import router as admin_router
from app.api.auth import router as auth_router
>>>>>>> c70571aa5f0f61cecdfa9661edea9626cb83e190

app = FastAPI(
    title="Votera API",
    description="Backend API for the Votera digital voting platform.",
    version="0.1.0",
)

app.include_router(auth_router)
<<<<<<< HEAD
=======
app.include_router(admin_router)

>>>>>>> c70571aa5f0f61cecdfa9661edea9626cb83e190

@app.get("/api/health")
def health_check():
    return {
        "status": "ok",
        "service": "votera-api",
        "version": "0.1.0",
        "database": "configured",
    }
