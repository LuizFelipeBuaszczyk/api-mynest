from fastapi import status
from fastapi.responses import JSONResponse

from dto import auth_dto as dto

class AuthController:

    def __init__(self):
        pass

    async def login(self, user: dto.requestUserLoginDTO):
        try:
            return JSONResponse(
                status_code=status.HTTP_501_NOT_IMPLEMENTED,
                content={"message": "Not Implemented"}
            )
        except Exception as E:
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                    "message": "Internal Server Error."
                }
            )