
from utils.logger import get_logger

from dtos.password_dto import RequestPostPassword, ResponsePostPassword, ResponseGetPassword, ResponseListPassword, ResponseListPasswordObject

from services.password_service import PasswordService

logger = get_logger(__name__)

class PasswordController:

    @staticmethod
    async def list_passwords() -> ResponseListPassword:
        logger.info("start listing passwords")
        response = await PasswordService.list_passwords()
        return ResponseListPassword(
            data=[ResponseListPasswordObject(
                id=password.id,
                name=password.name
            ) for password in response]
        )

    @staticmethod
    async def get_password_by_id(id: int):
        logger.info("start getting password by id")
        response = await PasswordService.get_password_by_id(id)
        return ResponseGetPassword(
            id=response.id,
            password=response.password,
            name=response.name,
            description=response.description
        )

    @staticmethod
    async def post_password(payload: RequestPostPassword):
        logger.info("start creating password")
        response = await PasswordService.post_password(**payload.model_dump())
        return ResponsePostPassword()
    
