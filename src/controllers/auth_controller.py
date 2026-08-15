from services.auth_service import AuthService

from dtos.auth_dto import PostAuthLoginDTO

class AuthController:

    @staticmethod
    async def login(payload: PostAuthLoginDTO):
        
        return await AuthService.login(payload.model_dump())
