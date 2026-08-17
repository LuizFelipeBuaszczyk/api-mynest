from fastapi import APIRouter
from routes.health_router import router as health_router
from routes.users_router import router as user_router
from routes.auth_router import router as auth_router
from routes.password_routes import router as password_router
from routes.roles_router import router as roles_router

router = APIRouter()

router.include_router(health_router)
router.include_router(auth_router)
router.include_router(user_router)
router.include_router(password_router)
router.include_router(roles_router)
