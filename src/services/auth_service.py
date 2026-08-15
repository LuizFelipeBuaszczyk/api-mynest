
from repositories.user_repository import UserRepository

from utils.encrypt import encrypt_password
from utils.token import create_auth_token

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

        return {
            'token': create_auth_token(user.id)
        }


