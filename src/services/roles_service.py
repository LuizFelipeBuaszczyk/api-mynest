from models.roles import Roles
from repositories.roles_repository import RoleRepository
from exceptions.roles_exception import NotFoundRolesException

class RolesService:

    @classmethod
    async def list_roles(cls) -> list[Roles]:
        return await RoleRepository.list_roles()

    @classmethod
    async def get_role_by_id(cls, id: int) -> Roles:
        role = await RoleRepository.get_role_by_id(id)

        if not role:
            raise NotFoundRolesException()

        return role

    @classmethod
    async def post_roles(cls, **data) -> Roles:
        return await RoleRepository.insert_role(**data)