from fastapi import Depends
from fastapi.routing import APIRouter

from utils.logger import get_logger

from dependencies.auth_dependency import auth_token
from controllers.roles_controller import RolesController
from dtos.roles_dto import (
    RequestPostRoles,
    RequestPostRolePermissions
)

TAG = 'Roles'

router = APIRouter(prefix='/roles', tags=[TAG])
logger = get_logger(__name__)

@router.get("/")
async def list_roles(auth_user = Depends(auth_token)):
    logger.info("received a request to list roles")
    return await RolesController.list_roles()

@router.post("/")
async def post_roles(payload: RequestPostRoles, auth_user = Depends(auth_token)):
    return await RolesController.post_roles(payload)

@router.get("/{id}")
async def get_role_by_id(id: int, auth_user = Depends(auth_token)):
    return await RolesController.get_role_by_id(id)

@router.get("/{id}/permissions")
async def get_role_permissions(id: int, auth_user = Depends(auth_token)):
    return await RolesController.get_role_permissions(id)

@router.post("/{id}/permissions")
async def post_role_permissions(id: int, payload: RequestPostRolePermissions, auth_user = Depends(auth_token)):
    return await RolesController.post_role_permissions(id, payload)
