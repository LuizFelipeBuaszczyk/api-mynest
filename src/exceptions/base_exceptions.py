from fastapi.exceptions import HTTPException


class APPException(HTTPException):
    default_status_code = 500
    default_detail = "Internal Server Error"

    def __init__(self, status_code: int | None=None, detail: str | None=None) -> None:
        status_code = status_code or self.default_status_code
        detail = detail or self.default_detail

        super().__init__(status_code, detail)

class UnauthorizedException(APPException):
    default_status_code = 401
    default_detail = "Not authorized"

class BusinessException(APPException):
    default_status_code = 400
    default_detail = "Bad request"
