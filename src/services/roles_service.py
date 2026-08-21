from models.roles import Roles
from repositories.roles_repository import RoleRepository
from services.permissions_service import PermissionsService
from exceptions.roles_exception import (
    NotFoundRolesException,
    RolePermissionAlreadyExistsException
)

class RolesService:

    @classmethod
    async def list_roles(cls) -> list[Roles]:
        await PermissionsService.ensure_permission('roles.view')

        return await RoleRepository.list_roles()

    @classmethod
    async def get_role_by_id(cls, id: int) -> Roles:
        await PermissionsService.ensure_permission('roles.view')

        role = await RoleRepository.get_role_by_id(id)

        if not role:
            raise NotFoundRolesException()

        return role

    @classmethod
    async def post_roles(cls, **data) -> Roles:
        await PermissionsService.ensure_permission('roles.create')

        return await RoleRepository.insert_role(**data)

    @classmethod
    async def post_role_permissions(cls, role_id: int, permission_ids: list[int]) -> None:
        await PermissionsService.ensure_permission('roles.edit')

        await cls.get_role_by_id(role_id)

        permission_ids = await PermissionsService.exists_permissions_by_id_list(permission_ids)

        associated = await RoleRepository.find_association_permissions(role_id, permission_ids)
        duplicates = [id for id in permission_ids if id in associated]

        if duplicates:
            raise RolePermissionAlreadyExistsException(detail=f"Permissions already associated: {duplicates}")

        await RoleRepository.insert_role_permissions(role_id, permission_ids)

    @classmethod
    async def get_role_permissions(cls, role_id: int) -> list[int]:
        await cls.get_role_by_id(role_id)

        return await RoleRepository.list_permissions_by_role_id(role_id)
