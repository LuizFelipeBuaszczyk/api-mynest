from fastapi import Request
from fastapi.responses import JSONResponse
from exceptions.base_exceptions import APPException

def app_handler_exception(request: Request, exc: Exception):
    print(type(exc))
    
    if isinstance(exc, APPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                'detail': exc.detail
            }
        )
    
    return JSONResponse(
            status_code=500,
            content={
                'detail': 'Internal Server Error'
            }
        )
