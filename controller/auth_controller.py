from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from dto import auth_dto as dto

from service.auth_service import AuthService

class AuthController:

    def __init__(self):
        pass

    async def login(self, user: dto.requestUserLoginDTO):
        try:
            auth_service = AuthService()
            
            if await auth_service.login(user=user):
                return JSONResponse(
                    status_code=status.HTTP_200_OK,
                    content={
                        "message": "Success"
                    }
                )
            else:
                return JSONResponse(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    content={
                        "message": "Internal Server Error."
                    }
                )
        except HTTPException as E:
            return JSONResponse(
                status_code=E.status_code,
                content={
                    "message": E.detail
                }
            )
        
        except Exception as E:
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                    "message": f"Internal Server Error. - {E}"
                }
            )