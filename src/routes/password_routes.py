from fastapi import Depends
from fastapi.routing import APIRouter

from utils.logger import get_logger

from dependencies.auth_dependency import auth_token

from controllers.password_controller import PasswordController
from dtos.password_dto import RequestPostPassword

TAG = 'Passwords'

router = APIRouter(prefix='/passwords', tags=[TAG])
logger = get_logger(__name__)

@router.get("/")
async def list_password(auth_user = Depends(auth_token)):
    logger.info("received a request to list passwords")
    return await PasswordController.list_passwords()

@router.get("/{id}")
async def get_password_by_id(id: int, auth_user = Depends(auth_token)):
    return await PasswordController.get_password_by_id(id)

@router.post("/")
async def post_password(payload: RequestPostPassword, auth_user = Depends(auth_token)):
    return await PasswordController.post_password(payload) 


