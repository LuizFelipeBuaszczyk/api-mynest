from utils.logger import get_logger

from services.auth_service import AuthService

from dtos.auth_dto import PostAuthLoginDTO, ResponsePostAuthLoginDTO, PostAuthRefreshTokenDTO, ResponsePostAuthRefreshTokenDTO

logger = get_logger(__name__)

class AuthController:

    @staticmethod
    async def login(payload: PostAuthLoginDTO):
        logger.info("start login user")
        response = await AuthService.login(payload.model_dump())
        return ResponsePostAuthLoginDTO(
            refresh_token=response['refresh_token'],
            access_token=response['access_token']
        )
    
    @staticmethod
    async def refresh_token(payload: PostAuthRefreshTokenDTO):
        logger.info("start refresh token")
        response = await AuthService.refresh_token(payload.refresh_token)
        return ResponsePostAuthRefreshTokenDTO(
            access_token=response
        )

