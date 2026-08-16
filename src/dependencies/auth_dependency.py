from fastapi import Header

from exceptions.auth_exceptions import InvalidTokenException
from utils.contextvars import set_current_user

async def auth_token(access_token: str = Header()) -> None:
    from utils.token import validate_token
    
    token = validate_token(access_token)
    if token['type'] != 'AUTH':
        raise InvalidTokenException()

    set_current_user(token['user_id'])

    return 
