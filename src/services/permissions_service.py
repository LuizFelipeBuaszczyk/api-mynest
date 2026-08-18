from models.permissions import Permissions

from repositories.permissions_repository import PermissionRepository
from exceptions.permissions_exception import NotFoundPermissionException, DuplicatePermissionException
from utils.length import is_same_size

class PermissionsService:

    @classmethod
    async def list_permissions(cls) -> list[Permissions]:
        return await PermissionRepository.list_permissions()

    @classmethod
    async def exists_permissions_by_id_list(cls, id_list: list[int]) -> list[int]:
        if len(id_list) == 0:
            return []

        permissions = await PermissionRepository.get_permissions_by_ids(id_list)
        id_dict = { id:True for id in permissions}
        missing = [id for id in id_list if not id_dict.get(id)]
        if missing:
            raise NotFoundPermissionException(detail=f"Permissions not found: {missing}")
       
        if not is_same_size(id_list, permissions):
            raise DuplicatePermissionException()

        return id_list 

