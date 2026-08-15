from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from repositories.user_repository import UserRepository

from utils.encrypt import encrypt_password
from utils.token import create_auth_token

AUTH_TOKEN_EXP = timedelta(minutes=5)
REFRESH_TOKEN_EXP = timedelta(days=1)

class AuthService:

    @classmethod
    async def login(cls, data: dict):
        if  "username" not in data:
            raise Exception("Invalid credentials") #TODO Exception personalizada

        user = await UserRepository.get_user_by_username(data['username'])
        if not user:
            raise Exception("Invalid credentials") #TODO Exception personalizada
        
        password_encrypted = encrypt_password(data['password'])
        
        if password_encrypted != user.password:
            raise Exception("Invalid credentials") #TODO Exception personalizada
        
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


