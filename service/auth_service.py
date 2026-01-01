from fastapi import status
from fastapi.exceptions import HTTPException

from model import Session
from model.user import User
from dto.auth_dto import requestUserLoginDTO

from repository.user_repository import UserRepository

class AuthService():

    def __init__(self):
        pass

    def login(self, user: requestUserLoginDTO):
        
        with Session() as session:
            userRepository = UserRepository(session=session)
            user_db: User = userRepository.find_user_by_username(user.username)

            if not user_db:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid username or password."
                )
            
            if user_db.password != user.password:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid username or password."
                )
            
            return True
