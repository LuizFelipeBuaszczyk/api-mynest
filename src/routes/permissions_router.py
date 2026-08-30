from fastapi import Depends
from fastapi.routing import APIRouter

from utils.logger import get_logger

from dependencies.auth_dependency import auth_token
from controllers.permissions_controller import PermissionsController

TAG = 'Permissions'

router = APIRouter(prefix='/permissions', tags=[TAG])
logger = get_logger(__name__)

@router.get("/")
async def list_permissions(auth_user = Depends(auth_token)):
    logger.info("received a request to list permissions")
    return await PermissionsController.list_permissions()