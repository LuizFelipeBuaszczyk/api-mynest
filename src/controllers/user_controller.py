from dtos.user_dto import PostUserDTO

from services.user_service import UserService

class UserController:
    
    @staticmethod
    async def post_super_user(data: PostUserDTO):
        return await UserService.create_super_user(data.model_dump())

    @staticmethod
    async def post_user(data: PostUserDTO):
       return await UserService.create_user()
