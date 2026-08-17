from dtos.roles_dto import (
    RequestPostRoles,
    ResponsePostRoles,
    ResponseListRoles,
    ResponseListRoleObject,
    ResponseGetRole
)

from services.roles_service import RolesService

class RolesController:

    @staticmethod
    async def list_roles() -> ResponseListRoles:
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
        response = await RolesService.get_role_by_id(id)
        return ResponseGetRole(
            id=response.id,
            codename=response.codename,
            description=response.description
        )

    @staticmethod
    async def post_roles(payload: RequestPostRoles) -> ResponsePostRoles:
        await RolesService.post_roles(**payload.model_dump())
        return ResponsePostRoles()