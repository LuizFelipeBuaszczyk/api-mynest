from fastapi.routing import APIRouter

from dtos.user_dto import PostUserDTO
from controllers.user_controller import UserController

router = APIRouter(prefix='/users', tags=['Users'])

@router.post("/super")
async def post_super_user(payload: PostUserDTO):
    return await UserController.post_super_user(payload)

# TODO Necessita autenticação de admin para essa rota
@router.post('/')
async def post_user(payload: PostUserDTO):
    return await UserController.post_user(payload)
