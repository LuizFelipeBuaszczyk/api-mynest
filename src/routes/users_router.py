from fastapi import Depends
from fastapi.routing import APIRouter

from utils.logger import get_logger

from dtos.user_dto import PostUserDTO
from controllers.user_controller import UserController
from dependencies.auth_dependency import auth_token

router = APIRouter(prefix='/users', tags=['Users'])
logger = get_logger(__name__)

@router.post("/super")
async def post_super_user(payload: PostUserDTO):
    logger.info("received a request to create super user")
    return await UserController.post_super_user(payload)

# TODO Necessita autenticação de admin para essa rota
@router.post('/')
async def post_user(payload: PostUserDTO, auth_user = Depends(auth_token)):
    logger.info("received a request to create user")
    return await UserController.post_user(payload)
