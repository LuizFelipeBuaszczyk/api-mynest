from fastapi import Request
from fastapi.responses import JSONResponse
from exceptions.base_exceptions import APPException
from utils.logger import get_logger

logger = get_logger(__name__)

def app_handler_exception(request: Request, exc: Exception):
    
    if isinstance(exc, APPException):
        logger.warning(f"error - {exc.detail}")
        return JSONResponse(
            status_code=exc.status_code,
            content={
                'detail': exc.detail
            }
        )
    logger.critical(f"error - {str(exc)}")
    return JSONResponse(
            status_code=500,
            content={
                'detail': 'Internal Server Error'
            }
        )
