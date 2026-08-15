from services.auth_service import AuthService

from dtos.auth_dto import PostAuthLoginDTO, ResponsePostAuthLoginDTO

class AuthController:

    @staticmethod
    async def login(payload: PostAuthLoginDTO):
        
        response = await AuthService.login(payload.model_dump())

        return ResponsePostAuthLoginDTO(
            refresh_token=response['refresh_token'],
            access_token=response['access_token']
        )
    
