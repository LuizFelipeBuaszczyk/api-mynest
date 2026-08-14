
from repositories.user_repository import UserRepository

class UserService:
    
    @classmethod
    async def create_super_user(cls, data: dict):
        data['is_superuser'] = True
        
        if await UserRepository.exists_superuser():
            raise Exception("Não é possível ter dois super usuários") # TODO Exception especifica
        
        # TODO: Criptografia da senha

        return await UserRepository.insert_user(**data)

    @classmethod
    async def create_user(cls):
        return {}
