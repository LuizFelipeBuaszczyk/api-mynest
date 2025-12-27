from fastapi import APIRouter
from dto import auth_dto as dto

from controller.auth_controller import AuthController

router = APIRouter(prefix='/auth', tags=['Auth'])
auth_controller = AuthController()

@router.post("/login")
async def login(user: dto.requestUserLoginDTO):
    return await auth_controller.login(user=user)