from utils.logger import get_logger

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from repositories.user_repository import UserRepository

from utils.encrypt import encrypt_password
from utils.token import create_auth_token, validate_token

from exceptions.auth_exceptions import InvalidCredentialsException

AUTH_TOKEN_EXP = timedelta(minutes=5)
REFRESH_TOKEN_EXP = timedelta(days=1)

logger = get_logger(__name__)

class AuthService:
    @classmethod
    async def login(cls, data: dict):
        logger.info("start business rule to login user")
        if  "username" not in data:
            raise InvalidCredentialsException()

        user = await UserRepository.get_user_by_username(data['username'])
        if not user:
            raise InvalidCredentialsException()
        
        password_encrypted = encrypt_password(data['password'])
        
        if password_encrypted != user.password:
            raise InvalidCredentialsException()
        
        access_token_payload = {
            'type': 'AUTH',
            'user_id': user.id,
            'exp': datetime.now(ZoneInfo('America/Sao_Paulo')) + AUTH_TOKEN_EXP
        }

        refresh_token_payload = {
            'type': 'REFRESH',
            'user_id': user.id,
            'exp': datetime.now(ZoneInfo('America/Sao_Paulo')) + REFRESH_TOKEN_EXP
        }

        return {
            'access_token': create_auth_token(access_token_payload),
            'refresh_token': create_auth_token(refresh_token_payload)
        }

    
    @classmethod
    async def refresh_token(cls, refresh_token: str) -> str:
        logger.info("start business rule to refresh token")
        token = validate_token(refresh_token) 
        token['type'] = 'AUTH'
        token['exp'] = datetime.now(ZoneInfo('America/Sao_Paulo')) + REFRESH_TOKEN_EXP

        return create_auth_token(token)

