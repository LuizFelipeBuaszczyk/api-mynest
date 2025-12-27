from fastapi import APIRouter
from routes.health import router as health_routes

router = APIRouter()

router.include_router(health_routes)

