from exceptions.base_exceptions import (
    BusinessException,
    NotFoundException
)

class NotFoundRolesException(NotFoundException):
    default_detail = "Role not found"

class RolePermissionAlreadyExistsException(BusinessException):
    default_detail = "Role and permission already associated"