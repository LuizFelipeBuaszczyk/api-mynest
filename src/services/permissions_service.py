from models.permissions import Permissions

from repositories.permissions_repository import PermissionRepository

class PermissionsService:

    @classmethod
    async def list_permissions(cls) -> list[Permissions]:
        return await PermissionRepository.list_permissions()