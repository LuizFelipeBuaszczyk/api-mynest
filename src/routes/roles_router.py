from fastapi import Depends
from fastapi.routing import APIRouter

from dependencies.auth_dependency import auth_token
from controllers.roles_controller import RolesController
from dtos.roles_dto import RequestPostRoles

TAG = 'Roles'

router = APIRouter(prefix='/roles', tags=[TAG])

@router.get("/")
async def list_roles(auth_user = Depends(auth_token)):
    return await RolesController.list_roles()

@router.get("/{id}")
async def get_role_by_id(id: int, auth_user = Depends(auth_token)):
    return await RolesController.get_role_by_id(id)

@router.post("/")
async def post_roles(payload: RequestPostRoles, auth_user = Depends(auth_token)):
    return await RolesController.post_roles(payload)