from utils.logger import get_logger

from dtos.permissions_dto import (
    ResponseListPermissions,
    ResponseListPermissionObject
)

from services.permissions_service import PermissionsService

logger = get_logger(__name__)

class PermissionsController:

    @staticmethod
    async def list_permissions() -> ResponseListPermissions:
        logger.info("start listing permissions")
        response = await PermissionsService.list_permissions()
        return ResponseListPermissions(
            data=[
                ResponseListPermissionObject(
                    id=permission.id,
                    codename=permission.codename,
                    description=permission.description
                ) for permission in response
            ]
        )

