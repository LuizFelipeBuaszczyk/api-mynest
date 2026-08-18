from exceptions.base_exceptions import NotFoundException, BusinessException

class NotFoundPermissionException(NotFoundException):
    default_detail = "Permission not found"

class DuplicatePermissionException(BusinessException):
    default_detail = "Duplicate permission"
