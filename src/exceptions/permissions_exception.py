from exceptions.base_exceptions import NotFoundException, BusinessException, APPException

class NotFoundPermissionException(NotFoundException):
    default_detail = "Permission not found"

class DuplicatePermissionException(BusinessException):
    default_detail = "Duplicate permission"

class PermissionDeniedException(APPException):
    default_status_code = 403
    default_detail = "Permission denied"
