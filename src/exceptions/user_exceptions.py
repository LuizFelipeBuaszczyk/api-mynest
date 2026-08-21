from exceptions.base_exceptions import BusinessException, NotFoundException

class AlreadyExistsSuperuserException(BusinessException):
    default_detail = "Super User has already created"

class AlreadyExistsUserException(BusinessException):
    default_detail = "User has already created"

class NotFoundUserException(NotFoundException):
    default_detail = "User not found"
