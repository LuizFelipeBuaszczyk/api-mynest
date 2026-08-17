
from dtos.password_dto import RequestPostPassword, ResponsePostPassword, ResponseGetPassword, ResponseListPassword, ResponseListPasswordObject

from services.password_service import PasswordService

class PasswordController:
    
    @staticmethod
    async def list_passwords() -> ResponseListPassword:
        response = await PasswordService.list_passwords()
        return ResponseListPassword(
            data=[ResponseListPasswordObject(
                id=password.id,
                name=password.name
            ) for password in response]
        )

    @staticmethod
    async def get_password_by_id(id: int):
        response = await PasswordService.get_password_by_id(id)
        return ResponseGetPassword(
            id=response.id,
            password=response.password,
            name=response.name,
            description=response.description
        )

    @staticmethod
    async def post_password(payload: RequestPostPassword):

        response = await PasswordService.post_password(**payload.model_dump())

        return ResponsePostPassword()
