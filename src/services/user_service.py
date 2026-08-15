
from repositories.user_repository import UserRepository

from utils.encrypt import encrypt_password

from exceptions.user_exceptions import AlreadyExistsSuperuserException

class UserService:
    
    @classmethod
    async def create_super_user(cls, data: dict):
        data['is_superuser'] = True
        
        if await UserRepository.exists_superuser():
            raise AlreadyExistsSuperuserException()
        
        data['password'] = encrypt_password(data['password'])
        return await UserRepository.insert_user(**data)

    @classmethod
    async def create_user(cls, data: dict):
        data['is_superuser'] = False
        
        data['password'] = encrypt_password(data['password'])
        return await UserRepository.insert_user(**data)

   
