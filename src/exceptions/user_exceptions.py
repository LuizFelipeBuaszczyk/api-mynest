from exceptions.base_exceptions import BusinessException

class AlreadyExistsSuperuserException(BusinessException):
    default_detail = "Super User has already created"
