from fastapi import FastAPI
from app.api.routes.resume import router as resume_router
from app.api.routes.health import router as health_router

app = FastAPI(title="AI Resume Parser API")

app.include_router(resume_router, prefix="/api")
app.include_router(health_router, prefix="/api")
