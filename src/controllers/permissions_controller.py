from dtos.permissions_dto import (
    ResponseListPermissions,
    ResponseListPermissionObject
)

from services.permissions_service import PermissionsService

class PermissionsController:

    @staticmethod
    async def list_permissions() -> ResponseListPermissions:
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
