from fastapi import APIRouter
from routes.health_router import router as health_router
from routes.users_router import router as user_router

router = APIRouter()

router.include_router(health_router)
router.include_router(user_router)

