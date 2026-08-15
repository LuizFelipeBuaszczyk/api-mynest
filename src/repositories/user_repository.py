from sqlalchemy import text, select
from sqlalchemy.orm import session
from models.users import Users
from utils.contextvars import get_session

class UserRepository:

    @staticmethod
    async def exists_superuser() -> bool:
        session = get_session()
        
        sql = """
        select exists (SELECT 1 FROM users WHERE is_superuser = true) 
        """

        result = session.execute(text(sql)).one()
        
        return result[0]

    @staticmethod
    async def insert_user(**data) -> Users:
        session = get_session()
        
        user = Users(
            username=data['username'],
            password=data['password'],
            email=data['email'],
            is_superuser=data['is_superuser']
        )
        session.add(user)
        return user

    @staticmethod
    async def get_user_by_username(username: str) -> Users | None:
        session = get_session()

        statement = select(Users).where(Users.username == username)
        return session.execute(statement).scalar_one_or_none()
