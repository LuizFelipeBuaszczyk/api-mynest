import bcrypt

from fastapi import status
from fastapi.exceptions import HTTPException

from model import Session
from model.user import User
from dto import auth_dto as dto 

from repository.user_repository import UserRepository

class AuthService():

    def __init__(self):
        pass

    async def login(self, user: dto.requestUserLoginDTO):
        
        with Session() as session:
            userRepository = UserRepository(session=session)
            user_db: User = await userRepository.find_user_by_username(user.username)

            if not user_db:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid username or password."
                )
            
            if not self._verify_password(user.password, user_db.password):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid username or password."
                )
            
            return True
        
    def _verify_password(self, password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(
            password.encode("utf-8"),
            hashed_password.encode("utf-8"),
        ) 
    
    async def register_user(self, user: dto.requestUserRegisterDTO):
        with Session() as session:
            userRepository = UserRepository(session=session)
            user_db: User = await userRepository.find_user_by_username(user.username)

            if user_db:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="User already exists."
                )

            new_user_db = User(
                username=user.username,
                password=self._hash_password(user.password)
            )

            await userRepository.insert_user(new_user_db)

            return True
        
    def _hash_password(self, password: str) -> str:
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hashed.decode("utf-8")