from exceptions.base_exceptions import NotFoundException

class NotFoundPasswordException(NotFoundException):
    default_detail="Password not found"
