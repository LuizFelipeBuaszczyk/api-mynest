from utils.logger import get_logger

from models.permissions import Permissions

from repositories.permissions_repository import PermissionRepository
from repositories.user_repository import UserRepository
from exceptions.permissions_exception import NotFoundPermissionException, DuplicatePermissionException, PermissionDeniedException
from exceptions.user_exceptions import NotFoundUserException
from utils.contextvars import get_current_user
from utils.length import is_same_size

logger = get_logger(__name__)

class PermissionsService:

    @classmethod
    async def list_permissions(cls) -> list[Permissions]:
        logger.info("start business rule to list permissions")
        await cls.ensure_permission('permissions.view')

        return await PermissionRepository.list_permissions()

    @classmethod
    async def exists_permissions_by_id_list(cls, id_list: list[int]) -> list[int]:
        logger.info("start business rule to exist permissions by id list")
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

    @classmethod
    async def has_permission(cls, user_id: int, permission_codename: str) -> bool:
        logger.info("verifying if user has permission")
        user = await UserRepository.get_user_by_id(user_id)
        if not user:
            raise NotFoundUserException()

        if user.is_superuser:
            return True

        return await UserRepository.user_has_permission_by_codename(user_id, permission_codename)
        
    @classmethod
    async def ensure_permission(cls, permission_codename: str, user_id: int | None = None) -> None:
        logger.info("start business rule to ensure permission")
        user_id = user_id or get_current_user()

        if not await cls.has_permission(user_id, permission_codename):
            raise PermissionDeniedException()

