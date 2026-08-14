
from repositories.user_repository import UserRepository

class UserService:
    
    @classmethod
    async def create_super_user(cls, data: dict):
        data['is_superuser'] = True
        
        if await UserRepository.exists_superuser():
            raise Exception("Não é possível ter dois super usuários") # TODO Exception especifica
        
        data['password'] = cls._encrypt_password(data['password'])
        return await UserRepository.insert_user(**data)

    @classmethod
    async def create_user(cls, data: dict):
        data['is_superuser'] = False
        
        data['password'] = cls._encrypt_password(data['password'])
        return await UserRepository.insert_user(**data)

    @classmethod
    def _encrypt_password(cls, password: str):
        import hashlib
        from utils.settings import ENCRYPT_KEY

        return hashlib.sha256(f"{password}{ENCRYPT_KEY}".encode('utf-8')).hexdigest()



