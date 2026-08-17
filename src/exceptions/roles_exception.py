from exceptions.base_exceptions import NotFoundException

class NotFoundRolesException(NotFoundException):
    default_detail = "Role not found"