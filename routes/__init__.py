from fastapi import APIRouter
from routes.health import router as health_router
from routes.auth import router as auth_router

router = APIRouter()

router.include_router(auth_router)
router.include_router(health_router)