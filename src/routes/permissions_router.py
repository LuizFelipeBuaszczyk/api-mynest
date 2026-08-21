from fastapi import Depends
from fastapi.routing import APIRouter

from dependencies.auth_dependency import auth_token
from controllers.permissions_controller import PermissionsController

TAG = 'Permissions'

router = APIRouter(prefix='/permissions', tags=[TAG])

@router.get("/")
async def list_permissions(auth_user = Depends(auth_token)):
    return await PermissionsController.list_permissions()