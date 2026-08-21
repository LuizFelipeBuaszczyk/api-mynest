import os

from models.passwords import Passwords
from utils.contextvars import get_current_user
from repositories.password_repository import PasswordRepository
from services.permissions_service import PermissionsService
from exceptions.password_exception import NotFoundPasswordException

class PasswordService:

    @classmethod
    async def list_passwords(cls):
        user_id = get_current_user()

        await PermissionsService.ensure_permission('passwords.view', user_id)

        return await PasswordRepository.list_passwords_by_owner(user_id)

    @classmethod
    async def get_password_by_id(cls, id: int) -> Passwords:
        user_id = get_current_user()

        await PermissionsService.ensure_permission('passwords.view', user_id)

        password = await PasswordRepository.get_password_by_id(id)

        if not password:
            raise NotFoundPasswordException()

        if user_id != password.fk_owner:
            raise NotFoundPasswordException()

        password.password = await cls._decrypt_password(password.password)
        return password

    @classmethod
    async def post_password(cls, **data):
        user_id = get_current_user()

        await PermissionsService.ensure_permission('passwords.create', user_id)
        
        password_data = {
            'fk_owner': user_id,
            'password': await cls._encrypt_password(data['password']),
            'name': data['name'],
            'description': data['description']
        }

        return await PasswordRepository.insert_password(**password_data)
    
    @classmethod
    async def _encrypt_password(cls, password: str) -> str:
        from cryptography.fernet import Fernet
        key = os.getenv('ENCRYPT_KEY', None)
        if not key:
            raise Exception('ENCRYPT_KEY is not defined')

        cipher_suite = Fernet(key.encode('utf-8'))
        return cipher_suite.encrypt(password.encode('utf-8')).decode('utf-8')

    @classmethod
    async def _decrypt_password(cls, password: str) -> str:
        from cryptography.fernet import Fernet
        key = os.getenv('ENCRYPT_KEY', None)
        if not key:
            raise Exception('ENCRYPT_KEY is not defined')

        cipher_suite = Fernet(key.encode('utf-8'))
        return cipher_suite.decrypt(password.encode('utf-8')).decode('utf-8')


