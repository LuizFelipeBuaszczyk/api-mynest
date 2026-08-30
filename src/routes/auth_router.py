from fastapi.routing import APIRouter

from utils.logger import get_logger

from controllers.auth_controller import AuthController
from dtos.auth_dto import PostAuthLoginDTO, PostAuthRefreshTokenDTO

TAG = "Auth"

router = APIRouter(prefix='/auth', tags=[TAG])
logger = get_logger(__name__)

@router.post('/login')
async def post_login(payload: PostAuthLoginDTO):
    logger.info("received a request to login")
    return await AuthController.login(payload)

@router.post('/refresh-token')
async def post_refresh_token(payload: PostAuthRefreshTokenDTO):
    logger.info("received a request to refresh token")
    return await AuthController.refresh_token(payload)
