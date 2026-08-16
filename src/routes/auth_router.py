from fastapi.routing import APIRouter

from controllers.auth_controller import AuthController
from dtos.auth_dto import PostAuthLoginDTO, PostAuthRefreshTokenDTO

router = APIRouter(prefix='/auth')

@router.post('/login')
async def post_login(payload: PostAuthLoginDTO):
    return await AuthController.login(payload)

@router.post('/refresh-token')
async def post_refresh_token(payload: PostAuthRefreshTokenDTO):
    return await AuthController.refresh_token(payload)
