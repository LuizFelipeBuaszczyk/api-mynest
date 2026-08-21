from repositories.user_repository import UserRepository
from services.permissions_service import PermissionsService

from utils.encrypt import encrypt_password

from exceptions.user_exceptions import AlreadyExistsSuperuserException, AlreadyExistsUserException

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
        await PermissionsService.ensure_permission('users.create')

        data['is_superuser'] = False
        
        data['password'] = encrypt_password(data['password'])
        
        if UserRepository.exists_user_by_username(data['password']):
            raise AlreadyExistsUserException()

        return await UserRepository.insert_user(**data)

