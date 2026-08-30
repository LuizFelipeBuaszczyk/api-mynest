from utils.logger import get_logger

from dtos.roles_dto import (
    RequestPostRoles,
    ResponsePostRoles,
    ResponseListRoles,
    ResponseListRoleObject,
    ResponseGetRole,
    RequestPostRolePermissions,
    ResponsePostRolePermissions,
    ResponseListRolePermissions
)

from services.roles_service import RolesService

logger = get_logger(__name__)

class RolesController:

    @staticmethod
    async def list_roles() -> ResponseListRoles:
        logger.info("start listing roles")
        response = await RolesService.list_roles()
        return ResponseListRoles(
            data=[
                ResponseListRoleObject(
                    id=role.id,
                    codename=role.codename
                ) for role in response
            ]
        )

    @staticmethod
    async def get_role_by_id(id: int) -> ResponseGetRole:
        logger.info("start getting role by id")
        response = await RolesService.get_role_by_id(id)
        return ResponseGetRole(
            id=response.id,
            codename=response.codename,
            description=response.description
        )

    @staticmethod
    async def post_roles(payload: RequestPostRoles) -> ResponsePostRoles:
        logger.info("start creating role")
        await RolesService.post_roles(**payload.model_dump())
        return ResponsePostRoles()

    @staticmethod
    async def post_role_permissions(id: int, payload: RequestPostRolePermissions) -> ResponsePostRolePermissions:
        logger.info("start assigning permissions to role")
        await RolesService.post_role_permissions(role_id=id, **payload.model_dump())
        return ResponsePostRolePermissions()

    @staticmethod
    async def get_role_permissions(id: int) -> ResponseListRolePermissions:
        logger.info("start getting role permissions")
        response = await RolesService.get_role_permissions(id)
        return ResponseListRolePermissions(data=response)

