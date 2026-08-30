from utils.logger import get_logger

from dtos.user_dto import PostUserDTO

from services.user_service import UserService

logger = get_logger(__name__)

class UserController:
    
    @staticmethod
    async def post_user(data: PostUserDTO):
        logger.info("start creating user")
        return await UserService.create_user(data.model_dump())
    
    @staticmethod
    async def post_super_user(data: PostUserDTO):
        logger.info("start create super user")
        return await UserService.create_super_user(data.model_dump())

