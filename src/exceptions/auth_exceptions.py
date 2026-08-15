from exceptions.base_exceptions import UnauthorizedException

class InvalidTokenException(UnauthorizedException):
    default_detail = "Invalid token"

class InvalidCredentialsException(UnauthorizedException):
    default_detail = "Invalid credentials"
